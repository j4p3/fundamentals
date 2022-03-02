defmodule LongestPalindrome do
  require IEx
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
  # @spec longest_palindrome(input :: String.t) :: String.t
  # def longest_palindrome(input) do
  #   input
  #   |> String.to_charlist()
  #   |> (fn s -> {s, Enum.count(s)} end).()
  #   |> palindromic_length()
  #   |> IO.inspect()
  #   |> Enum.map(fn {l, _o} -> l end)
  #   |> Enum.max()
  # end

  @spec longest_palindrome(input :: String.t) :: String.t
  def longest_palindrome(input) do
    input
    |> String.to_charlist()
    |> Enum.reduce({0, %{}, [0], 0}, &build_palindrome/2)
  end

  def build_palindrome(letter, {charlist, [current_palindrome | palindromes]}) do
    if letter == Enum.at(charlist - length(current_palindrome)) do
      {
        charlist,
        [letter | current_palindrome]
      }
    else
      if letter == Enum.at(charlist - length(current_palindrome)) do

      end
    end
  end

  # defp build_palindrome(letter, {index, letters, [length | lengths], offset = 0}) when length > 1 do
  #   # in palindrome
  #   # no offset
  #   new_length = if letter == letters[index - (length + offset)], do: length + 2, else: 1
  #   {
  #     index + 1,
  #     Map.put(letters, index, letter),
  #     [new_length | [length | lengths]],
  #     offset
  #   }
  # end

  # defp build_palindrome(letter, {index, letters, [length | lengths], offset = 0}) do
  #   # not in palindrome
  #   # no offset
  #   if letter == letters[index - (length + offset)] do
  #     {
  #       index + 1,
  #       Map.put(letters, index, letter),
  #       [length + 1 | [length | lengths]],
  #       offset
  #     }
  #   else
  #     build_palindrome(letter, {index, letters, [length | lengths], 1})
  #   end
  #   {

  #   }
  # end

  # defp build_palindrome(letter, {index, letters, [length | lengths], offset = 1}) do
  #   # not in palindrome
  #   # with offset

  # end

  # defp build_palindrome(letter, {index, letters, [length | lengths], offset}) do
  #   # if offset, use it
  #   # increment or reset

  #   # if no offset, try 0
  #   # try 1
  #   # increment or reset

  #   # need base case for no-current-palindrome, in which case we should inc by 1?
  #   # couple of these build_palindrome clauses for offset, no offset, for in palindrome, not in palindrome?

  #   {new_length, new_offset} = if letter == letters[index - (length + offset)] do
  #     {length + 2, offset}
  #   else
  #     if offset == 0 and letter == letters[index - (length + offset + 1)] do
  #       {length + 2, offset + 1}
  #     else
  #       {1, 0}
  #     end
  #   end

  #   {
  #     index + 1,
  #     Map.put(letters, index, letter),
  #     [new_length | [length | lengths]],
  #     new_offset
  #   }
  # end

  # defp palindromic_length(input_tuple, index \\ 0, lengths \\ [])
  # defp palindromic_length({_input, input_size}, index, lengths) when index == input_size, do: lengths
  # defp palindromic_length(input_tuple, index, _lengths) when index == 0, do: palindromic_length(input_tuple, index + 1, [{1, 0}])
  # defp palindromic_length({input, input_size}, index, [{current_length, offset} | lengths]) when index < input_size do
  #   # @todo handle offset - don't continue to increment by 2 when incrementing in an offset-2 palindrome
  #   IO.inspect({"#{index}: #{Enum.at(input, index)}", {current_length, offset}})
  #   lengths = if Enum.at(input, index) == Enum.at(input, index - (current_length + offset)) do
  #     [{current_length + 1, 0} | lengths]
  #   else
  #     [{1, 0} | lengths]
  #   end
  #   palindromic_length(
  #     {input, input_size},
  #     index + 1,
  #     lengths
  #   )
  # end
end
