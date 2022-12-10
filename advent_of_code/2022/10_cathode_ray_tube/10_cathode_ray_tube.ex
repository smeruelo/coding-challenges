defmodule CathodeRayTube do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_instruction/1)
  end

  def parse_instruction(line) do
    tokens = String.split(line, " ")

    case hd(tokens) do
      "noop" -> {:noop}
      "addx" -> {:addx, String.to_integer(Enum.at(tokens, 1))}
    end
  end

  def simulate([], _cycle, _register, register_history) do
    register_history
  end

  def simulate([{:noop} | rest], cycle, register, register_history) do
    simulate(rest, cycle + 1, register, Map.put(register_history, cycle, register))
  end

  def simulate([{:addx, x} | rest], cycle, register, register_history) do
    register_history = Map.put(register_history, cycle, register)
    simulate(rest, cycle + 2, register + x, Map.put(register_history, cycle + 1, register))
  end

  def simulate(instructions) do
    simulate(instructions, 1, 1, %{})
  end

  def signal_strenth(cycle, registry_history) do
    cycle * Map.get(registry_history, cycle, 0)
  end

  def sum_of_strengths(registry_history) do
    -20..map_size(registry_history)//40
    |> Enum.map(&signal_strenth(&1, registry_history))
    |> Enum.sum()
  end

  def draw(241, screen, _registry_history) do
    screen
  end

  def draw(cycle, screen, registry_history) do
    pixel = rem(cycle - 1, 40)
    registry = registry_history[cycle]
    sprite_positions = [registry - 1, registry, registry + 1]

    if pixel in sprite_positions do
      draw(cycle + 1, screen <> "#", registry_history)
    else
      draw(cycle + 1, screen <> ".", registry_history)
    end
  end

  def draw(registry_history) do
    draw(1, "", registry_history)
  end
end

instructions = CathodeRayTube.read_input("10_cathode_ray_tube.input")
registry_history = CathodeRayTube.simulate(instructions)

part_1 = CathodeRayTube.sum_of_strengths(registry_history)
IO.puts("Part 1: #{part_1}")

IO.puts("Part 2:")

CathodeRayTube.draw(registry_history)
|> to_charlist()
|> Enum.chunk_every(40)
|> Enum.each(&IO.puts/1)
