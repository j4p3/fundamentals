defmodule Fraction do
  defstruct numerator: nil, denominator: nil

  def new(n, d) do
    %Fraction{numerator: n, denominator: d}
  end

  def value(f), do: f.numerator / f.denominator

  def add(f1, f2) do
    new(
      f1.numerator * f2.denominator + f2.numerator * f1.denominator,
      f1.denominator * f2.denominator
    )
  end
end
