# https://exercism.io/my/solutions/6422bca0241c43eea6e1f640d13249bb

defmodule ResistorColor do
  @moduledoc false

  @colors [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
  ]
  @codes @colors |> Enum.with_index() |> Enum.into(%{})

  @spec colors() :: list(String.t())
  def colors, do: @colors

  @spec code(String.t()) :: integer()
  def code(color) do
    Map.get(@codes, color)
  end
end
