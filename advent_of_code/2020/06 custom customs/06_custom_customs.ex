defmodule CustomCustoms do
  def parse_input_1(data) do
    data
    |> String.split("\n\n")
    |> Enum.map(fn group -> String.replace(group, "\n", "") end)
    |> Enum.map(fn responses -> MapSet.new(String.codepoints(responses)) end)
  end

  def count(responses) do
    responses
    |> Enum.map(fn group -> MapSet.size(group) end)
    |> Enum.reduce(0, fn cardinal, acc -> acc + cardinal end)
  end

  def parse_input_2(data) do
    data
    |> String.split("\n\n")
    |> Enum.map(fn group ->
      Enum.map(String.split(group, "\n"), fn person ->
        MapSet.new(String.codepoints(person))
      end)
    end)
    |> Enum.map(fn group_sets -> intersection(group_sets) end)
  end

  def intersection(set_list) do
    first_set = List.first(set_list)
    Enum.reduce(set_list, first_set, fn set, acc -> MapSet.intersection(set, acc) end)
  end
end

{:ok, data} = File.read("06_custom_customs.input")
count_1 = CustomCustoms.count(CustomCustoms.parse_input_1(data))
IO.puts("Part 1: #{count_1}")

count_2 = CustomCustoms.count(CustomCustoms.parse_input_2(data))
IO.puts("Part 2: #{count_2}")
