defmodule KeyValueStore do
  @spec init :: %{}
  def init do
    %{}
  end

  @spec handle_call({:get, any} | {:put, any, any}, map) :: {any, map}
  def handle_call({:put, key, value}, state) do
    {:ok, Map.put(state, key, value)}
  end
  def handle_call({:get, key}, state) do
    {Map.get(state, key), state}
  end
end
