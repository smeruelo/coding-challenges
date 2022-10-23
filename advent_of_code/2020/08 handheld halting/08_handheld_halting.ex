defmodule HandheldHalting do
  def parse_line(line) do
    [opp, rest] = String.split(line, " ")
    {num, _} = Integer.parse(rest)
    {opp, num}
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
    |> Enum.reduce({0, %{}}, fn instruction, {i, program} ->
      {i + 1, Map.put(program, i, instruction)}
    end)
    |> elem(1)
  end

  def run_until_loop(program, pointer, acc, history) do
    with false <- MapSet.member?(history, pointer),
         {opp, arg} <- program[pointer] do
      case {opp, arg} do
        {"nop", _} ->
          run_until_loop(program, pointer + 1, acc, MapSet.put(history, pointer))

        {"acc", arg} ->
          run_until_loop(program, pointer + 1, acc + arg, MapSet.put(history, pointer))

        {"jmp", arg} ->
          run_until_loop(program, pointer + arg, acc, MapSet.put(history, pointer))
      end
    else
      true -> {acc, :loop}
      nil -> {acc, :end}
    end
  end

  def brute_force_fix(program, pointer) do
    with {opp, arg} <- program[pointer] do
      fixed_program =
        case {opp, arg} do
          {"nop", arg} ->
            Map.update!(program, pointer, fn _ -> {"jmp", arg} end)

          {"jmp", arg} ->
            Map.update!(program, pointer, fn _ -> {"nop", arg} end)

          _ ->
            program
        end

      case run_until_loop(fixed_program, 0, 0, MapSet.new()) do
        {_, :loop} -> brute_force_fix(program, pointer + 1)
        {acc, :end} -> acc
      end
    end
  end
end

program = HandheldHalting.read_input("08_handheld_halting.input")
{acc_1, :loop} = HandheldHalting.run_until_loop(program, 0, 0, MapSet.new())
IO.puts("Part 1: #{acc_1}")

acc_2 = HandheldHalting.brute_force_fix(program, 0)
IO.puts("Part 2: #{acc_2}")
