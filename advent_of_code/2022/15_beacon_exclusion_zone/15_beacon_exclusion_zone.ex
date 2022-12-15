defmodule BeaconExclusionZone do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.reduce(%{}, fn line, sensors ->
      [sx, sy, bx, by] = parse_sensor(line)
      Map.put(sensors, {sx, sy}, {bx, by})
    end)
    |> Map.to_list()
  end

  def parse_sensor(line) do
    [_, sx, _, sy, _, bx, _, by] = String.split(line, ["=", ",", ":"])
    [sx, sy, bx, by] |> Enum.map(&String.to_integer/1)
  end

  def limits(sensors) do
    sensors
    |> Enum.reduce([0, 0, 0, 0], fn {{sx, sy}, {bx, by}}, [min_x, max_x, min_y, max_y] ->
      [
        Enum.min([min_x, sx, bx]),
        Enum.max([max_x, sx, bx]),
        Enum.min([min_y, sy, by]),
        Enum.max([max_y, sy, by])
      ]
    end)
  end

  def print(area, [min_x, max_x, min_y, max_y]) do
    Enum.each(min_y..max_y, fn y ->
      min_x..max_x
      |> Enum.map(&Map.get(area[y], &1))
      |> IO.puts()
    end)

    IO.puts("")
    area
  end

  def init_area([min_x, max_x, min_y, max_y], sensors) do
    empty_area =
      Enum.reduce(min_y..max_y, %{}, fn y, acc ->
        Map.put(acc, y, Enum.reduce(min_x..max_x, %{}, fn x, acc -> Map.put(acc, x, ?.) end))
      end)

    Enum.reduce(sensors, empty_area, fn {sensor_pos, beacon_pos}, area ->
      area
      |> mark_position(sensor_pos, :sensor)
      |> mark_position(beacon_pos, :beacon)
    end)
  end

  def mark_position(area, {x, y}, symbol) do
    new_row =
      case symbol do
        :sensor -> Map.put(area[y], x, ?S)
        :beacon -> Map.put(area[y], x, ?B)
        :exclusion -> Map.put(area[y], x, ?#)
      end

    Map.put(area, y, new_row)
  end

  def manhattan_distance({x1, y1}, {x2, y2}), do: abs(x1 - x2) + abs(y1 - y2)

  def exclusion_zone({x, y} = sensor, beacon) do
    distance = manhattan_distance(sensor, beacon)

    {
      (x - distance)..(distance + x),
      (y - distance)..(distance + y)
    }
  end

  def row_in_exclusion_zone(row, {min_x..max_x, min_y..max_y}) do
    if row in min_y..max_y do
      medium_x = div(min_x + max_x, 2)
      medium_y = div(min_y + max_y, 2)
      offset = if row <= medium_y, do: row - min_y, else: max_y - row

      (medium_x - offset)..(medium_x + offset)
    else
      []
    end
  end

  def is_beacon?(_position, []), do: false

  def is_beacon?(position, [{_sensor, beacon} | rest]) do
    if position == beacon do
      true
    else
      is_beacon?(position, rest)
    end
  end

  def in_exclusion_zone?({x, y}, sensor, beacon) do
    x in row_in_exclusion_zone(y, exclusion_zone(sensor, beacon))
  end

  def in_any_exclusion_zone?(_position, []), do: false

  def in_any_exclusion_zone?(position, [{sensor, beacon} | rest]) do
    if in_exclusion_zone?(position, sensor, beacon) do
      true
    else
      in_any_exclusion_zone?(position, rest)
    end
  end

  def count_free_positions(row, sensors, [limit_min_x, limit_max_x, _, _]) do
    # (limit_min_x - 1 - 40)..(limit_max_x + 1 + 40)
    (limit_min_x - 1 - 6_000_000)..(limit_max_x + 1 + 6_000_000)
    |> Enum.reduce(0, fn x, acc ->
      if !is_beacon?({x, row}, sensors) and in_any_exclusion_zone?({x, row}, sensors) do
        acc + 1
      else
        acc
      end
    end)
  end

  def perimeter({sensor, beacon}) do
    {min_x..max_x, min_y..max_y} = exclusion_zone(sensor, beacon)
    medium_x = div(min_x + max_x, 2)

    Enum.reduce(min_y..max_y, [{medium_x, min_y - 1}, {medium_x, max_y + 1}], fn row, acc ->
      left..right = row_in_exclusion_zone(row, {min_x..max_x, min_y..max_y})
      [{left - 1, row} | [{right + 1, row} | acc]]
    end)
    |> Enum.filter(fn {x, y} -> x >= 0 and x <= 4_000_000 and y >= 0 and y <= 4_000_000 end)

    # |> Enum.filter(fn {x, y} -> x >= 0 and x <= 20 and y >= 0 and y <= 20 end)
  end

  def find_distress_beacon([{sensor, beacon} | rest], sensors) do
    perimeter({sensor, beacon})
    |> Enum.find(fn position -> !in_any_exclusion_zone?(position, sensors) end)
    |> case do
      nil -> find_distress_beacon(rest, sensors)
      position -> position
    end
  end
end

sensors = BeaconExclusionZone.read_input("15_beacon_exclusion_zone.input")
limits = BeaconExclusionZone.limits(sensors)

# part_1 = BeaconExclusionZone.count_free_positions(10, sensors, limits)
part_1 = BeaconExclusionZone.count_free_positions(2_000_000, sensors, limits)
IO.puts("Part 1: #{part_1}")

{x, y} = BeaconExclusionZone.find_distress_beacon(sensors, sensors)
part_2 = x * 4_000_000 + y
IO.puts("Part 2: #{part_2}")
