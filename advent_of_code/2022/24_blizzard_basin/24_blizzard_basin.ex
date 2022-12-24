defmodule BlizzardBasin do
  # @max_x 6
  # @max_y 4
  @max_x 150
  @max_y 20

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&to_charlist/1)
    |> Enum.with_index()
    |> Enum.reduce(MapSet.new(), fn {line, y}, acc_blizzards ->
      line
      |> Enum.with_index()
      |> Enum.reduce(acc_blizzards, fn {chr, x}, acc_acc_blizzards ->
        case chr do
          ?> -> MapSet.put(acc_acc_blizzards, {{y, x}, :right})
          ?< -> MapSet.put(acc_acc_blizzards, {{y, x}, :left})
          ?^ -> MapSet.put(acc_acc_blizzards, {{y, x}, :up})
          ?v -> MapSet.put(acc_acc_blizzards, {{y, x}, :down})
          _ -> acc_acc_blizzards
        end
      end)
    end)
  end

  def next({{y, x}, :right}) do
    if x + 1 > @max_x, do: {{y, 1}, :right}, else: {{y, x + 1}, :right}
  end

  def next({{y, x}, :left}) do
    if x - 1 < 1, do: {{y, @max_x}, :left}, else: {{y, x - 1}, :left}
  end

  def next({{y, x}, :up}) do
    if y - 1 < 1, do: {{@max_y, x}, :up}, else: {{y - 1, x}, :up}
  end

  def next({{y, x}, :down}) do
    if y + 1 > @max_y, do: {{1, x}, :down}, else: {{y + 1, x}, :down}
  end

  def blizzards_next_minute(blizzards) do
    Enum.reduce(blizzards, MapSet.new(), fn blizzard, acc ->
      MapSet.put(acc, next(blizzard))
    end)
  end

  def within_limits?({y, x}) do
    {y, x} in [{0, 1}, {@max_y + 1, @max_x}] or
      (y > 0 and y <= @max_y and x > 0 and x <= @max_x)
  end

  def blizzard_at_position?(pos, blizzards) do
    [{pos, :right}, {pos, :left}, {pos, :up}, {pos, :down}]
    |> Enum.any?(fn b -> b in blizzards end)
  end

  def possible_positions_from({y, x}, blizzards) do
    [{y, x}, {y, x + 1}, {y, x - 1}, {y - 1, x}, {y + 1, x}]
    |> Enum.filter(&within_limits?/1)
    |> Enum.filter(fn pos -> !blizzard_at_position?(pos, blizzards) end)
    |> MapSet.new()
  end

  def bfs(minute, positions, blizzards, goal) do
    # IO.inspect(positions)

    if goal in positions do
      {minute, blizzards}
    else
      new_positions =
        Enum.reduce(positions, MapSet.new(), fn pos, acc ->
          MapSet.union(acc, possible_positions_from(pos, blizzards))
        end)

      bfs(minute + 1, new_positions, blizzards_next_minute(blizzards), goal)
    end
  end

  def part_1(initial_blizzards) do
    {minutes, _blizzards} =
      bfs(0, MapSet.new([{0, 1}]), blizzards_next_minute(initial_blizzards), {@max_y + 1, @max_x})

    minutes
  end

  def part_2(initial_blizzards) do
    {minutes_1, blizzards_1} =
      bfs(0, MapSet.new([{0, 1}]), blizzards_next_minute(initial_blizzards), {@max_y + 1, @max_x})

    {minutes_2, blizzards_2} =
      bfs(
        minutes_1 + 1,
        MapSet.new([{@max_y + 1, @max_x}]),
        blizzards_next_minute(blizzards_1),
        {0, 1}
      )

    {minutes_3, _blizzards_3} =
      bfs(
        minutes_2 + 1,
        MapSet.new([{0, 1}]),
        blizzards_next_minute(blizzards_2),
        {@max_y + 1, @max_x}
      )

    minutes_3
  end
end

blizzards = BlizzardBasin.read_input("24_blizzard_basin.input")

part_1 = BlizzardBasin.part_1(blizzards)
IO.puts("Part 1: #{part_1}")

part_2 = BlizzardBasin.part_2(blizzards)
IO.puts("Part 2: #{part_2}")
