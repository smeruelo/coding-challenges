defmodule TreetopTreeHouse do
  @size 99

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    lines =
      data
      |> String.split("\n")
      |> Enum.map(fn line ->
        to_charlist(line)
        |> Enum.map(fn c -> c - 48 end)
      end)

    [0..(length(lines) - 1), lines]
    |> Enum.zip_reduce(%{}, fn [row, line], acc ->
      Map.put(acc, row, collect_row(line))
    end)
  end

  def collect_row(line) do
    [0..(length(line) - 1), line]
    |> Enum.zip_reduce(%{}, fn [col, tree], acc ->
      Map.put(acc, col, tree)
    end)
  end

  def left(_row, 0, _trees), do: []

  def left(row, col, trees) do
    Enum.map((col - 1)..0, fn i -> Map.get(trees[row], i) end)
  end

  def right(_row, col, _trees) when col >= @size - 1, do: []

  def right(row, col, trees) do
    Enum.map((col + 1)..(@size - 1), fn i -> Map.get(trees[row], i) end)
  end

  def up(0, _col, _trees), do: []

  def up(row, col, trees) do
    Enum.map((row - 1)..0, fn i -> Map.get(trees[i], col) end)
  end

  def down(row, _col, _trees) when row >= @size - 1, do: []

  def down(row, col, trees) do
    Enum.map((row + 1)..(@size - 1), fn i -> Map.get(trees[i], col) end)
  end

  def visible(tree, direction) do
    Enum.all?(direction, fn x -> x < tree end)
  end

  def count_visible(trees), do: count_visible(0, 0, trees, 0)
  def count_visible(@size, _col, _trees, count), do: count

  def count_visible(row, @size, trees, count) do
    count_visible(row + 1, 0, trees, count)
  end

  def count_visible(row, col, trees, count) do
    tree = Map.get(trees[row], col)

    directions = [
      left(row, col, trees),
      right(row, col, trees),
      up(row, col, trees),
      down(row, col, trees)
    ]

    if Enum.any?(directions, &visible(tree, &1)) do
      count_visible(row, col + 1, trees, count + 1)
    else
      count_visible(row, col + 1, trees, count)
    end
  end

  def direction_score([], _reference_tree, count), do: count

  def direction_score([tree | others], reference_tree, count) do
    if tree < reference_tree do
      direction_score(others, reference_tree, count + 1)
    else
      count + 1
    end
  end

  def score(row, col, trees) do
    [
      up(row, col, trees),
      left(row, col, trees),
      right(row, col, trees),
      down(row, col, trees)
    ]
    |> Enum.map(&direction_score(&1, Map.get(trees[row], col), 0))
    |> Enum.product()
  end

  def best_score(trees), do: best_score(0, 0, trees, 0)
  def best_score(@size, _col, _trees, best_so_far), do: best_so_far

  def best_score(row, @size, trees, best_so_far) do
    best_score(row + 1, 0, trees, best_so_far)
  end

  def best_score(row, col, trees, best_so_far) do
    tree_score = score(row, col, trees)

    if tree_score > best_so_far do
      best_score(row, col + 1, trees, tree_score)
    else
      best_score(row, col + 1, trees, best_so_far)
    end
  end
end

trees = TreetopTreeHouse.read_input("08_treetop_tree_house.input")

part_1 = TreetopTreeHouse.count_visible(trees)
IO.puts("Part 1: #{part_1}")

part_2 = TreetopTreeHouse.best_score(trees)
IO.puts("Part 2: #{part_2}")
