defmodule OperationOrder do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    parse_token = fn token ->
      case token do
        "+" -> :sum
        "*" -> :multiply
        "(" -> :open
        ")" -> :close
        num -> String.to_integer(num)
      end
    end

    tokenize = fn line ->
      line
      |> String.replace("(", "( ")
      |> String.replace(")", " )")
      |> String.split(" ")
      |> Enum.map(parse_token)
    end

    data
    |> String.split("\n")
    |> Enum.map(tokenize)
  end

  def eval(num1, :sum, num2), do: num1 + num2

  def eval(num1, :multiply, num2), do: num1 * num2

  def eval_1([num]), do: num

  def eval_1([num1 | [op | [num2 | rest]]]) do
    eval_1([eval(num1, op, num2) | rest])
  end

  def eval_2([num]), do: num

  def eval_2([num1 | [:sum | [num2 | rest]]]) do
    eval_2([eval(num1, :sum, num2) | rest])
  end

  def eval_2([num1 | [:multiply | rest]]) do
    num1 * eval_2(rest)
  end

  def evaluate_expression([], acc, eval_fn) do
    eval_fn.(Enum.reverse(acc))
  end

  def evaluate_expression([current | rest], acc, eval_fn) do
    case current do
      :open ->
        {paren_content_evaluated, rest} = evaluate_expression(rest, [], eval_fn)
        evaluate_expression(rest, [paren_content_evaluated | acc], eval_fn)

      :close ->
        {eval_fn.(Enum.reverse(acc)), rest}

      other ->
        evaluate_expression(rest, [other | acc], eval_fn)
    end
  end
end

expressions = OperationOrder.read_input("18_operation_order.input")

part_1 =
  Enum.reduce(expressions, 0, fn expr, acc ->
    acc + OperationOrder.evaluate_expression(expr, [], &OperationOrder.eval_1/1)
  end)

IO.puts("Part 1: #{part_1}")

part_2 =
  Enum.reduce(expressions, 0, fn expr, acc ->
    acc + OperationOrder.evaluate_expression(expr, [], &OperationOrder.eval_2/1)
  end)

IO.puts("Part 2: #{part_2}")
