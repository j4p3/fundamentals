defmodule StockCooldown do
  @moduledoc """
  You are given an array prices where prices[i] is the price of a given stock on the ith day.

  Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

  After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
  Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


  Example 1:

  Input: prices = [1,2,3,0,2]
  Output: 3
  Explanation: transactions = [buy, sell, cooldown, buy, sell]
  Example 2:

  Input: prices = [1]
  Output: 0


  Constraints:

  1 <= prices.length <= 5000
  0 <= prices[i] <= 1000
  """

  @spec max_profit(prices :: [integer]) :: integer
  def max_profit(prices) do
    Enum.reduce(prices, [{-Enum.at(prices, 0), 0, 0}], &profits_today/2)
    |> Enum.at(0)
    |> Tuple.to_list()
    |> Enum.max()
  end

  defp profits_today(price, [{y_holding, y_not_holding, y_cooldown} | profits_list]) do
    [
      {
        max(y_holding, y_not_holding - price), # holding: held or bought
        max(y_not_holding, y_cooldown), # not holding: not holding or cooldown
        y_holding + price # cooldown: sold
      },
      {y_holding, y_not_holding, y_cooldown} | profits_list
    ]
  end
end
