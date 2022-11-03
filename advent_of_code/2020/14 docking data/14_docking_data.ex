defmodule DockingData do
  def parse_line(line) do
    [left, right] = line |> String.split(" = ")

    case left do
      "mask" ->
        {:mask, String.to_charlist(right)}

      _ ->
        value = String.to_integer(right)
        [_, address, _] = String.split(left, ["[", "]"])
        {:mem, String.to_integer(address), value}
    end
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(fn line -> parse_line(line) end)
  end

  def mask_1(value, mask) do
    value
    |> Integer.to_string(2)
    |> String.pad_leading(36, "0")
    |> String.to_charlist()
    |> Enum.zip_with(mask, fn a, b ->
      case b do
        ?X -> a
        b -> b
      end
    end)
    |> to_string()
    |> String.to_integer(2)
  end

  def run_1([], _mask, memory) do
    Enum.sum(Map.values(memory))
  end

  def run_1([instruction | rest], mask, memory) do
    case instruction do
      {:mask, mask} ->
        run_1(rest, mask, memory)

      {:mem, address, value} ->
        run_1(rest, mask, Map.put(memory, address, mask_1(value, mask)))
    end
  end

  def mask_2(address, mask) do
    address
    |> Integer.to_string(2)
    |> String.pad_leading(36, "0")
    |> String.to_charlist()
    |> Enum.zip_with(mask, fn a, b ->
      case b do
        ?1 -> ?1
        ?0 -> a
        ?X -> ?X
      end
    end)
  end

  def resolve_floatiness([], _power, acc) do
    [acc]
  end

  def resolve_floatiness([hd | tl], power, acc) do
    case hd do
      ?X ->
        resolve_floatiness(tl, power - 1, acc) ++
          resolve_floatiness(tl, power - 1, acc + Integer.pow(2, power))

      b ->
        resolve_floatiness(tl, power - 1, acc + (b - 48) * Integer.pow(2, power))
    end
  end

  def all_possible_addresses(unmasked_address, mask) do
    resolve_floatiness(mask_2(unmasked_address, mask), 35, 0)
  end

  def run_2([], _mask, memory) do
    Enum.sum(Map.values(memory))
  end

  def run_2([instruction | rest], mask, memory) do
    case instruction do
      {:mask, mask} ->
        run_2(rest, mask, memory)

      {:mem, address, value} ->
        new_writes =
          address
          |> all_possible_addresses(mask)
          |> Enum.reduce(%{}, fn x, acc -> Map.put(acc, x, value) end)

        run_2(rest, mask, Map.merge(memory, new_writes))
    end
  end
end

program = DockingData.read_input("14_docking_data.input")
sum_1 = DockingData.run_1(program, "", %{})
IO.puts("Part 1: #{sum_1}")

sum_2 = DockingData.run_2(program, "", %{})
IO.puts("Part 2: #{sum_2}")
