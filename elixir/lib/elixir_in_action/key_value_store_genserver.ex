defmodule KeyValueStoreGenserver do
  use GenServer

  @impl GenServer
  @spec init(any) :: {:ok, %{}}
  def init(_) do
    {:ok, %{}}
  end

  # @spec handle_call({:get, any} | {:put, any, any}, {pid, any}, map) :: {:reply, map}
  @impl GenServer
  def handle_call({:put, key, value}, _, state) do
    {:reply, nil, Map.put(state, key, value)}
  end

  def handle_call({:get, key}, _, state) do
    {:reply, Map.get(state, key), state}
  end

  @impl GenServer
  @spec handle_cast({:put, any, any}, map) :: {:noreply, map}
  def handle_cast({:put, key, value}, state) do
    {:noreply, Map.put(state, key, value)}
  end

  def start_link() do
    GenServer.start(__MODULE__, nil, name: __MODULE__)
  end

  @spec put(any, any) :: any
  def put(key, value) do
    GenServer.cast(__MODULE__, {:put, key, value})
  end

  @spec get(any) :: any
  def get(key) do
    GenServer.call(__MODULE__, {:get, key})
  end
end
