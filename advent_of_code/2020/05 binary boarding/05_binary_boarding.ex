defmodule BinaryBoarding do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(fn pass -> String.replace(pass, "F", "0") end)
    |> Enum.map(fn pass -> String.replace(pass, "B", "1") end)
    |> Enum.map(fn pass -> String.replace(pass, "L", "0") end)
    |> Enum.map(fn pass -> String.replace(pass, "R", "1") end)
    |> Enum.map(fn pass -> String.to_integer(pass, 2) end)
  end

  def find_missing([hd | tl], expected) do
    if hd != expected do
      expected
    else
      find_missing(tl, expected - 1)
    end
  end
end

seats = BinaryBoarding.read_input("05_binary_boarding.input")
sorted_seats = Enum.sort(seats, &(&1 > &2))
highest = List.first(sorted_seats)
IO.puts("Part 1: #{highest}")

seat = BinaryBoarding.find_missing(sorted_seats, List.first(sorted_seats))
IO.puts("Part 2: #{seat}")
