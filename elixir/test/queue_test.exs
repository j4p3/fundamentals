defmodule QueueTest do
  use ExUnit.Case
  alias ElixirImplementations.Queue, as: Queue

  test "create" do
    assert Queue.new()
  end

  test "push" do
    depth = Queue.new() |> Queue.push(1) |> Queue.depth()
    assert depth == 1
  end

  test "pop" do
    {_, queue} = Queue.new() |> Queue.push(1) |> Queue.pop()
    assert Queue.depth(queue) == 0
  end

  test "item order" do
    {top, _} = Queue.new() |> Queue.push(1) |> Queue.push(2) |> Queue.pop()
    assert top == 1
  end
end
