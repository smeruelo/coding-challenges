defmodule UnstableDiffusion do
  #  @size 73

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&to_charlist/1)
    |> Enum.with_index()
    |> Enum.reduce(MapSet.new(), fn {line, y}, acc_elves ->
      line
      |> Enum.with_index()
      |> Enum.reduce(acc_elves, fn {chr, x}, acc_acc_elves ->
        case chr do
          ?. -> acc_acc_elves
          ?# -> MapSet.put(acc_acc_elves, {y, x})
        end
      end)
    end)
  end

  def north({y, x}), do: {y - 1, x}
  def northwest({y, x}), do: {y - 1, x - 1}
  def northeast({y, x}), do: {y - 1, x + 1}
  def south({y, x}), do: {y + 1, x}
  def southwest({y, x}), do: {y + 1, x - 1}
  def southeast({y, x}), do: {y + 1, x + 1}
  def west({y, x}), do: {y, x - 1}
  def east({y, x}), do: {y, x + 1}

  def free?(position, elves), do: position not in elves

  def free?(:all, position, elves) do
    free?(
      [
        &north/1,
        &northeast/1,
        &northwest/1,
        &south/1,
        &southeast/1,
        &southwest/1,
        &west/1,
        &east/1
      ],
      position,
      elves
    )
  end

  def free?(directions, position, elves) do
    directions
    |> Enum.map(fn f -> free?(f.(position), elves) end)
    |> Enum.all?()
  end

  def try_move(:north, elf, elves) do
    if free?([&north/1, &northwest/1, &northeast/1], elf, elves) do
      {:halt, north(elf)}
    else
      {:cont, nil}
    end
  end

  def try_move(:south, elf, elves) do
    if free?([&south/1, &southwest/1, &southeast/1], elf, elves) do
      {:halt, south(elf)}
    else
      {:cont, nil}
    end
  end

  def try_move(:west, elf, elves) do
    if free?([&northwest/1, &west/1, &southwest/1], elf, elves) do
      {:halt, west(elf)}
    else
      {:cont, nil}
    end
  end

  def try_move(:east, elf, elves) do
    if free?([&northeast/1, &east/1, &southeast/1], elf, elves) do
      {:halt, east(elf)}
    else
      {:cont, nil}
    end
  end

  def proposal(directions, elf, elves) do
    Enum.reduce_while(directions, nil, fn dir, _acc -> try_move(dir, elf, elves) end)
  end

  def add_proposal_if_unique(elf, new_pos, proposals, updated_elves) do
    case proposals[new_pos] do
      nil ->
        {
          Map.put(proposals, new_pos, elf),
          MapSet.put(updated_elves, new_pos)
        }

      other_elf ->
        {
          Map.delete(proposals, new_pos),
          updated_elves |> MapSet.delete(new_pos) |> MapSet.put(elf) |> MapSet.put(other_elf)
        }
    end
  end

  def next_directions([first, second, third, fourth]), do: [second, third, fourth, first]

  def count_free_positions(elves) do
    y_sorted = Enum.sort(elves, fn {y1, _}, {y2, _} -> y1 < y2 end)
    x_sorted = Enum.sort(elves, fn {_, x1}, {_, x2} -> x1 < x2 end)
    {_, min_x} = List.first(x_sorted)
    {_, max_x} = List.last(x_sorted)
    {min_y, _} = List.first(y_sorted)
    {max_y, _} = List.last(y_sorted)
    (max_x - min_x + 1) * (max_y - min_y + 1) - MapSet.size(elves)
  end

  def diffuse(rules, elves, round, f_stop, f_out) do
    {acc_proposals, updated_elves} =
      Enum.reduce(elves, {%{}, MapSet.new()}, fn elf, {acc_proposals, acc_elves} ->
        if free?(:all, elf, elves) do
          {acc_proposals, MapSet.put(acc_elves, elf)}
        else
          case proposal(rules, elf, elves) do
            nil -> {acc_proposals, MapSet.put(acc_elves, elf)}
            new_pos -> add_proposal_if_unique(elf, new_pos, acc_proposals, acc_elves)
          end
        end
      end)

    if f_stop.(round, acc_proposals) do
      f_out.(round, updated_elves)
    else
      diffuse(next_directions(rules), updated_elves, round + 1, f_stop, f_out)
    end
  end

  def diffuse(elves, f_stop, f_out) do
    diffuse([:north, :south, :west, :east], elves, 1, f_stop, f_out)
  end
end

elves = UnstableDiffusion.read_input("23_unstable_diffusion.input")

part_1 =
  UnstableDiffusion.diffuse(
    elves,
    fn round, _proposals -> round == 10 end,
    fn _round, elves -> UnstableDiffusion.count_free_positions(elves) end
  )

IO.puts("Part 1: #{part_1}")

part_2 =
  UnstableDiffusion.diffuse(
    elves,
    fn _round, proposals -> map_size(proposals) == 0 end,
    fn round, _elves -> round end
  )

IO.puts("Part 2: #{part_2}")
