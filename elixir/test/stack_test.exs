defmodule StackTest do
  use ExUnit.Case
  alias ElixirImplementations.Stack, as: Stack

  test "create" do
    assert Stack.new()
  end

  test "push" do
    depth = Stack.new() |> Stack.push(1) |> Stack.depth()
    assert depth == 1
  end

  test "pop" do
    {_, stack} = Stack.new() |> Stack.push(1) |> Stack.pop()
    assert Stack.depth(stack) == 0
  end

  test "item order" do
    {top, _} = Stack.new() |> Stack.push(1) |> Stack.push(2) |> Stack.pop()
    assert top == 2
  end
end
