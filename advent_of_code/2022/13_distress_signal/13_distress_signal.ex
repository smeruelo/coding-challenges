defmodule DistressSignal do
  def read_input_1(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.map(&parse_pair/1)
  end

  def read_input_2(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.filter(fn line -> line != "" end)
    |> Enum.map(fn line ->
      {_, parsed_list} = parse_list(to_charlist(line))
      parsed_list
    end)
  end

  def parse_pair(block) do
    String.split(block, "\n")
    |> Enum.map(fn line ->
      {_, parsed_list} = parse_list(to_charlist(line))
      parsed_list
    end)
  end

  def parse_num([current | rest], num) do
    if current in ?0..?9 do
      parse_num(rest, num * 10 + current - 48)
    else
      {[current | rest], num}
    end
  end

  def parse_list([?[ | rest]), do: parse_list(rest, [])

  def parse_list([], parsed), do: {[], parsed}

  def parse_list([?[ | rest], parsed) do
    {new_rest, parsed_list} = parse_list(rest, [])
    parse_list(new_rest, [parsed_list | parsed])
  end

  def parse_list([?] | rest], parsed), do: {rest, Enum.reverse(parsed)}

  def parse_list([?, | rest], parsed), do: parse_list(rest, parsed)

  def parse_list([num | rest], parsed) do
    {new_rest, num} = parse_num(rest, num - 48)
    parse_list(new_rest, [num | parsed])
  end

  def ordered(int_a, int_b) when is_integer(int_a) and is_integer(int_b) do
    cond do
      int_a < int_b -> {:halt, true}
      int_a == int_b -> {:continue}
      int_a > int_b -> {:halt, false}
    end
  end

  def ordered([], []), do: {:continue}

  def ordered([], list_b) when is_list(list_b), do: {:halt, true}

  def ordered([_head_a | _tail_a], []), do: {:halt, false}

  def ordered([head_a | tail_a], [head_b | tail_b]) do
    case ordered(head_a, head_b) do
      {:continue} -> ordered(tail_a, tail_b)
      {:halt, true} -> {:halt, true}
      {:halt, false} -> {:halt, false}
    end
  end

  def ordered(int_a, list_b) when is_integer(int_a) and is_list(list_b) do
    ordered([int_a], list_b)
  end

  def ordered(list_a, int_b) when is_integer(int_b) and is_list(list_a) do
    ordered(list_a, [int_b])
  end

  def sum_ordered(pair_list) do
    pair_list
    |> Enum.with_index()
    |> Enum.reduce(0, fn {[list_a, list_b], index}, acc ->
      case ordered(list_a, list_b) do
        {:halt, true} -> acc + index + 1
        {:halt, false} -> acc
      end
    end)
  end

  def order(lists) do
    Enum.sort(lists, fn list_1, list_2 ->
      {:halt, result} = ordered(list_1, list_2)
      result
    end)
  end

  def part_2(lists) do
    dividers = [[[2]], [[6]]]

    (dividers ++ lists)
    |> order()
    |> Enum.with_index()
    |> Enum.reduce(1, fn {list, index}, acc ->
      if list in dividers do
        acc * (index + 1)
      else
        acc
      end
    end)
  end
end

part_1 =
  DistressSignal.read_input_1("13_distress_signal.input")
  |> DistressSignal.sum_ordered()

IO.puts("Part 1: #{part_1}")

part_2 =
  DistressSignal.read_input_2("13_distress_signal.input")
  |> DistressSignal.part_2()

IO.puts("Part 2: #{part_2}")
