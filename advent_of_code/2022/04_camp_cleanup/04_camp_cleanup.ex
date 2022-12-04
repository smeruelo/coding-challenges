defmodule CampCleanup do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&String.split(&1, ","))
    |> Enum.map(&Enum.map(&1, fn r -> parse_range(r) end))
  end

  def parse_range(str) do
    [first, last] =
      str
      |> String.split("-")
      |> Enum.map(&String.to_integer/1)

    first..last
  end

  def embedded([first_1..last_1 = range_1, first_2..last_2 = range_2]) do
    (first_1 in range_2 and last_1 in range_2) or (first_2 in range_1 and last_2 in range_1)
  end

  def overlapped([first_1.._last_1 = range_1, first_2.._last_2 = range_2]) do
    first_1 in range_2 or first_2 in range_1
  end
end

assignments = CampCleanup.read_input("04_camp_cleanup.input")

part_1 = Enum.count(assignments, &CampCleanup.embedded/1)
IO.puts("Part 1: #{part_1}")

part_2 = Enum.count(assignments, &CampCleanup.overlapped/1)
IO.puts("Part 2: #{part_2}")
