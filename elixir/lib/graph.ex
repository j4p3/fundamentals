defmodule ElixirImplementations.Graph do
  @type graph_node :: %{value: any, neighbors: {}}

  def new(value) do
    %{value: value, neighbors: {}}
  end
end
