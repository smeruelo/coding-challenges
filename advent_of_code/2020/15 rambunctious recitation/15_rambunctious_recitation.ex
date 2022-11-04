defmodule RambunctiousRecitation do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    first_numbers =
      data
      |> String.split(",")
      |> Enum.map(&String.to_integer/1)

    Enum.zip_reduce(
      [first_numbers, 1..length(first_numbers)],
      %{},
      fn [n, turn], acc ->
        Map.put(acc, n, turn)
      end
    )
  end

  def speak_numbers(starting_numbers, max) do
    speak_numbers(map_size(starting_numbers) + 1, 0, starting_numbers, max)
  end

  def speak_numbers(turn, n, numbers, max) do
    case turn do
      ^max ->
        n

      turn ->
        {last_time, updated_numbers} =
          Map.get_and_update(numbers, n, fn old_t -> {old_t, turn} end)

        next_n =
          case last_time do
            nil -> 0
            last_time -> turn - last_time
          end

        speak_numbers(turn + 1, next_n, updated_numbers, max)
    end
  end
end

starting_numbers = RambunctiousRecitation.read_input("15_rambunctious_recitation.input")

part_1 = RambunctiousRecitation.speak_numbers(starting_numbers, 2020)
IO.puts("Part 1: #{part_1}")

part_2 = RambunctiousRecitation.speak_numbers(starting_numbers, 30_000_000)
IO.puts("Part 2: #{part_2}")
