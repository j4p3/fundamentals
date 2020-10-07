defmodule ServerProcess do
  @spec start(atom) :: pid
  def start(callback_module) do
    spawn(fn ->
      initial_state = callback_module.init()
      loop(callback_module, initial_state)
    end)
  end

  @spec call(pid, any) :: any
  def call(server_pid, request) do
    send(server_pid, {request, self()})

    receive do
      {:response, response} -> response
    end
  end

  defp loop(callback_module, current_state) do
    receive do
      {request, caller} ->
        {response, new_state} = callback_module.handle_call(request, current_state)
        send(caller, {:response, response})
        loop(callback_module, new_state)  # strange - in this server, we loop from inside receive block
    end
  end
end
