defmodule Tasks do
  def test(times) do
    run_query = fn i ->
      Process.sleep(2000)
      "result #{i}"
    end

    1..times
    |> Enum.map(&Task.async(fn -> run_query.("query #{&1}") end))
    |> Enum.map(&Task.await/1)
  end
end
