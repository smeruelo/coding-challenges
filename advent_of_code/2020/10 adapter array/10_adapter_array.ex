defmodule AdapterArray do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.sort()
  end

  def count_differences(joltages, previous, count_1, count_3) do
    case joltages do
      [] ->
        count_1 * count_3

      [head | tail] ->
        case head - previous do
          1 -> count_differences(tail, head, count_1 + 1, count_3)
          3 -> count_differences(tail, head, count_1, count_3 + 1)
        end
    end
  end

  # array of booleans marking joltages as removable or not
  # (i.e. if they might be not included in the arrangement)
  def mark_removables(joltages, previous, removables) do
    case joltages do
      [_] ->
        [false | removables] |> Enum.reverse()

      [head | [next | _] = tail] ->
        case {head - previous, next - head} do
          {1, 1} -> mark_removables(tail, head, [true | removables])
          _ -> mark_removables(tail, head, [false | removables])
        end
    end
  end

  def count_arrangements(removables) do
    removables
    |> Enum.reduce({1, 0}, fn removable, {num_arrangements, adjacents} ->
      case {removable, adjacents} do
        {false, adj} when adj == 0 ->
          {num_arrangements, 0}

        {false, adj} when adj > 0 ->
          case adj do
            # 3 adjacent removable joltages only produce 7 combos,
            # because the 8th (= removing the 3 of them) is not admisible
            3 -> {7 * num_arrangements, 0}
            2 -> {4 * num_arrangements, 0}
            1 -> {2 * num_arrangements, 0}
          end

        {true, adj} ->
          {num_arrangements, adj + 1}
      end
    end)
    |> elem(0)
  end
end

joltages = AdapterArray.read_input("10_adapter_array.input")

result_1 = AdapterArray.count_differences(joltages, 0, 0, 1)
IO.puts("Part 1: #{result_1}")

result_2 =
  joltages
  |> AdapterArray.mark_removables(0, [])
  |> AdapterArray.count_arrangements()

IO.puts("Part 2: #{result_2}")
