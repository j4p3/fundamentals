defmodule Math do
  @spec factorial(non_neg_integer) :: pos_integer
  def factorial(0), do: 1
  def factorial(n), do: n * factorial(n - 1)

  def max(a, b) do
    cond do
      a >= b -> a
      true -> b
    end
  end

  # Same impl, case vs cond
  def max(a, b) do
    case a >= b do
      true -> a
      false -> b
    end
  end
end
