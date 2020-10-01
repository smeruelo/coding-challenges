# https://exercism.io/my/solutions/fc842117968b433daa891a425c1aa398

defmodule BeerSong do
  @spec bottles(integer) :: String.t()
  defp bottles(0), do: "no more bottles"
  defp bottles(1), do: "1 bottle"
  defp bottles(n), do: "#{n} bottles"

  @doc """
  Get a single verse of the beer song
  """
  @spec verse(integer) :: String.t()
  def verse(0) do
    """
    No more bottles of beer on the wall, no more bottles of beer.
    Go to the store and buy some more, 99 bottles of beer on the wall.
    """
  end

  def verse(n) do
    """
    #{bottles(n)} of beer on the wall, #{bottles(n)} of beer.
    Take #{if n === 1, do: "it", else: "one"} down and pass it around, #{bottles(n - 1)} of beer on the wall.
    """
  end

  @spec lyrics() :: String.t()
  def lyrics(), do: lyrics(99..0)

  @doc """
  Get the entire beer song for a given range of numbers of bottles.
  """
  @spec lyrics(Range.t()) :: String.t()
  def lyrics(range) do
    Enum.map_join(range, "\n", &verse(&1))
  end
end
