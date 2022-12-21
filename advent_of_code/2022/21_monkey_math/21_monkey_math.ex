defmodule MonkeyMath do
  def read_input_1(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_line_1/1)
  end

  def parse_line_1(line) do
    [name, right] = String.split(line, ": ")

    case String.split(right, " ") do
      [arg_1, op, arg_2] -> {name, parse_op(op), arg_1, arg_2}
      [num] -> {name, String.to_integer(num)}
    end
  end

  def parse_op(op) do
    case op do
      "+" -> fn x, y -> x + y end
      "-" -> fn x, y -> x - y end
      "*" -> fn x, y -> x * y end
      "/" -> fn x, y -> div(x, y) end
    end
  end

  def yell_1(input) do
    yell_1(input, [], %{})
  end

  def yell_1([], [], values) do
    values["root"]
  end

  def yell_1([], pending, values) do
    yell_1(pending, [], values)
  end

  def yell_1([{name, num} | rest], pending, values) do
    yell_1(rest, pending, Map.put(values, name, num))
  end

  def yell_1([{name, f, arg_1, arg_2} | rest], pending, values) do
    case {Map.get(values, arg_1), Map.get(values, arg_2)} do
      {r1, r2} when is_nil(r1) or is_nil(r2) ->
        yell_1(rest, [{name, f, arg_1, arg_2} | pending], values)

      {num_1, num_2} ->
        yell_1(rest, pending, Map.put(values, name, f.(num_1, num_2)))
    end
  end

  def read_input_2(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_line_2/1)
    |> Enum.filter(fn x -> !is_nil(x) end)
  end

  def parse_line_2(line) do
    [name, right] = String.split(line, ": ")

    case String.split(right, " ") do
      [arg_1, op, arg_2] ->
        if name == "root" do
          {"root", "==", arg_1, arg_2}
        else
          {name, parse_op(op), arg_1, arg_2}
        end

      [num] ->
        if name == "humn" do
          nil
        else
          {name, String.to_integer(num)}
        end
    end
  end

  def find_number(f, n1, n2) do
    n = n2 + div(n1 - n2, 2)

    cond do
      f.(n) == 0 -> n
      f.(n) < 0 -> find_number(f, n, n2)
      f.(n) > 0 -> find_number(f, n1, n)
    end
  end

  def yell_2(input) do
    yell_2(input, [], %{"humn" => fn x -> x end})
  end

  def yell_2([], [{"root", _, arg_1, arg_2}], values) do
    find_number(fn humn -> values[arg_1].(humn) - values[arg_2] end, values[arg_2], 0)
  end

  def yell_2([], pending, values) do
    yell_2(pending, [], values)
  end

  def yell_2([{name, num} | rest], pending, values) do
    yell_2(rest, pending, Map.put(values, name, num))
  end

  def yell_2([{name, op, arg_1, arg_2} | rest], pending, values) do
    case {Map.get(values, arg_1), Map.get(values, arg_2)} do
      {r1, r2} when is_nil(r1) or is_nil(r2) ->
        yell_2(rest, [{name, op, arg_1, arg_2} | pending], values)

      {f_1, num_2} when is_function(f_1) and is_integer(num_2) ->
        g = fn humn -> op.(f_1.(humn), num_2) end
        yell_2(rest, pending, Map.put(values, name, g))

      {num_1, f_2} when is_function(f_2) and is_integer(num_1) ->
        g = fn humn -> op.(num_1, f_2.(humn)) end
        yell_2(rest, pending, Map.put(values, name, g))

      {num_1, num_2} when is_integer(num_1) and is_integer(num_2) ->
        v = op.(num_1, num_2)
        yell_2(rest, pending, Map.put(values, name, v))
    end
  end
end

input_1 = MonkeyMath.read_input_1("21_monkey_math.input")
part_1 = MonkeyMath.yell_1(input_1)
IO.puts("Part 1: #{part_1}")

input_2 = MonkeyMath.read_input_2("21_monkey_math.input")
part_2 = MonkeyMath.yell_2(input_2)
IO.puts("Part 2: #{part_2}")
