defmodule FullOfHotAir do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split()
    |> Enum.map(&to_charlist/1)
  end

  def snafu_to_decimal(snafu) do
    Enum.reduce(snafu, 0, fn chr, acc ->
      acc * 5 +
        case chr do
          ?- -> -1
          ?= -> -2
          chr -> chr - 48
        end
    end)
  end

  def decimal_to_base_5(0, acc), do: acc
  def decimal_to_base_5(num, acc), do: decimal_to_base_5(div(num, 5), [rem(num, 5) | acc])
  def decimal_to_base_5(num), do: decimal_to_base_5(num, [])

  def base_5_to_snafu([], 0, acc), do: acc
  def base_5_to_snafu([], 1, acc), do: base_5_to_snafu([], 0, [?1 | acc])

  def base_5_to_snafu([digit | rest], carry, acc) do
    {chr, new_carry} =
      case digit + carry do
        3 -> {?=, 1}
        4 -> {?-, 1}
        5 -> {?0, 1}
        digit -> {digit + 48, 0}
      end

    base_5_to_snafu(rest, new_carry, [chr | acc])
  end

  def base_5_to_snafu(digits) do
    base_5_to_snafu(Enum.reverse(digits), 0, [])
  end

  def part_1(snafu_list) do
    snafu_list
    |> Enum.map(&snafu_to_decimal/1)
    |> Enum.sum()
    |> decimal_to_base_5()
    |> base_5_to_snafu()
  end
end

snafu_list = FullOfHotAir.read_input("25_full_of_hot_air.input")

part_1 = FullOfHotAir.part_1(snafu_list)
IO.puts("Part 1: #{part_1}")
