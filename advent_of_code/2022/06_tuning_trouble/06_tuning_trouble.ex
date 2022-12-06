defmodule TuningTrouble do
  def read_input(filename) do
    {:ok, signal} = File.read(filename)
    signal |> to_charlist()
  end

  def unique(chars) do
    MapSet.size(MapSet.new(chars))
  end

  def find_marker(i, size, signal) do
    if unique(Enum.slice(signal, (i - (size - 1))..i)) == size do
      i + 1
    else
      find_marker(i + 1, size, signal)
    end
  end
end

signal = TuningTrouble.read_input("06_tuning_trouble.input")

part_1 = TuningTrouble.find_marker(3, 4, signal)
IO.puts("Part 1: #{part_1}")

part_2 = TuningTrouble.find_marker(13, 14, signal)
IO.puts("Part 2: #{part_2}")
