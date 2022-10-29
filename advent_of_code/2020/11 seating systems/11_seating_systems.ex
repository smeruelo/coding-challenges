defmodule SeatingSystems do
  @rows 95
  @columns 99
  # @rows 10
  # @columns 10

  @directions [:up_left, :up, :up_right, :left, :right, :down_left, :down, :down_right]

  def read_input(filename) do
    {:ok, data} = File.read(filename)
    layout_str = data |> String.replace("\n", "")

    Enum.reduce(0..(@rows * @columns - 1), %{}, fn i, acc ->
      Map.put(acc, i, String.at(layout_str, i))
    end)
  end

  def adjacents(seat) do
    up = [seat - @columns]
    down = [seat + @columns]

    left =
      if rem(seat, @columns) != 0 do
        [seat - @columns - 1, seat - 1, seat + @columns - 1]
      else
        []
      end

    right =
      if rem(seat, @columns) != @columns - 1 do
        [seat - @columns + 1, seat + 1, seat + @columns + 1]
      else
        []
      end

    Enum.filter(up ++ down ++ left ++ right, fn x -> x >= 0 and x < @rows * @columns end)
  end

  def next_in_dir(seat, direction) do
    next =
      case direction do
        :up_left -> seat - @columns - 1
        :up -> seat - @columns
        :up_right -> seat - @columns + 1
        :left -> seat - 1
        :right -> seat + 1
        :down_left -> seat + @columns - 1
        :down -> seat + @columns
        :down_right -> seat + @columns + 1
      end

    if next in adjacents(seat) do
      next
    else
      nil
    end
  end

  def is_empty?(layout, seat), do: layout[seat] == "L"

  def is_occupied?(layout, seat), do: layout[seat] == "#"

  def see_occupied?(layout, seat, direction) do
    next = next_in_dir(seat, direction)

    if is_nil(next) do
      false
    else
      case layout[next] do
        "L" -> false
        "#" -> true
        "." -> see_occupied?(layout, next, direction)
      end
    end
  end

  def more_than(bool_lst, x), do: Enum.count(bool_lst, fn x -> x end) >= x

  def will_empty_1?(layout, seat) do
    is_occupied?(layout, seat) and
      more_than(Enum.map(adjacents(seat), fn x -> is_occupied?(layout, x) end), 4)
  end

  def will_occupy_1?(layout, seat) do
    is_empty?(layout, seat) and
      not Enum.any?(adjacents(seat), fn x -> is_occupied?(layout, x) end)
  end

  def will_empty_2?(layout, seat) do
    is_occupied?(layout, seat) and
      more_than(Enum.map(@directions, fn dir -> see_occupied?(layout, seat, dir) end), 5)
  end

  def will_occupy_2?(layout, seat) do
    is_empty?(layout, seat) and
      not Enum.any?(@directions, fn dir -> see_occupied?(layout, seat, dir) end)
  end

  def count_occupied(layout) do
    Map.values(layout)
    |> Enum.reduce(0, fn x, acc ->
      if x == "#" do
        acc + 1
      else
        acc
      end
    end)
  end

  def do_round(layout, {will_empty?, will_occupy?}) do
    Enum.reduce(
      0..(@rows * @columns - 1),
      {%{}, 0},
      fn i, {new_layout, changes} ->
        case layout[i] do
          "L" ->
            if will_occupy?.(layout, i) do
              {Map.put(new_layout, i, "#"), changes + 1}
            else
              {Map.put(new_layout, i, "L"), changes}
            end

          "#" ->
            if will_empty?.(layout, i) do
              {Map.put(new_layout, i, "L"), changes + 1}
            else
              {Map.put(new_layout, i, "#"), changes}
            end

          "." ->
            {Map.put(new_layout, i, "."), changes}
        end
      end
    )
  end

  def until_stabilized(j, {layout, changes}, rules) do
    # IO.puts("Round #{j}, changes #{changes}")

    if changes == 0 do
      count_occupied(layout)
    else
      until_stabilized(j + 1, do_round(layout, rules), rules)
    end
  end

  def run(part, layout) do
    case part do
      1 -> until_stabilized(0, {layout, -1}, {&will_empty_1?/2, &will_occupy_1?/2})
      2 -> until_stabilized(0, {layout, -1}, {&will_empty_2?/2, &will_occupy_2?/2})
    end
  end

  def print(layout) do
    lines =
      Enum.map(
        Enum.chunk_every(0..(@rows * @columns - 1), @columns),
        fn chunk ->
          Enum.join(Enum.map(chunk, fn i -> layout[i] end))
        end
      )

    Enum.map(lines, &IO.puts/1)
    layout
  end
end

layout = SeatingSystems.read_input("11_seating_systems.input")

count_1 = SeatingSystems.run(1, layout)
IO.puts("Part 1: #{count_1}")

count_2 = SeatingSystems.run(2, layout)
IO.puts("Part 2: #{count_2}")
