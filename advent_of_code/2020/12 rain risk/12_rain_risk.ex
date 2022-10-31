defmodule RainRisk do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(fn line ->
      action =
        case String.at(line, 0) do
          "N" -> :north
          "S" -> :south
          "E" -> :east
          "W" -> :west
          "L" -> :left
          "R" -> :right
          "F" -> :forward
        end

      {value, _} = Integer.parse(String.slice(line, 1..-1))
      {action, value}
    end)
  end

  def manhattan({x, y}) do
    abs(x) + abs(y)
  end

  def forward_1({x, y}, value, direction) do
    case direction do
      :north -> {x, y + value}
      :south -> {x, y - value}
      :east -> {x + value, y}
      :west -> {x - value, y}
    end
  end

  def new_direction(current_dir, :left, degrees) do
    new_direction(current_dir, :right, 360 - degrees)
  end

  def new_direction(current_dir, :right, degrees) do
    directions_to_index = %{north: 0, east: 1, south: 2, west: 3}
    index_to_directions = %{0 => :north, 1 => :east, 2 => :south, 3 => :west}

    current_index = directions_to_index[current_dir]
    new_index = Integer.mod(current_index + div(degrees, 90), 4)
    index_to_directions[new_index]
  end

  def run_1({x, y}, _direction, []) do
    {x, y}
  end

  def run_1({x, y}, direction, [{action, value} | rest]) do
    case {action, value} do
      {:north, v} -> run_1({x, y + v}, direction, rest)
      {:south, v} -> run_1({x, y - v}, direction, rest)
      {:east, v} -> run_1({x + v, y}, direction, rest)
      {:west, v} -> run_1({x - v, y}, direction, rest)
      {:left, v} -> run_1({x, y}, new_direction(direction, :left, v), rest)
      {:right, v} -> run_1({x, y}, new_direction(direction, :right, v), rest)
      {:forward, v} -> run_1(forward_1({x, y}, v, direction), direction, rest)
    end
  end

  def new_waypoint(waypoint, :left, degrees) do
    new_waypoint(waypoint, :right, 360 - degrees)
  end

  def new_waypoint({x, y}, :right, degrees) do
    case degrees do
      90 -> {y, -x}
      180 -> {-x, -y}
      270 -> {-y, x}
    end
  end

  def forward_2({pos_x, pos_y}, {way_x, way_y}, value) do
    {pos_x + value * way_x, pos_y + value * way_y}
  end

  def run_2(position, _waypoint, []) do
    position
  end

  def run_2(position, {way_x, way_y} = waypoint, [{action, value} | rest]) do
    case {action, value} do
      {:north, v} -> run_2(position, {way_x, way_y + v}, rest)
      {:south, v} -> run_2(position, {way_x, way_y - v}, rest)
      {:east, v} -> run_2(position, {way_x + v, way_y}, rest)
      {:west, v} -> run_2(position, {way_x - v, way_y}, rest)
      {:left, v} -> run_2(position, new_waypoint(waypoint, :left, v), rest)
      {:right, v} -> run_2(position, new_waypoint(waypoint, :right, v), rest)
      {:forward, v} -> run_2(forward_2(position, waypoint, v), waypoint, rest)
    end
  end
end

instructions = RainRisk.read_input("12_rain_risk.input")

final_position_1 = RainRisk.run_1({0, 0}, :east, instructions)
distance_1 = RainRisk.manhattan(final_position_1)
IO.puts("Part 1: #{distance_1}")

final_position_2 = RainRisk.run_2({0, 0}, {10, 1}, instructions)
distance_2 = RainRisk.manhattan(final_position_2)
IO.puts("Part 2: #{distance_2}")
