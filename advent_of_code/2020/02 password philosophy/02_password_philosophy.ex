defmodule PasswordPhilosophy do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(fn line -> String.split(line, ["-", " ", ": "]) end)
  end

  def is_valid_1?([min, max, char, password]) do
    min = String.to_integer(min)
    max = String.to_integer(max)
    frequencies = String.graphemes(password) |> Enum.frequencies()

    case Map.get(frequencies, char) do
      nil -> false
      x -> x >= min and x <= max
    end
  end

  def is_valid_2?([pos1, pos2, char, password]) do
    pos1 = String.to_integer(pos1) - 1
    pos2 = String.to_integer(pos2) - 1

    case String.at(password, pos1) do
      ^char -> String.at(password, pos2) != char
      _ -> String.at(password, pos2) == char
    end
  end

  def count_valid_passwords(lines, f) do
    Enum.reduce(lines, 0, fn line, acc ->
      if f.(line) do
        acc + 1
      else
        acc
      end
    end)
  end
end

lines = PasswordPhilosophy.read_input("02_password_philosophy.input")
count1 = PasswordPhilosophy.count_valid_passwords(lines, &PasswordPhilosophy.is_valid_1?/1)
IO.puts("Part 1: #{count1}")
count2 = PasswordPhilosophy.count_valid_passwords(lines, &PasswordPhilosophy.is_valid_2?/1)
IO.puts("Part 2: #{count2}")
