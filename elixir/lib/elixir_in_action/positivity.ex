defmodule Positivity do
  @spec test(any) :: :negative | :positive | :zero
  def test(x) when x < 0 do
    :negative
  end

  def test(0), do: :zero

  def test(x) when x > 0 do
    :positive
  end
end
