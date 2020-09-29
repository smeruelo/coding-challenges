defmodule Strain do
  @doc """
  Given a `list` of items and a function `fun`, return the list of items where
  `fun` returns true.

  Do not use `Enum.filter`.
  """
  @spec keep(list :: list(any), fun :: (any -> boolean)) :: list(any)
  def keep(list, fun), do: keep_rec(list, fun, [])

  @spec keep_rec(list :: list(any), fun :: (any -> boolean), acc :: list(any)) :: list(any)
  defp keep_rec([], _, acc), do: Enum.reverse(acc)
  defp keep_rec([head | tail], fun, acc) do
	keep_rec(tail, fun, (if fun.(head), do: [head | acc], else: acc))
  end

  @doc """
  Given a `list` of items and a function `fun`, return the list of items where
  `fun` returns false.

  Do not use `Enum.reject`.
  """
  @spec discard(list :: list(any), fun :: (any -> boolean)) :: list(any)
  def discard(list, fun), do: keep_rec(list, fn x -> not fun.(x) end, [])
end
