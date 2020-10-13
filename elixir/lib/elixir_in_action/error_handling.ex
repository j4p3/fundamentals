defmodule ErrorHandling do
  def tryer(fun) do
    try do
      fun.()
      IO.puts("ran without erroring")
    catch
      type, value ->
        IO.puts("raised #{inspect(type)}:\n #{inspect(value)}")
    end
  end

  def trap_exit() do
    # Mark this process should trap exits
    Process.flag(:trap_exit, true)

    # Create an error exit
    # The linked process exiting will cause this process to exit
    # If this process exits, any linked processes will also exit
    spawn_link(fn -> raise("Test error") end)

    # Handle error exits
    receive do
      {:EXIT, _pid, error, _trace} ->
        IO.inspect(error)
    end
  end

  def trap_monitored_process_exit() do
    # Create a process to monitor
    monitored_pid = spawn(fn -> Process.sleep(1000) end)

    # Set up monitor on process:
    # If the child process exits, this process will receive a message
    # If this process exits, the child process will continue
    Process.monitor(monitored_pid)

    receive do
      message -> IO.inspect(message)
    end
  end
end
