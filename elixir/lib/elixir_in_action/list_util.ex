# Tail call recursion:
#
# a function returning
#   current_value + recursive_fn(remaining_to_be_processed)
# cannot be optimized, because we need to keep a stack for current_value
#
# whereas a function returning
#   recursive_fn(current_value, remaining_to_be_processed)
# can be optimized

defmodule ListUtil do
  @spec sum([number]) :: number
  def sum([]), do: 0
  # Not tail call optimized, because:
  # the final return value is an operation performed in the function
  def sum([head | tail]), do: head + sum(tail)
end

defmodule RecursionOptimized do
  defmodule ListUtil do
    @spec sum([number]) :: number
    def sum(list) do
      add(0, list)
    end

    @spec add(number, list) :: number
    defp add(sum, []), do: sum
    # Tail call optimized, because the final return value is simply the result of a function
    # Therefore no stack is needed, we can use BEAM's equivalent of a goto/pointer
    defp add(sum, [head | tail]) do
      add(sum + head, tail)
    end
  end
end
