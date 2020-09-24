defmodule FileUtil do
  def count_lines(file_path) do
    File.read(file_path)
    |> lines_num
  end

  defp lines_num({:ok, contents}) do
    contents
    |> String.split("\n")
    |> length
  end

  defp lines_num(error), do: error
end
