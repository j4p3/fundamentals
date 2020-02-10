defmodule ElixirImplementations.Queue do
  alias __MODULE__, as: Queue
  defstruct elements: []

  def new do
    %Queue{}
  end

  def push(queue, el) do
    %Queue{queue | elements: queue.elements ++ [el]}
  end

  def pop(%Queue{elements: []}), do: raise("empty")

  def pop(%Queue{elements: [first | rest]}) do
    {first, %Queue{elements: rest}}
  end

  def depth(%Queue{elements: elements}), do: length(elements)
end
