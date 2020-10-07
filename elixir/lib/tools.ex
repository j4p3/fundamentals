defmodule Tools do
  # Dump info on currently running processes
  @spec processes :: [list]
  def processes() do
    Process.list() |> Enum.map(&:erlang.process_info(&1))
  end
end
