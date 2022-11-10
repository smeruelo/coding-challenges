defmodule JurassicJigsaw do
  def parse_tile(block) do
    borders = fn tile ->
      top = List.first(tile)
      bottom = List.last(tile)
      left = Enum.map(tile, &List.first/1)
      right = Enum.map(tile, &List.last/1)
      [top, right, bottom, left]
    end

    [header | rest] = String.split(block, "\n")
    [_, tile_num, _] = String.split(header, [" ", ":"])

    tile_borders =
      rest
      |> Enum.map(&to_charlist/1)
      |> borders.()

    {String.to_integer(tile_num), tile_borders}
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.map(&parse_tile/1)
    |> Enum.reduce(%{}, fn {tile_num, tile}, acc ->
      Map.put(acc, tile_num, tile)
    end)
  end

  def all_other_borders(tile_num, tiles) do
    normal = Map.values(Map.delete(tiles, tile_num))

    flipped =
      Enum.map(normal, fn tile ->
        Enum.map(tile, fn border -> Enum.reverse(border) end)
      end)

    Enum.reduce(normal ++ flipped, [], fn tile, acc -> tile ++ acc end)
  end

  def is_corner?({num, tile}, tiles) do
    all_borders = all_other_borders(num, tiles)

    tile
    |> Enum.map(fn border -> border not in all_borders end)
    |> Enum.count(& &1) == 2
  end

  def corners(tiles) do
    Enum.filter(Map.to_list(tiles), fn {num, tile} ->
      JurassicJigsaw.is_corner?({num, tile}, tiles)
    end)
    |> Enum.map(&elem(&1, 0))
    |> Enum.product()
  end
end

tiles = JurassicJigsaw.read_input("20_jurassic_jigsaw.input")

part_1 = JurassicJigsaw.corners(tiles)
IO.puts("Part 1: #{part_1}")
