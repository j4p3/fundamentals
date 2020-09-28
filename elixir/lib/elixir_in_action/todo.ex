defmodule Todo do
  require MultiMap
  defstruct id_sequence: 1, entries: %{}

  @type todo_list :: %{}
  @type entry :: %{date: Date, message: charlist}

  def new, do: %Todo{}

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
        new_entry = Enum.reduce(
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
