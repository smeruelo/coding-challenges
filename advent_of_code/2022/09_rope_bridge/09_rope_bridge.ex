defmodule RopeBridge do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_move/1)
  end

  def parse_move(line) do
    [direction, steps] = String.split(line, " ")
    {direction, String.to_integer(steps)}
  end

  def touch?({hx, hy}, {tx, ty}) do
    abs(hx - tx) <= 1 and abs(hy - ty) <= 1
  end

  def follow_2({hx, hy}, {tx, ty}) do
    cond do
      hy - ty == 2 -> {tx + adjust_step(hx, tx), ty + 1}
      hy - ty == -2 -> {tx + adjust_step(hx, tx), ty - 1}
      hx - tx == 2 -> {tx + 1, ty + adjust_step(hy, ty)}
      hx - tx == -2 -> {tx - 1, ty + adjust_step(hy, ty)}
    end
  end

  # unnecessary (but harmless) in part 1
  def adjust_step(h, t) do
    cond do
      abs(h - t) < 2 -> h - t
      h - t == 2 -> 1
      h - t == -2 -> -1
    end
  end

  def move_head({hx, hy}, direction) do
    case direction do
      "U" -> {hx, hy + 1}
      "L" -> {hx - 1, hy}
      "D" -> {hx, hy - 1}
      "R" -> {hx + 1, hy}
    end
  end

  def simulate_1([], _head, _tail, visited) do
    visited
  end

  def simulate_1([{_direction, 0} | rest], head, tail, visited) do
    simulate_1(rest, head, tail, visited)
  end

  def simulate_1([{direction, steps} | rest], head, tail, visited) do
    moved_head = move_head(head, direction)
    moved_tail = if touch?(moved_head, tail), do: tail, else: follow_2(moved_head, tail)

    simulate_1(
      [{direction, steps - 1} | rest],
      moved_head,
      moved_tail,
      MapSet.put(visited, moved_tail)
    )
  end

  def simulate_1(moves) do
    simulate_1(moves, {0, 0}, {0, 0}, MapSet.new([{0, 0}]))
  end

  def simulate_2([], _head, _tails, visited) do
    visited
  end

  def simulate_2([{_direction, 0} | rest], head, tails, visited) do
    simulate_2(rest, head, tails, visited)
  end

  def simulate_2([{direction, steps} | rest], head, tails, visited) do
    moved_head = move_head(head, direction)

    moved_tails =
      Enum.reduce(1..9, %{0 => moved_head}, fn i, moved_tails ->
        if touch?(moved_tails[i - 1], tails[i]) do
          Map.put(moved_tails, i, tails[i])
        else
          Map.put(moved_tails, i, follow_2(moved_tails[i - 1], tails[i]))
        end
      end)

    simulate_2(
      [{direction, steps - 1} | rest],
      moved_head,
      moved_tails,
      MapSet.put(visited, moved_tails[9])
    )
  end

  def simulate_2(moves) do
    tails = %{
      1 => {0, 0},
      2 => {0, 0},
      3 => {0, 0},
      4 => {0, 0},
      5 => {0, 0},
      6 => {0, 0},
      7 => {0, 0},
      8 => {0, 0},
      9 => {0, 0}
    }

    simulate_2(moves, {0, 0}, tails, MapSet.new([{0, 0}]))
  end
end

moves = RopeBridge.read_input("09_rope_bridge.input")

visited = RopeBridge.simulate_1(moves)
part_1 = MapSet.size(visited)
IO.puts("Part 1: #{part_1}")

visited = RopeBridge.simulate_2(moves)
part_2 = MapSet.size(visited)
IO.puts("Part 2: #{part_2}")
