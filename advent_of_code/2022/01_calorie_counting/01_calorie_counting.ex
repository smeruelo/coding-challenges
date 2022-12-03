defmodule CalorieCounting do
  def parse_elfs_calories(block) do
    block
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.map(&parse_elfs_calories/1)
  end

  def biggest(calories) do
    Enum.max(Enum.map(calories, &Enum.sum/1))
  end

  def sum_of_bigger_three(calories) do
    calories
    |> Enum.map(&Enum.sum/1)
    |> Enum.sort(:desc)
    |> Enum.slice(0..2)
    |> Enum.sum()
  end
end

calories = CalorieCounting.read_input("01_calorie_counting.input")

part_1 = CalorieCounting.biggest(calories)
IO.puts("Part_1: #{part_1}")

part_2 = CalorieCounting.sum_of_bigger_three(calories)
IO.puts("Part_2: #{part_2}")
