defmodule BoilingBoulders do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_cube/1)
    |> MapSet.new()
  end

  def parse_cube(line) do
    line
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
    |> List.to_tuple()
  end

  def adjacents({x, y, z} = cube) when is_tuple(cube) do
    [
      {x - 1, y, z},
      {x + 1, y, z},
      {x, y - 1, z},
      {x, y + 1, z},
      {x, y, z - 1},
      {x, y, z + 1}
    ]
  end

  def adjacents(group) do
    Enum.reduce(group, MapSet.new(), fn c, acc ->
      adjacents(c)
      |> Enum.filter(fn adj -> adj not in group end)
      |> MapSet.new()
      |> MapSet.union(acc)
    end)
  end

  def count_touching_sides(cubes) do
    cubes
    |> Enum.map(fn cube -> Enum.count(adjacents(cube), fn adj -> adj in cubes end) end)
    |> Enum.sum()
  end

  def max_positions(cubes) do
    max_x = Enum.max(Enum.map(cubes, fn {x, _, _} -> x end))
    max_y = Enum.max(Enum.map(cubes, fn {_, y, _} -> y end))
    max_z = Enum.max(Enum.map(cubes, fn {_, _, z} -> z end))
    {max_x, max_y, max_z}
  end

  def not_in_droplet(cubes) do
    {max_x, max_y, max_z} = max_positions(cubes)
    possible_cubes = for x <- 1..max_x, y <- 1..max_y, z <- 1..max_z, do: {x, y, z}
    Enum.filter(possible_cubes, fn c -> c not in cubes end)
  end

  def are_adjacent?(cube_1, cube_2), do: cube_2 in adjacents(cube_1)

  def add_to_adjacents_group(groups, cube),
    do: add_to_adjacents_group(groups, cube, MapSet.new([cube]), [])

  def add_to_adjacents_group([], _cube, adjacent, not_adjacents), do: [adjacent | not_adjacents]

  def add_to_adjacents_group([group | rest], cube, adjacent, not_adjacents) do
    if Enum.any?(group, fn c -> are_adjacent?(c, cube) end) do
      add_to_adjacents_group(rest, cube, MapSet.union(group, adjacent), not_adjacents)
    else
      add_to_adjacents_group(rest, cube, adjacent, [group | not_adjacents])
    end
  end

  def group_adjacents(cubes) do
    Enum.reduce(cubes, [], fn cube, acc -> add_to_adjacents_group(acc, cube) end)
  end

  def trapped?(group, cubes) do
    Enum.all?(adjacents(group), fn adj -> adj in cubes end)
  end

  def surface(cubes), do: 6 * MapSet.size(cubes) - count_touching_sides(cubes)

  def part_2(cubes) do
    trapped_sides =
      cubes
      |> not_in_droplet()
      |> group_adjacents()
      |> Enum.reduce(0, fn group, acc ->
        if trapped?(group, cubes) do
          acc + surface(group)
        else
          acc
        end
      end)

    surface(cubes) - trapped_sides
  end
end

cubes = BoilingBoulders.read_input("18_boiling_boulders.input")

part_1 = BoilingBoulders.surface(cubes)
IO.puts("Part 1: #{part_1}")

part_2 = BoilingBoulders.part_2(cubes)
IO.puts("Part 2: #{part_2}")
