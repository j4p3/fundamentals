defmodule PerfectSquares do
  require IEx
  @moduledoc """
  https://leetcode.com/problems/perfect-squares/

  Given an integer n, return the least number of perfect square numbers that sum to n.
  A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

  Example 1:
  ----------
  Input: n = 12
  Output: 3
  Explanation: 12 = 4 + 4 + 4.

  Example 2:
  -----------
  Input: n = 13
  Output: 2
  Explanation: 13 = 4 + 9.


  Constraints:
  ------------
  1 <= n <= 104
  """
  # @squares [100, 81, 64, 49, 26, 25, 16, 9, 4, 1]

  # @doc """
  # Plan: iterate down through squares, increment sum, increment count
  # """
  # def num_squares(input) when input < 1, do: nil
  # def num_squares(input) when input > 104, do: nil

  # def num_squares(input) do
  #   add_squares(input)
  # end

  # defp add_squares(target_sum, possible_squares \\ @squares, used_squares \\ [], square_count \\ 0, current_sum \\ 0)

  # defp add_squares(target_sum, possible_squares, used_squares, square_count, current_sum)
  #      when current_sum < target_sum do
  #   largest_square = Enum.find(possible_squares, fn s -> current_sum + s <= target_sum end)
  #   # @todo optimize: trim squares list
  #   add_squares(target_sum, possible_squares, [largest_square | used_squares], square_count + 1, current_sum + largest_square)
  # end

  # defp add_squares(target_sum, _possible_squares, used_squares, square_count, current_sum)
  #      when current_sum == target_sum,
  #      do: {square_count, Enum.reverse(used_squares)}

  @doc """
  Plan 2: build cache of min square values on the way up to input
  """
  def num_squares(input) when input < 1, do: nil
  def num_squares(input) when input > 10_000, do: nil
  def num_squares(input) do
    squares = for n <- (1..trunc(:math.sqrt(input))), do: :math.pow(n, 2) |> trunc()
    add_squares(input, squares)
  end

  @doc """
  Iterate through index up to input, build cache
  """
  defp add_squares(target, squares, index \\ 0, cache \\ %{0 => 0})
  defp add_squares(target, squares, index, cache) when index < target do
    add_squares(
      target,
      squares,
      index + 1,
      Map.put(cache, index, least_squares(index, cache, squares))
    )
  end
  defp add_squares(target, squares, index, cache) when index == target do
    least_squares(index, cache, squares)
  end

  @doc """
  Iterate through squares for given index, determine next cached value
  """
  defp least_squares(index, cache, squares)
  defp least_squares(index, cache, [next_square | tail]) when index < next_square, do: least_squares(index, cache, tail)
  defp least_squares(index, cache, [next_square | tail]) do
    least_squares(
      index,
      Map.put(cache, index, min(cache[index], cache[index - next_square] + 1)),
      tail
    )
  end
  defp least_squares(index, cache, []), do: cache[index]
end
