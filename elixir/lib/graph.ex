defmodule ElixirImplementations.Graph do
  @type node :: %{value: any, neighbors: {}}
  
  def new(value) do
    %{value: value, neighbors: {}}
  end
end