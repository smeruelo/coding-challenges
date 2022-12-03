defmodule RucksackReorganization do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&to_charlist/1)
  end

  def into_compartments(rucksack) do
    Enum.chunk_every(rucksack, div(length(rucksack), 2))
  end

  def into_groups(rucksacks) do
    Enum.chunk_every(rucksacks, 3)
  end

  def find_common(rucksack) do
    rucksack
    |> Enum.map(&MapSet.new/1)
    |> Enum.reduce(&MapSet.intersection/2)
    |> MapSet.to_list()
    |> hd()
  end

  def priority(item) do
    cond do
      item in ?a..?z -> item - 96
      item in ?A..?Z -> item - 38
    end
  end

  def prioritize(rucksacks) do
    rucksacks
    |> Enum.map(&find_common/1)
    |> Enum.map(&priority/1)
    |> Enum.sum()
  end
end

rucksacks = RucksackReorganization.read_input("03_rucksack_reorganization.input")

part_1 =
  rucksacks
  |> Enum.map(&RucksackReorganization.into_compartments/1)
  |> RucksackReorganization.prioritize()

part_2 =
  rucksacks
  |> RucksackReorganization.into_groups()
  |> RucksackReorganization.prioritize()

IO.puts("Part 1: #{part_1}")
IO.puts("Part 2: #{part_2}")
