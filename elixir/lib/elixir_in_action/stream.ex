defmodule Strims do
  @spec roots(any) :: :ok
  def roots(list) do
    # Stream enumerators return a lambda rather than the result of the operation
    # When an Enum eagerly evaulated enumerator is called, then the chain of lambdas is executed on the input
    list
    |> Stream.filter(&is_number(&1) and &1 > 0)
    |> Stream.map(&{&1, :math.sqrt(&1)})
    |> Stream.with_index
    |> Enum.each(
      fn({{input, result}, index}) ->
        IO.puts("#{index + 1}. #{input}^(1/2) = #{result}")
      end
    )
  end
end
