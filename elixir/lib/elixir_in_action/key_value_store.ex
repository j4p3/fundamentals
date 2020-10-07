defmodule KeyValueStore do
  @spec init :: %{}
  def init do
    %{}
  end

  @spec start :: pid
  def start do
    ServerProcess.start(KeyValueStore)
  end

  @spec put(pid, any, any) :: any
  def put(pid, key, value) do
    ServerProcess.call(pid, {:put, key, value})
  end

  @spec get(pid, any) :: any
  def get(pid, key) do
    ServerProcess.call(pid, {:get, key})
  end

  @spec handle_call({:get, any} | {:put, any, any}, map) :: {any, map}
  def handle_call({:put, key, value}, state) do
    {:ok, Map.put(state, key, value)}
  end
  def handle_call({:get, key}, state) do
    {Map.get(state, key), state}
  end
end
