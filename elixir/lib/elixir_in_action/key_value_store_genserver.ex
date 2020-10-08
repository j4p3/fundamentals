defmodule KeyValueStoreGenserver do
  use GenServer

  # Callback functions
  @spec init(any) :: {:ok, %{}}
  def init(_) do
    {:ok, %{}}
  end

  # @spec handle_call({:get, any} | {:put, any, any}, {pid, any}, map) :: {:reply, map}
  def handle_call({:put, key, value}, _, state) do
    {:reply, nil, Map.put(state, key, value)}
  end
  def handle_call({:get, key}, _, state) do
    {:reply, Map.get(state, key), state}
  end

  @spec handle_cast({:put, any, any}, map) :: {:noreply, map}
  def handle_cast({:put, key, value}, state) do
    {:noreply, Map.put(state, key, value)}
  end

  # Interface functions
  @spec start :: :ignore | {:error, any} | {:ok, pid}
  def start do
    GenServer.start(KeyValueStoreGenserver, nil)
  end

  @spec put(pid, any, any) :: any
  def put(pid, key, value) do
    GenServer.cast(pid, {:put, key, value})
  end

  @spec get(pid, any) :: any
  def get(pid, key) do
    GenServer.call(pid, {:get, key})
  end
end
