defmodule KeyValueStore do

  # Callback functions
  # These are expected by the server
  # By implementing them, any module can be run on the server
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

  @spec handle_cast({:put, any, any}, map) :: map
  def handle_cast({:put, key, value}, state) do
    Map.put(state, key, value)
  end

  # Interface functions
  # They let a client directly call the module they're interested in
  # Client doesn't need to know about how to pass a message to the server
  @spec start :: pid
  def start do
    ServerProcess.start(KeyValueStore)
  end

  @spec put(pid, any, any) :: any
  def put(pid, key, value) do
    ServerProcess.cast(pid, {:put, key, value})
  end

  @spec get(pid, any) :: any
  def get(pid, key) do
    ServerProcess.call(pid, {:get, key})
  end
end
