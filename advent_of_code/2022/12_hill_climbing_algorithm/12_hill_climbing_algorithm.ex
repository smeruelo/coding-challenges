defmodule HillClimbingAlgorithm do
  @max_row 40
  @max_col 135

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&to_charlist/1)
    |> Stream.with_index(0)
    |> Enum.reduce(%{}, fn {row, index}, acc ->
      Map.put(acc, index, row_to_dict(row))
    end)
  end

  def row_to_dict(row) do
    0..@max_col |> Stream.zip(row) |> Enum.into(%{})
  end

  def height({row, col}, area) do
    case Map.get(area[row], col) do
      ?S -> ?a
      ?E -> ?z
      other -> other
    end
  end

  def feasible_move?({row_from, col_from}, {row_to, col_to}, area) do
    height({row_to, col_to}, area) - height({row_from, col_from}, area) <= 1
  end

  def neighbors({row, col} = current, area) do
    [{row - 1, col}, {row, col - 1}, {row, col + 1}, {row + 1, col}]
    |> Enum.filter(fn {r, c} -> r >= 0 and r <= @max_row and c >= 0 and c <= @max_col end)
    |> Enum.filter(&feasible_move?(current, &1, area))
  end

  def is_target?({row, col}, area), do: Map.get(area[row], col) == ?E

  def sort(to_explore) do
    Enum.sort(to_explore, fn {distance_1, _node_1}, {distance_2, _node_2} ->
      distance_1 < distance_2
    end)
  end

  def dijkstra([], _visited, _area), do: nil

  def dijkstra(to_explore, visited, area) do
    {distance, {row, col}} = hd(to_explore)

    if is_target?({row, col}, area) do
      distance
    else
      {to_explore, visited} =
        neighbors({row, col}, area)
        |> Enum.filter(fn node -> node not in visited end)
        |> Enum.reduce(
          {tl(to_explore), visited},
          fn node, {acc_to_explore, acc_visited} ->
            {
              [{distance + 1, node} | acc_to_explore],
              MapSet.put(acc_visited, node)
            }
          end
        )

      dijkstra(sort(to_explore), visited, area)
    end
  end

  def shortest_path_length(source, area) do
    dijkstra([{0, source}], MapSet.new([source]), area)
  end

  def find_shortest(41, _col, shortest_so_far, _area) do
    shortest_so_far
  end

  def find_shortest(row, @max_col, shortest_so_far, area) do
    find_shortest(row + 1, 0, shortest_so_far, area)
  end

  def find_shortest(row, col, shortest_so_far, area) do
    if height({row, col}, area) == ?a do
      case shortest_path_length({row, col}, area) do
        nil -> find_shortest(row, col + 1, shortest_so_far, area)
        length -> find_shortest(row, col + 1, min(shortest_so_far, length), area)
      end
    else
      find_shortest(row, col + 1, shortest_so_far, area)
    end
  end

  def find_shortest(area) do
    find_shortest(0, 0, @max_col * @max_row, area)
  end
end

area = HillClimbingAlgorithm.read_input("12_hill_climbing_algorithm.input")

part_1 = HillClimbingAlgorithm.shortest_path_length({20, 0}, area)
IO.puts("Part 1: #{part_1}")

part_2 = HillClimbingAlgorithm.find_shortest(area)
IO.puts("Part 2: #{part_2}")
