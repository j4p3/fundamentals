defmodule UniqueBinarySearchTrees do
  @moduledoc """
  96. Unique Binary Search Trees
  https://leetcode.com/problems/unique-binary-search-trees/
  Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

  Example 2:
  Input: n = 3
  Output: 5

  Example 2:
  Input: n = 1
  Output: 1
  """

  @doc """
  Solution: define relationship between subproblems
  f(n) = sum(f(i-1)*f(n-i)) for i 1..n
  Because we have two independent subtrees of a root, and their combinations are the total count
  """
  def solve(n) do
    counts = %{0 => 1}
    Enum.reduce(1..n, counts, &unique_trees/2)
    |> Map.get(n)
  end

  def unique_trees(limit, cache) do
    count = Enum.map(1..limit, fn i ->
      Map.get(cache, i - 1) * Map.get(cache, limit - i)
    end)
    |> Enum.sum()
    Map.put(cache, limit, count)
  end
end
