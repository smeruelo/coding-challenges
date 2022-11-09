defmodule MonsterMessages do
  def parse_grammar_rule(line) do
    [left, rest] = String.split(line, ": ")
    rule = String.to_integer(left)

    next_rules =
      case rest do
        "\"a\"" -> ?a
        "\"b\"" -> ?b
        rest -> parse_next_rules(rest)
      end

    {rule, next_rules}
  end

  def parse_next_rules(s) do
    parse_rule_sequence = fn rules ->
      rules |> String.split(" ") |> Enum.map(&String.to_integer/1)
    end

    case String.split(s, " | ") do
      [rules] -> [parse_rule_sequence.(rules)]
      [_ | _] = lst -> Enum.map(lst, fn rules -> parse_rule_sequence.(rules) end)
    end
  end

  def parse_grammar(lines) do
    lines
    |> Enum.map(&parse_grammar_rule/1)
    |> Enum.reduce(%{}, fn {rule, next_rules}, acc ->
      Map.put(acc, rule, next_rules)
    end)
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    [top, bottom] = String.split(data, "\n\n")
    messages = bottom |> String.split("\n") |> Enum.map(&to_charlist/1)
    grammar = top |> String.split("\n") |> parse_grammar()

    {messages, grammar}
  end

  def parse_message(message, grammar), do: parse_message(message, [0], grammar)
  def parse_message([], [], _), do: true
  def parse_message([], _, _), do: false
  def parse_message(_, [], _), do: false

  def parse_message([chr | pending_message] = message, [rule | pending_rules], grammar) do
    case {Map.get(grammar, rule), chr} do
      {next_rules, _} when is_list(next_rules) ->
        Enum.map(next_rules, fn rules_option ->
          parse_message(
            message,
            rules_option ++ pending_rules,
            grammar
          )
        end)
        |> Enum.any?()

      {chr1, chr2} when chr1 == chr2 ->
        parse_message(pending_message, pending_rules, grammar)

      {chr1, chr2} when chr1 != chr2 ->
        false
    end
  end

  def count({messages, grammar}) do
    messages
    |> Enum.map(fn msg -> parse_message(msg, grammar) end)
    |> Enum.count(& &1)
  end
end

count_1 =
  "19_monster_messages_1.input"
  |> MonsterMessages.read_input()
  |> MonsterMessages.count()

count_2 =
  "19_monster_messages_2.input"
  |> MonsterMessages.read_input()
  |> MonsterMessages.count()

IO.puts("Part 1: #{count_1}")
IO.puts("Part 2: #{count_2}")
