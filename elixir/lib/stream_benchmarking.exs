defmodule StreamBenchmarking do
  def benchmark([length]) do
    Benchee.run(%{
      "stream" => fn -> process_stream(String.to_integer(length)) end,
      "enum" => fn -> process_enum(String.to_integer(length)) end
    })
  end

  def process_stream(length) do
    1..length
    |> Stream.map(&:math.sqrt(&1))
    |> Stream.map(&:math.pow(&1, 2))
    |> Stream.run()
  end

  def process_enum(length) do
    1..length
    |> Enum.map(&:math.sqrt(&1))
    |> Enum.map(&:math.pow(&1, 2))
  end
end

StreamBenchmarking.benchmark(System.argv())
