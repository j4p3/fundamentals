defmodule ValidSudoku do
  @moduledoc """
  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

  Each row must contain the digits 1-9 without repetition.
  Each column must contain the digits 1-9 without repetition.
  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
  Note:

  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  Only the filled cells need to be validated according to the mentioned rules.


  Example 1:
  Input: board =
  [["5","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]]
  Output: true

  Example 2:
  Input: board =
  [["8","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]]
  Output: false
  Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


  Example 3:
  board=
  [[".",".",".",".","5",".",".","1","."],
   [".","4",".","3",".",".",".",".","."],
   [".",".",".",".",".","3",".",".","1"],
   ["8",".",".",".",".",".",".","2","."],
   [".",".","2",".","7",".",".",".","."],
   [".","1","5",".",".",".",".",".","."],
   [".",".",".",".",".","2",".",".","."],
   [".","2",".","9",".",".",".",".","."],
   [".",".","4",".",".",".",".",".","."]]

  Constraints:

  board.length == 9
  board[i].length == 9
  board[i][j] is a digit 1-9 or '.'.
  """
  @spec is_valid_sudoku(board :: [[char]]) :: boolean
  def is_valid_sudoku(board) do
    accumulator = %{
      x: 0,
      y: 0,
      rows: for(i <- 0..8, into: %{}, do: {i, MapSet.new()}),
      columns: for(i <- 0..8, into: %{}, do: {i, MapSet.new()}),
      grids: for(i <- 0..8, into: %{}, do: {i, MapSet.new()})
    }

    Enum.reduce_while(board, accumulator, &evaluate_row/2)
    # if Enum.reduce_while(board, accumulator, &evaluate_row/2), do: true, else: false
  end

  defp evaluate_row(row, %{y: y} = acc) do
    row_results = Enum.reduce_while(row, acc, &evaluate_square/2)

    if row_results do
      {:cont,
       %{
         row_results
         | x: 0,
           y: y + 1
       }}
    else
      {:halt, false}
    end
  end

  defp evaluate_square(square, %{x: x, y: y, rows: rows, columns: columns, grids: grids} = acc) do
    if square == "." do
      {:cont, %{acc | x: x + 1}}
    else
      grid_num = div(x, 3) + 3 * div(y, 3)
      IO.puts("#{x}, #{y}: #{square} (#{grid_num})")
      IO.puts("is there a #{square} in grid num #{grid_num}? #{MapSet.member?(grids[grid_num], square)}")

      if MapSet.member?(rows[y], square) ||
           MapSet.member?(columns[x], square) || MapSet.member?(grids[grid_num], square) do
        {:halt, false}
      else
        {:cont,
         %{
           acc
           | x: x + 1,
             rows: %{rows | y => MapSet.put(rows[y], square)},
             columns: %{columns | x => MapSet.put(columns[x], square)},
             grids: %{grids | grid_num => MapSet.put(grids[grid_num], square)}
         }}
      end
    end
  end
end
