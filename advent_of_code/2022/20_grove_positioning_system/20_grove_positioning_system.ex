defmodule GrovePositioningSystem do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(fn s -> String.to_integer(s) end)
    |> Enum.with_index()
  end

  def find_current_position(original_position, encrypted) do
    Enum.find_index(encrypted, fn {_num, index} -> index == original_position end)
  end

  def find_zero(encrypted) do
    Enum.find_index(encrypted, fn {num, _original_position} -> num == 0 end)
  end

  def mix(encrypted, _original_position, rounds, rounds) do
    encrypted
  end

  def mix(encrypted, original_position, round, rounds)
      when original_position == length(encrypted) do
    mix(encrypted, 0, round + 1, rounds)
  end

  def mix(encrypted, original_position, round, rounds) do
    current_position = find_current_position(original_position, encrypted)
    {{number, original_position}, tmp_list} = List.pop_at(encrypted, current_position)
    new_position = Integer.mod(current_position + number, length(encrypted) - 1)

    mix(
      List.insert_at(tmp_list, new_position, {number, original_position}),
      original_position + 1,
      round,
      rounds
    )
  end

  def mix(encrypted, rounds) do
    mix(encrypted, 0, 0, rounds)
  end

  def grove(encrypted) do
    mixed = mix(encrypted, 0)
    zero_position = find_zero(mixed)

    [1000, 2000, 3000]
    |> Enum.map(fn i -> Integer.mod(i + zero_position, length(mixed)) end)
    |> Enum.map(fn i -> elem(Enum.at(mixed, i), 0) end)
    |> Enum.sum()
  end
end

encrypted = GrovePositioningSystem.read_input("20_grove_positioning_system.input")

part_1 = GrovePositioningSystem.grove(GrovePositioningSystem.mix(encrypted, 1))
IO.puts("Part 1: #{part_1}")

part_2 =
  encrypted
  |> Enum.map(fn {n, i} -> {n * 811_589_153, i} end)
  |> GrovePositioningSystem.mix(10)
  |> GrovePositioningSystem.grove()

IO.puts("Part 2: #{part_2}")
