defmodule MultiMap do
  @type multi_map :: %{}

  @spec new :: %{}
  def new(), do: %{}

  @spec insert(multi_map, any, any) :: multi_map
  def insert(map, key, value) do
    Map.update(
      map,
      key,
      [value],
      &[value | &1]
    )
  end

  @spec get(multi_map, any) :: list
  def get(map, key) do
    Map.get(map, key)
  end
end
