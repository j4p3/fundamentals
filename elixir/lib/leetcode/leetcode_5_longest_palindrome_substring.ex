defmodule LongestPalindrome do
  @moduledoc """
  Given a string s, return the longest palindromic substring in s.

  Example 1:
  Input: s = "babad"
  Output: "bab"
  Note: "aba" is also a valid answer.

  Example 2:
  Input: s = "cbbd"
  Output: "bb"

  Example 3:
  Input: s = "a"
  Output: "a"

  Example 4:
  Input: s = "ac"
  Output: "a"

  Constraints:

  1 <= s.length <= 1000
  s consist of only digits and English letters.
  """
  @spec run(input :: String.t()) :: integer()
  def run(input) do
    input
    |> interpolate()
    |> max_pal()
    |> then(fn max ->
      div(max, 2) + 1
    end)
  end

  @spec interpolate(String.t()) :: [integer()]
  def interpolate(input) do
    input
    |> String.to_charlist()
    |> Enum.map(fn c ->
      [~c(.), c]
    end)
    |> List.flatten()
    |> tl()
  end

  @doc """
  Palindromic length from each letter in the input.
  """
  @spec max_pal([integer()]) :: integer()
  def max_pal(input) do
    max_pal(input, 1, 0)
  end

  @spec max_pal([integer()], integer(), integer()) :: integer()
  def max_pal(input, max_len, i) when i == length(input) - 1, do: max_len

  def max_pal(input, max_len, i) do
    max_pal(
      input,
      Enum.max([pal_length(input, i), max_len]),
      i + 1
    )
  end

  @doc """
  The palindromic length from the center of an odd-numbered palindrome.

  Recursively compare from center, discarding current letter and incrementing count.
  """
  @spec pal_length([integer()], integer()) :: integer()
  def pal_length(input, target) do
    pal_length(
      1,
      Enum.reverse(Enum.slice(input, 0..(target - 1))),
      Enum.slice(input, (target + 1)..length(input))
    )
  end

  @spec pal_length(integer(), [integer()], [integer()]) :: integer()
  def pal_length(current_length, [], []), do: current_length
  def pal_length(current_length, _, []), do: current_length
  def pal_length(current_length, [], _), do: current_length

  def pal_length(current_length, [l_head | l_tail], [r_head | r_tail]) do
    if l_head == r_head do
      pal_length(current_length + 2, l_tail, r_tail)
    else
      current_length
    end
  end
end
