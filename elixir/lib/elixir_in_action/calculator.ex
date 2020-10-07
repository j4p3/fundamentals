defmodule Calculator do
  def start do
    spawn(fn -> loop(0) end)
  end

  def value(server_pid) do
    send(server_pid, {:value, self()})
    receive do
      {:response, value} -> value
    end
  end

  def add(server_pid, value), do: send(server_pid, {:add, value})
  def sub(server_pid, value), do: send(server_pid, {:sub, value})
  def mul(server_pid, value), do: send(server_pid, {:mul, value})
  def div(server_pid, value), do: send(server_pid, {:div, value})
  def exp(server_pid, value), do: send(server_pid, {:exp, value})
  def clear(server_pid), do: send(server_pid, {:clear})

  defp loop(current_value) do
    new_value = receive do
      message -> process_message(current_value, message)
    end

    loop(new_value)
  end

  defp process_message(current_value, {:value, caller}) do
    send(caller, {:response, current_value})
    current_value
  end
  defp process_message(current_value, {:add, value}), do: current_value + value
  defp process_message(current_value, {:sub, value}), do: current_value - value
  defp process_message(current_value, {:mul, value}), do: current_value * value
  defp process_message(current_value, {:div, value}), do: current_value / value
  defp process_message(current_value, {:exp, value}), do: :math.pow(current_value, value)
  defp process_message(_current_value, {:clear}), do: 0
  defp process_message(current_value, {invalid_request}) do
    IO.puts("Invalid input #{invalid_request}")
    current_value
  end
end