defmodule SupplyStacks do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_move/1)
  end

  def parse_move(line) do
    [left, right] = String.split(line, " from ")
    [_, amount] = String.split(left, "move ")
    [from, to] = String.split(right, " to ")

    [amount, from, to] |> Enum.map(&String.to_integer/1)
  end

  def tops(stacks) do
    Enum.map(1..map_size(stacks), fn i -> hd(stacks[i]) end)
  end

  def move_crates_1([], stacks) do
    tops(stacks)
  end

  def move_crates_1([[0, _from, _to] | rest_moves], stacks) do
    move_crates_1(rest_moves, stacks)
  end

  def move_crates_1([[amount, from, to] | rest_moves], stacks) do
    from_stack = stacks[from]
    to_stack = stacks[to]

    move_crates_1(
      [[amount - 1, from, to] | rest_moves],
      %{stacks | from => tl(from_stack), to => [hd(from_stack) | to_stack]}
    )
  end

  def move_crates_2([], stacks) do
    tops(stacks)
  end

  def move_crates_2([[amount, from, to] | rest_moves], stacks) do
    from_stack = stacks[from]
    to_stack = stacks[to]

    moving = Enum.slice(from_stack, 0..(amount - 1))
    new_from = Enum.slice(from_stack, amount..-1)
    new_to = moving ++ to_stack

    move_crates_2(
      rest_moves,
      %{stacks | from => new_from, to => new_to}
    )
  end
end

_stacks_example = %{1 => 'NZ', 2 => 'DCM', 3 => 'P'}

stacks = %{
  1 => 'LCGMQ',
  2 => 'GHFTCLDR',
  3 => 'RWTMNFJV',
  4 => 'PQVDFJ',
  5 => 'TBLSMFN',
  6 => 'PDCHVNR',
  7 => 'TCH',
  8 => 'PHNZVJSG',
  9 => 'GHFZ'
}

moves = SupplyStacks.read_input("05_supply_stacks.input")

part_1 = SupplyStacks.move_crates_1(moves, stacks)
IO.puts("Part 1: #{part_1}")

part_2 = SupplyStacks.move_crates_2(moves, stacks)
IO.puts("Part 2: #{part_2}")
