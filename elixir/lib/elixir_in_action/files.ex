defmodule Files do
  @line_width 80

  def line_lengths(path) do
    File.stream!(path)
    |> Stream.map(&(String.replace&1, "\n", ""))
    |> Enum.map&(String.length(&1))
  end

  def long_lines(path) do
    File.stream!(path)
    |> Stream.map(&(String.replace&1, "\n", ""))
    |> Enum.filter(&(String.length(&1) > @line_width))
  end

  def longest_line(path) do
    File.stream!(path)
    |> Stream.map(&(String.replace&1, "\n", ""))
    |> Stream.map(&({String.length(&1), &1}))
    |> Stream.with_index
    |> Enum.reduce(
      fn
        {{len, line}, line_idx},
        {{long_len, long_line}, long_idx} ->
        IO.puts(line)
        case len > long_len do
          true -> {{len, line}, line_idx}
          false -> {{long_len, long_line}, long_idx}
        end
      end
    )
    |> format
  end

  defp format({{len, line}, idx}) do
    "\##{idx + 1}. (#{len}) #{line}"
  end
end
