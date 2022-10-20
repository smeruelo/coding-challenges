defmodule PassportProcessing do
  def parse_passport(key_value_list) do
    Enum.reduce(key_value_list, %{}, fn [key, value], acc -> Map.put(acc, key, value) end)
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.map(fn str -> String.replace(str, "\n", " ") end)
    |> Enum.map(fn str -> String.split(str, " ") end)
    |> Enum.map(fn lst -> Enum.map(lst, fn key_value -> String.split(key_value, ":") end) end)
    |> Enum.map(fn lst -> parse_passport(lst) end)
  end

  def is_valid_1?(passport) do
    Enum.reduce(
      ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
      true,
      fn field, acc -> acc and Map.has_key?(passport, field) end
    )
  end

  def is_valid_2?(passport) do
    is_valid_1?(passport) and
      valid_byr?(passport["byr"]) and
      valid_iyr?(passport["iyr"]) and
      valid_eyr?(passport["eyr"]) and
      valid_hgt?(passport["hgt"]) and
      valid_hcl?(passport["hcl"]) and
      valid_ecl?(passport["ecl"]) and
      valid_pid?(passport["pid"])
  end

  defp valid_byr?(byr) do
    byr_num = String.to_integer(byr)
    byr_num >= 1920 and byr_num <= 2002
  end

  defp valid_iyr?(iyr) do
    iyr_num = String.to_integer(iyr)
    iyr_num >= 2010 and iyr_num <= 2020
  end

  defp valid_eyr?(eyr) do
    eyr_num = String.to_integer(eyr)
    eyr_num >= 2020 and eyr_num <= 2030
  end

  defp valid_height_cm?(hgt) do
    try do
      height = String.to_integer(hgt)
      height >= 150 and height <= 193
    rescue
      ArgumentError -> false
    end
  end

  defp valid_height_in?(hgt) do
    try do
      height = String.to_integer(hgt)
      height >= 59 and height <= 76
    rescue
      ArgumentError -> false
    end
  end

  defp valid_hgt?(hgt) do
    case String.ends_with?(hgt, "cm") do
      true ->
        valid_height_cm?(String.slice(hgt, 0..-3))

      false ->
        case String.ends_with?(hgt, "in") do
          true ->
            valid_height_in?(String.slice(hgt, 0..-3))

          false ->
            false
        end
    end
  end

  defp valid_hcl?(hcl) do
    Regex.match?(~r/^#[0-9a-f]{6}$/, hcl)
  end

  defp valid_ecl?(ecl) do
    ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  end

  defp valid_pid?(pid) do
    Regex.match?(~r/^[0-9]{9}$/, pid)
  end
end

passports = PassportProcessing.read_input("04_passport_processing.input")

count1 =
  Enum.reduce(passports, 0, fn passport, acc ->
    case PassportProcessing.is_valid_1?(passport) do
      true -> acc + 1
      false -> acc
    end
  end)

IO.puts("Part 1: #{count1}")

count2 =
  Enum.reduce(passports, 0, fn passport, acc ->
    case PassportProcessing.is_valid_2?(passport) do
      true -> acc + 1
      false -> acc
    end
  end)

IO.puts("Part 2: #{count2}")
