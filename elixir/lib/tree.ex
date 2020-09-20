defmodule ElixirImplementations.Tree do
  # not actually necessary unless you want to define a spec
  @type tree_node :: %{value: any, left: %{} | nil, right: %{} | nil}

  @doc "Return a new tree."
  @spec new(any) :: %{value: any, left: :leaf, right: :leaf}
  def new(value) do
    %{value: value, left: nil, right: nil}
  end

  @doc "Insert value onto tree from provided node. Return updated tree."
  @spec insert(tree_node | :leaf, any) :: tree_node
  def insert(nil, value), do: new(value)

  def insert(%{value: existing_value, left: left, right: right}, value) do
    if value < existing_value do
      %{value: existing_value, left: insert(left, value), right: right}
    else
      %{value: existing_value, left: left, right: insert(right, value)}
    end
  end
end
