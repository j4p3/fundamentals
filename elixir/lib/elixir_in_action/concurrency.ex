defmodule Concurrency do
  def test(times) do
    # some blocking operation we want to perform, like a query
    run_query = fn i ->
      Process.sleep(2000)
      "result: #{i}"
    end

    # the code that's going to a) run the query and b) return it to the parent process
    async_callback_query = fn query_def ->
      caller = self()

      spawn(fn ->
        send(caller, {:query_result, run_query.(query_def)})
      end)
    end

    # what the parent process will do with the message returning from the spawned process
    get_result = fn ->
      receive do
        {:query_result, result} -> result
      end
    end

    # parallel maps to perform the work and receive results
    1..times
    |> Enum.map(&async_callback_query.("q #{&1}"))
    |> Enum.map(fn _ -> get_result.() end)
  end
end
