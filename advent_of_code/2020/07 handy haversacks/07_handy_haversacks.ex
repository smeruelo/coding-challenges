defmodule HandyHaversacks do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_rule/1)
    |> Enum.reduce(%{}, fn rule, acc -> add_vertex_to_graph(rule, acc) end)
  end

  def parse_rule(rule_line) do
    [container, rest] = String.split(rule_line, " bags contain ")

    {_, contents} =
      rest
      |> String.split([" bag, ", " bag.", " bags, ", " bags."])
      |> List.pop_at(-1)

    case contents do
      ["no other"] -> {container, []}
      lst -> {container, Enum.map(lst, &quantity_and_bag/1)}
    end
  end

  def quantity_and_bag(str) do
    {quantity, rest} = Integer.parse(str)
    {quantity, String.slice(rest, 1..-1)}
  end

  def add_vertex_to_graph(rule, graph) do
    {vertex, adjacencies} = rule
    Map.put(graph, vertex, adjacencies)
  end

  def is_there_path?({_, bag_source} = _from, {_, bag_target} = to, graph) do
    if bag_source == bag_target do
      true
    else
      case graph[bag_source] do
        [] ->
          false

        adjacencies ->
          adjacencies
          |> Enum.map(fn adj -> is_there_path?(adj, to, graph) end)
          |> Enum.any?()
      end
    end
  end

  def count_possible_containers_of(bag, graph) do
    graph
    |> Map.keys()
    |> List.delete(bag)
    |> Enum.reduce(0, fn vertex, count ->
      case is_there_path?({-1, vertex}, {-1, bag}, graph) do
        true -> count + 1
        false -> count
      end
    end)
  end

  def count_inside_bags(bag, graph) do
    1 +
      Enum.reduce(graph[bag], 0, fn {q, b}, acc ->
        acc + q * count_inside_bags(b, graph)
      end)
  end
end

graph = HandyHaversacks.read_input("07_handy_haversacks.input")

count_1 = HandyHaversacks.count_possible_containers_of("shiny gold", graph)
IO.puts("Part 1: #{count_1}")

count_2 = HandyHaversacks.count_inside_bags("shiny gold", graph) - 1
IO.puts("Part 2: #{count_2}")
