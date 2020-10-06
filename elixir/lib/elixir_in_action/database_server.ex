defmodule DatabaseServer do
  @spec start :: pid
  def start() do
    spawn(fn ->
      loop(:rand.uniform(1000))
    end)
  end

  @spec run_async(pid, bitstring) :: any
  def run_async(server_pid, query_def) do
    # Use interface function to encapsulate async message passing
    send(server_pid, {:run_query, self(), query_def})
  end

  @spec get_result :: bitstring
  def get_result do
    # Wouldn't this give us the result of the first query to return, rather than the query we want?
    receive do
      {:query_result, result} -> result
    after
      5000 -> {:error, :timeout}
    end
  end

  defp loop(connection) do
    receive do
      {:run_query, caller, query_def} ->
        send(caller, {:query_result, run_query(connection, query_def)})
    end

    loop(connection)
  end

  defp run_query(connection, query_def) do
    # call db here
    Process.sleep(2000)
    "connection #{connection}: query #{query_def} result"
  end
end
