defmodule MonkeyInTheMiddle do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.reduce(%{}, fn block, monkeys ->
      [i | info] = parse_monkey(block)
      Map.put(monkeys, i, info)
    end)
  end

  def parse_monkey(block) do
    [line_1, line_2, line_3, line_4, line_5, line_6] = String.split(block, "\n")
    monkey_num = parse_monkey_num(line_1)
    items = parse_items(line_2)
    op = parse_operation(line_3)
    test = parse_number_at_the_end(line_4)
    if_true = parse_number_at_the_end(line_5)
    if_false = parse_number_at_the_end(line_6)

    [monkey_num, items, op, test, if_true, if_false]
  end

  def parse_monkey_num(line) do
    ["Monkey", i] = String.split(String.slice(line, 0..-2), " ")
    String.to_integer(i)
  end

  def parse_items(line) do
    ["  Starting items", nums] = String.split(line, ": ")

    String.split(nums, ", ")
    |> Enum.map(&String.to_integer/1)
  end

  def parse_operation(line) do
    ["  Operation: new", operation] = String.split(line, " = ")
    [arg_1, op, arg_2] = String.split(operation, " ")

    case op do
      "+" ->
        fn old ->
          parse_arg(arg_1, old) + parse_arg(arg_2, old)
        end

      "*" ->
        fn old ->
          parse_arg(arg_1, old) * parse_arg(arg_2, old)
        end
    end
  end

  def parse_arg(arg, old) do
    case arg do
      "old" -> old
      num -> String.to_integer(num)
    end
  end

  def parse_number_at_the_end(line) do
    line
    |> String.split(" ")
    |> List.last()
    |> String.to_integer()
  end

  def simulate(rounds, func, monkeys) do
    simulate(0, func, monkeys, rounds, %{})
  end

  def simulate(rounds, _func, _, rounds, inspects) do
    monkey_business(inspects)
  end

  def simulate(round, func, monkeys, rounds, inspects) do
    {monkeys, inspects} =
      0..(map_size(monkeys) - 1)
      |> Enum.reduce(
        {monkeys, inspects},
        fn i, {monkeys, inspects} ->
          [monkey_items | _] = monkeys[i]

          {
            play_monkey(i, monkey_items, func, monkeys),
            increment_inspects(i, length(monkey_items), inspects)
          }
        end
      )

    #    IO.puts("\n After round #{round}")
    #    IO.inspect(inspects)
    simulate(round + 1, func, monkeys, rounds, inspects)
  end

  def increment_inspects(monkey, amount, inspects) do
    {_, updated_inspects} =
      Map.get_and_update(inspects, monkey, fn current ->
        case current do
          nil -> {nil, amount}
          current -> {current, current + amount}
        end
      end)

    updated_inspects
  end

  def play_monkey(_, [], _func, monkeys) do
    monkeys
  end

  def play_monkey(i, [item | rest], func, monkeys) do
    [_, op, test, if_true, if_false] = monkeys[i]
    worry_level = func.(op.(item))

    case rem(worry_level, test) == 0 do
      true -> play_monkey(i, rest, func, throw(worry_level, i, if_true, monkeys))
      false -> play_monkey(i, rest, func, throw(worry_level, i, if_false, monkeys))
    end
  end

  def throw(item, monkey_from, monkey_to, monkeys) do
    [items_from | rest_from] = monkeys[monkey_from]
    [items_to | rest_to] = monkeys[monkey_to]

    monkeys
    |> Map.put(monkey_to, [items_to ++ [item] | rest_to])
    |> Map.put(monkey_from, [tl(items_from) | rest_from])
  end

  def monkey_business(inspects) do
    [first | [second | _rest]] =
      inspects
      |> Map.to_list()
      |> Enum.map(&Tuple.to_list/1)
      |> Enum.sort(&(Enum.at(&1, 1) >= Enum.at(&2, 1)))

    Enum.at(first, 1) * Enum.at(second, 1)
  end
end

monkeys = MonkeyInTheMiddle.read_input("11_monkey_in_the_middle.input")
# IO.inspect(monkeys, charlists: :as_lists)

part_1 = MonkeyInTheMiddle.simulate(20, fn x -> div(x, 3) end, monkeys)
IO.puts("Part 1: #{part_1}")
