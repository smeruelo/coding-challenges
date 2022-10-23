defmodule EncodingError do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end

  def number_valid?(preambule, number) do
    preambule
    |> Enum.map(fn x -> number - x end)
    |> Enum.zip_with(preambule, fn x, y -> x >= 0 and x != y and x in preambule end)
    |> Enum.any?()
  end

  def attack(numbers, i, size) do
    preambule = Enum.slice(numbers, (i - size)..(i - 1))
    current = Enum.at(numbers, i)

    case number_valid?(preambule, current) do
      true -> attack(numbers, i + 1, size)
      false -> current
    end
  end

  def find_contiguous(numbers, i, j, current_sum, expected) do
    if current_sum == expected do
      block = Enum.slice(numbers, i..j) |> Enum.sort()
      List.first(block) + List.last(block)
    else
      if current_sum < expected do
        find_contiguous(numbers, i, j + 1, current_sum + Enum.at(numbers, j + 1), expected)
      else
        find_contiguous(numbers, i + 1, j, current_sum - Enum.at(numbers, i), expected)
      end
    end
  end
end

numbers = EncodingError.read_input("09_encoding_error.input")
result_1 = EncodingError.attack(numbers, 25, 25)
IO.puts("Part 1: #{result_1}")

result_2 =
  EncodingError.find_contiguous(
    numbers,
    0,
    1,
    Enum.at(numbers, 0) + Enum.at(numbers, 1),
    result_1
  )

IO.puts("Part 2: #{result_2}")
