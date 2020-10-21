defmodule HomebrewAgent do
  use GenServer

  def start_link(init_func) do
    GenServer.start_link(__MODULE__, init_func)
  end

  def init(init_func) do
    {:ok, init_func.()}
  end

  def get(pid, func) do
    Genserver.call(pid, {:get, func})
  end

  def update(pid, func) do
    GenServer.call(pid, {:update, func})
  end

  def handle_call({:get, func}, _caller, state) do
    {:reply, func.(state), state}
  end
  def handle_call({:update, func}, _caller, state) do
    {:reply, :ok, func.(state)}
  end
end
