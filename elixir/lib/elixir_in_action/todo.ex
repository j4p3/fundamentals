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
