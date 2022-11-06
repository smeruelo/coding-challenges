defmodule ConwayCubes do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    lines =
      data
      |> String.split("\n")
      |> Enum.map(&to_charlist/1)

    parse_lines(lines, 0, [])
  end

  def parse_lines([], _y, active_cubes_2d) do
    active_cubes_2d
  end

  def parse_lines([line | rest], y, active_cubes_2d) do
    updated_active_cubes =
      0..(length(line) - 1)
      |> Enum.zip(line)
      |> Enum.reduce(active_cubes_2d, fn {x, cube}, acc ->
        if cube == ?# do
          [{y, x} | acc]
        else
          acc
        end
      end)

    parse_lines(rest, y + 1, updated_active_cubes)
  end

  def initial_cubes(active_cubes_2d, dimensions) do
    active_cubes_2d
    |> Enum.reduce(MapSet.new(), fn {y, x}, acc ->
      case dimensions do
        :D3 -> MapSet.put(acc, {0, y, x})
        :D4 -> MapSet.put(acc, {0, 0, y, x})
      end
    end)
  end

  def combos({z, y, x}) do
    Enum.map(combos(z), fn z ->
      Enum.map(combos(y), fn y ->
        Enum.map(combos(x), fn x ->
          {z, y, x}
        end)
      end)
    end)
  end

  def combos({w, z, y, x}) do
    Enum.map(combos(w), fn w ->
      Enum.map(combos(z), fn z ->
        Enum.map(combos(y), fn y ->
          Enum.map(combos(x), fn x ->
            {w, z, y, x}
          end)
        end)
      end)
    end)
  end

  def combos(value) do
    [value - 1, value, value + 1]
  end

  def neighbors_with(cube) do
    combos(cube)
    |> List.flatten()
    |> MapSet.new()
  end

  def neighbors_without(cube) do
    cube
    |> neighbors_with()
    |> MapSet.delete(cube)
  end

  def active?(cube, active_cubes) do
    MapSet.member?(active_cubes, cube)
  end

  def count_active_neighbors(cube, active_cubes) do
    cube
    |> neighbors_without()
    |> Enum.reduce(0, fn c, acc ->
      if active?(c, active_cubes) do
        acc + 1
      else
        acc
      end
    end)
  end

  def active_next_cycle?(cube, active_cubes) do
    an = count_active_neighbors(cube, active_cubes)

    case active?(cube, active_cubes) do
      true -> an == 2 or an == 3
      false -> an == 3
    end
  end

  def cycle(active_cubes) do
    active_cubes
    |> Enum.reduce(MapSet.new(), fn cube, acc ->
      MapSet.union(acc, neighbors_with(cube))
    end)
    |> Enum.reduce(MapSet.new(), fn cube, acc ->
      if active_next_cycle?(cube, active_cubes) do
        MapSet.put(acc, cube)
      else
        acc
      end
    end)
  end

  def run_cycles(n, n, active_cubes) do
    active_cubes
  end

  def run_cycles(i, n, active_cubes) do
    run_cycles(i + 1, n, cycle(active_cubes))
  end
end

active_cubes_2d = ConwayCubes.read_input("17_conway_cubes.input")
active_cubes_3d = ConwayCubes.initial_cubes(active_cubes_2d, :D3)
active_cubes_4d = ConwayCubes.initial_cubes(active_cubes_2d, :D4)

part_1 = MapSet.size(ConwayCubes.run_cycles(0, 6, active_cubes_3d))
IO.puts("Part 1: #{part_1}")

part_2 = MapSet.size(ConwayCubes.run_cycles(0, 6, active_cubes_4d))
IO.puts("Part 2: #{part_2}")
