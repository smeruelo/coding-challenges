defmodule TicketTranslation do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    [lines_rules, lines_my_ticket, lines_nearby_tickets] =
      data
      |> String.split("\n\n")
      |> Enum.map(fn lines -> String.split(lines, "\n") end)

    rules = Enum.map(lines_rules, &parse_rule/1)
    my_ticket = parse_ticket(Enum.at(lines_my_ticket, 1))
    nearby_tickets = Enum.map(Enum.slice(lines_nearby_tickets, 1..-1), &parse_ticket/1)

    {rules, my_ticket, nearby_tickets}
  end

  def parse_range(range) do
    range
    |> String.split("-")
    |> Enum.map(&String.to_integer/1)
  end

  def parse_rule(line) do
    [name, rest] = String.split(line, ": ")
    [range_1, range_2] = Enum.map(String.split(rest, " or "), &parse_range/1)

    {name, range_1, range_2}
  end

  def parse_ticket(line) do
    line
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  def obeys_rule?(value, rule) do
    {_, [min1, max1], [min2, max2]} = rule
    (value >= min1 and value <= max1) or (value >= min2 and value <= max2)
  end

  def obeys_any_rule?(value, rules) do
    Enum.any?(rules, fn r -> obeys_rule?(value, r) end)
  end

  def is_valid?(ticket, rules) do
    Enum.all?(ticket, fn v -> obeys_any_rule?(v, rules) end)
  end

  def ticket_error(ticket, rules) do
    Enum.reduce(ticket, 0, fn v, acc ->
      if obeys_any_rule?(v, rules) do
        acc
      else
        acc + v
      end
    end)
  end

  def error_rate(tickets, rules) do
    Enum.reduce(tickets, 0, fn t, acc ->
      acc + ticket_error(t, rules)
    end)
  end

  def discard_invalid(tickets, rules) do
    Enum.filter(tickets, fn t -> is_valid?(t, rules) end)
  end

  def rule_obeyed_by_all?(values, rule) do
    Enum.all?(values, fn v -> obeys_rule?(v, rule) end)
  end

  def possible_fields_for_rule(rule, indexed_zipped_fields) do
    indexed_zipped_fields
    |> Enum.filter(fn {_index, values} -> rule_obeyed_by_all?(values, rule) end)
    |> Enum.map(fn {index, _values} -> index end)
  end

  def possible_assignments(tickets, rules) do
    zipped_fields =
      tickets
      |> discard_invalid(rules)
      |> Enum.zip()

    indexed_zipped_fields =
      [zipped_fields, 0..19]
      |> Enum.zip_with(fn [field_values, field_index] ->
        {field_index, Tuple.to_list(field_values)}
      end)

    rules
    |> Enum.map(fn r ->
      {elem(r, 0), possible_fields_for_rule(r, indexed_zipped_fields)}
    end)
    |> Enum.sort(fn {_, x}, {_, y} -> length(x) <= length(y) end)
  end

  def identify_fields([], dict) do
    dict
  end

  def identify_fields([{rule, indexes} | rest], dict) do
    [index] = Enum.filter(indexes, fn i -> is_nil(Map.get(dict, i)) end)
    identify_fields(rest, Map.put(dict, index, rule))
  end

  def departure_values(ticket, nearby_tickets, rules) do
    dict = identify_fields(possible_assignments(nearby_tickets, rules), %{})

    0..(length(ticket) - 1)
    |> Enum.zip(ticket)
    |> Enum.reduce(1, fn {i, v}, acc ->
      if String.starts_with?(Map.get(dict, i, ""), "departure") do
        acc * v
      else
        acc
      end
    end)
  end
end

{rules, my_ticket, nearby_tickets} = TicketTranslation.read_input("16_ticket_translation.input")

part_1 = TicketTranslation.error_rate(nearby_tickets, rules)
IO.puts("Part 1: #{part_1}")

part_2 = TicketTranslation.departure_values(my_ticket, nearby_tickets, rules)
IO.puts("Part 2: #{part_2}")
