defmodule Todo do
  require MultiMap
  defstruct id_sequence: 1, entries: %{}

  @type todo_list :: %{}
  @type entry :: %{date: Date, message: charlist}

  def new, do: %Todo{}

  def add(todos, entry) do
    entry = Map.put(entry, :id, todos.id_sequence)

    entries = Map.put(
      todos.entries,
      todos.id_sequence,
      entry
    )

    %Todo{
      todos |
      entries: entries,
      id_sequence: todos.id_sequence
    }
  end

  @spec entries(todo_list, tuple) :: list
  def entries(todos, date), do: MultiMap.get(todos, date)
end
