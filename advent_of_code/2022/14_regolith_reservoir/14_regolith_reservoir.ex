defmodule RegolithReservoir do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_path/1)
  end

  def parse_path(line) do
    line
    |> String.split(" -> ")
    |> Enum.map(&parse_point/1)
  end

  def parse_point(str) do
    str
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  def limits(paths) do
    [[[500, 0]] | paths]
    |> Enum.map(fn path ->
      x = Enum.map(path, fn [x, _y] -> x end)
      y = Enum.map(path, fn [_x, y] -> y end)
      [Enum.min(x), Enum.max(x), Enum.min(y), Enum.max(y)]
    end)
    |> Enum.reduce(
      [10000, 0, 10000, 0],
      fn [min_x_path, max_x_path, min_y_path, max_y_path],
         [min_x_global, max_x_global, min_y_global, max_y_global] ->
        [
          Enum.min([min_x_path, min_x_global]),
          Enum.max([max_x_path, max_x_global]),
          Enum.min([min_y_path, min_y_global]),
          Enum.max([max_y_path, max_y_global])
        ]
      end
    )
  end

  def print(cave, [min_x, max_x, min_y, max_y]) do
    Enum.each(min_y..max_y, fn y ->
      min_x..max_x
      |> Enum.map(&Map.get(cave[y], &1))
      |> IO.puts()
    end)

    IO.puts("")
    cave
  end

  def add(cave, [x, y], something) do
    new_row =
      case something do
        :water_source -> Map.put(cave[y], x, ?+)
        :rock -> Map.put(cave[y], x, ?#)
        :sand -> Map.put(cave[y], x, ?o)
      end

    Map.put(cave, y, new_row)
  end

  def add_path(cave, [current | [next | rest]], limits) do
    updated_cave = add(cave, current, :rock)

    [current_x, current_y] = current
    [next_x, next_y] = next

    next_in_path =
      cond do
        next_x == current_x ->
          if next_y > current_y, do: [current_x, current_y + 1], else: [current_x, current_y - 1]

        next_y == current_y ->
          if next_x > current_x, do: [current_x + 1, current_y], else: [current_x - 1, current_y]
      end

    if next_in_path == next do
      add_path(updated_cave, [next | rest], limits)
    else
      add_path(updated_cave, [next_in_path | [next | rest]], limits)
    end
  end

  def add_path(cave, [last], _limits) do
    add(cave, last, :rock)
  end

  def cave(paths, [min_x, max_x, min_y, max_y]) do
    empty_cave =
      Enum.reduce(min_y..max_y, %{}, fn y, acc ->
        Map.put(acc, y, Enum.reduce(min_x..max_x, %{}, fn x, acc -> Map.put(acc, x, ?.) end))
      end)
      |> add([500, 0], :water_source)

    Enum.reduce(paths, empty_cave, fn path, cave ->
      add_path(cave, path, [min_x, max_x, min_y, max_y])
    end)
  end

  def status([x, y], cave, [min_x, max_x, min_y, max_y]) do
    if x not in min_x..max_x or y not in min_y..max_y do
      :abyss
    else
      if Map.get(cave[y], x) == ?. do
        :free
      else
        :occupied
      end
    end
  end

  def rest_down([x, y], cave, limits) do
    case status([x, y + 1], cave, limits) do
      :free -> rest_down([x, y + 1], cave, limits)
      :occupied -> rest_left([x, y], cave, limits)
      :abyss -> nil
    end
  end

  def rest_left([x, y], cave, limits) do
    case status([x - 1, y + 1], cave, limits) do
      :free -> rest_down([x - 1, y + 1], cave, limits)
      :occupied -> rest_right([x, y], cave, limits)
      :abyss -> nil
    end
  end

  def rest_right([x, y], cave, limits) do
    case status([x + 1, y + 1], cave, limits) do
      :free -> rest_down([x + 1, y + 1], cave, limits)
      :occupied -> [x, y]
      :abyss -> nil
    end
  end

  def produce_sand(cave, limits, count) do
    case rest_down([500, 0], cave, limits) do
      nil ->
        count

      resting_point ->
        if resting_point == [500, 0] do
          count + 1
        else
          produce_sand(add(cave, resting_point, :sand), limits, count + 1)
        end
    end
  end
end

paths = RegolithReservoir.read_input("14_regolith_reservoir.input")
limits = RegolithReservoir.limits(paths)

cave = RegolithReservoir.cave(paths, limits)
part_1 = RegolithReservoir.produce_sand(cave, limits, 0)
IO.puts("Part 1: #{part_1}")

[min_x, max_x, _min_y, max_y] = limits
floor_path = [[min_x - 10000, max_y + 2], [max_x + 10000, max_y + 2]]
new_paths = [floor_path | paths]
new_limits = RegolithReservoir.limits(new_paths)
cave = RegolithReservoir.cave(new_paths, new_limits)
part_2 = RegolithReservoir.produce_sand(cave, new_limits, 0)
IO.puts("Part 2: #{part_2}")
