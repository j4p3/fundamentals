defmodule EchoServer do
  use GenServer

  def start_link(id) do
    GenServer.start_link(__MODULE__, nil, name: via_tuple(id))
  end

  def call(id, request) do
    GenServer.call(via_tuple(id), request)
  end

  def handle_call(request, _caller, state) do
    {:reply, request, state}
  end

  defp via_tuple(id) do
    {:via, Registry, {:test_registry, {__MODULE__, id}}}
  end
end
