defmodule TreeTest do
  use ExUnit.Case
  alias ElixirImplementations.Tree, as: Tree

  test "create" do
    assert Tree.new(10).value == 10
  end

  test "insert" do
    tree = Tree.new(10) |> Tree.insert(5)
    assert tree.left.value == 5
  end

  test "insert recursive" do
    tree = Tree.new(10) |> Tree.insert(5) |> Tree.insert(15) |> Tree.insert(6)
    assert tree.left.right.value == 6
  end
end
