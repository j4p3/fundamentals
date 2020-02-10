defmodule ElixirImplementations.Stack do
  defstruct elements: []

  def new do
    %__MODULE__{}
  end

  def push(stack, el) do
    %__MODULE__{stack | elements: [el | stack.elements]}
  end

  def pop(%__MODULE__{elements: []}), do: raise("empty")

  def pop(%__MODULE__{elements: [first | rest]}) do
    {first, %__MODULE__{elements: rest}}
  end

  def depth(%__MODULE__{elements: elements}), do: length(elements)
end
