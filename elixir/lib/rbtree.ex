defmodule ElixirImplementations.RBTree do
  @type tree_node :: %{value: any, color: :red | :black, left: %{} | nil, right: %{} | nil}

  def new(new_value) do
    %{value: new_value, color: :red, left: nil, right: nil}
  end

  def insert(nil, new_value), do: new(new_value)

  def insert(%{value: value, color: color, left: left, right: right}, new_value) do
    if new_value < value do
      %{value: value, left: insert(left, new_value), right: right}
    else
      %{value: value, left: left, right: insert(right, new_value)}
    end

    if right.color == :red do
      # lRotate
    end

    if left.color == :red or (left.left and left.left.color == :red) do
      # rrotate
    end

    if left.color == :red and right.color == :red do
      # flip
    end
  end
end
