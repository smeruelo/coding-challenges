defmodule TobogganTrajectory do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
  end

  def next(x, step) do
    # rem(x + step, 11)
    rem(x + step, 31)
  end

  def tree(line, x) do
    case String.at(line, x) do
      "#" -> 1
      _ -> 0
    end
  end

  def head_tail(lines, step_y) do
    [hd | tl] = lines

    case {step_y, tl} do
      {1, _} -> {hd, tl}
      {2, []} -> {hd, []}
      {2, [_ | tl]} -> {hd, tl}
    end
  end

  def traverse(lines, x, step_x, step_y, count) do
    {hd, tl} = head_tail(lines, step_y)

    case tl do
      [] ->
        count + tree(hd, x)

      _ ->
        traverse(tl, next(x, step_x), step_x, step_y, count + tree(hd, x))
    end
  end
end

lines = TobogganTrajectory.read_input("03_toboggan_trajectory.input")

count1 = TobogganTrajectory.traverse(lines, 0, 3, 1, 0)
IO.puts("Part 1: #{count1}")

count2 =
  TobogganTrajectory.traverse(lines, 0, 1, 1, 0) *
    TobogganTrajectory.traverse(lines, 0, 3, 1, 0) *
    TobogganTrajectory.traverse(lines, 0, 5, 1, 0) *
    TobogganTrajectory.traverse(lines, 0, 7, 1, 0) *
    TobogganTrajectory.traverse(lines, 0, 1, 2, 0)

IO.puts("Part 2: #{count2}")
