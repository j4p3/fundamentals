defmodule Todo do
  require MultiMap
  @type todo_list :: %{}
  @type entry :: %{date: Date, message: charlist}
  @spec new :: %{}
  def new, do: MultiMap.new()

  @spec add(todo_list, entry) :: todo_list
  def add(todos, entry), do: MultiMap.insert(todos, entry.date, entry)

  @spec entries(todo_list, tuple) :: list
  def entries(todos, date), do: MultiMap.get(todos, date)
end
