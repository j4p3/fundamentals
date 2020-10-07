
# Step 2: build a "stateful" abstraction atop a functional data structure
defmodule TodoServer do
  def start() do
    Process.register(spawn(fn -> loop(Todo.new()) end), :todo_server)
  end

  def create(todo), do: send(:todo_server, {:create, todo})
  def update(todo_id, todo), do: send(:todo_server, {:update, todo_id, todo})
  def delete(todo_id), do: send(:todo_server, {:delete, todo_id})
  def entries(date) do
    send(:todo_server, {:entries, self(), date})
    receive do
      {:entries_response, entries} -> entries
    after
      5000 -> {:error, :timeout}
    end
  end

  defp loop(state) do
    new_state = receive do
      message -> process_message(state, message)
    end
    loop(new_state)
  end

  defp process_message(todo_list, {:create, entry}), do: Todo.create(todo_list, entry)
  defp process_message(todo_list, {:update, entry_id, entry}), do: Todo.update(todo_list, entry_id, entry)
  defp process_message(todo_list, {:delete, entry_id}), do: Todo.delete(todo_list, entry_id)
  defp process_message(todo_list, {:entries, caller, date}) do
    send(caller, {:entries_response, Todo.entries(todo_list, date)})
    todo_list  # ensure process_message returns list data so it can be preserved to next loop
  end
end

# Step 1: build a functional data structure
defmodule Todo do
  defstruct id_sequence: 1, entries: %{}

  @type todo_list :: %{}
  @type entry :: %{date: Date, message: charlist}

  def new, do: %Todo{}

  def new(entry_data) do
    Enum.reduce(entry_data, %Todo{}, &create(&2, &1))
  end

  def create(todos, entry) do
    entry = Map.put(entry, :id, todos.id_sequence)

    entries =
      Map.put(
        todos.entries,
        todos.id_sequence,
        entry
      )

    %Todo{
      todos
      | entries: entries,
        id_sequence: todos.id_sequence + 1
    }
  end

  def update(todos, id, update_body) do
    case Map.fetch(todos.entries, id) do
      :error ->
        todos

      {:ok, existing_entry} ->
        new_entry =
          Enum.reduce(
            update_body,
            existing_entry,
            fn {k, v}, acc ->
              %{acc | k => v}
            end
          )

        entries =
          Map.put(
            todos.entries,
            new_entry.id,
            new_entry
          )

        %Todo{todos | entries: entries}
    end
  end

  def delete(todos, id) do
    {_, updated} = Map.pop(todos.entries, id)
    %Todo{todos | entries: updated}
  end

  def entries(todos, date) do
    todos.entries
    |> Stream.filter(fn {_, entry} -> entry.date == date end)
    |> Enum.map(fn {_, entry} -> entry end)
  end
end

defmodule Todo.CsvImport do
  def import(path) do
    entries = File.stream!(path)
    |> Stream.map(&String.replace(&1, "\n", ""))
    |> Stream.map(&String.split(&1, ","))
    |> Stream.map(fn [date, message] ->
      [year, month, day] = Enum.map(String.split(date, "/"), &String.to_integer/1)
      {{year, month, day}, message}
    end)
    |> Enum.map(fn {{year, month, day}, message} ->
      %{
        date: "~D[#{year}-#{month}-#{day}",
        message: message
      }
    end)

    Todo.new(entries)
  end
end

defimpl String.Chars, for: Todo do
  def to_string(_) do
    "#Todo"
  end
end
