defmodule RobotSimulator do
  defstruct [:direction, position: {}]
  @valid_directions [:north, :east, :south, :west]
  @valid_movements ["R", "L", "A"]

  @doc """
  Create a Robot Simulator given an initial direction and position.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec create(direction :: atom, position :: {integer, integer}) :: any
  def create(direction \\ :north, {x, y} = position \\ {0, 0}) do
    unless Enum.member?(@valid_directions, direction), do: {:error, "invalid direction"}
    unless is_integer(x) and is_integer(y), do: {:error, "invalid position"}

    %RobotSimulator{direction: direction, position: position}
  end

  def create(_, _) do
    {:error, "invalid position"}
  end

  @doc """
  Simulate the robot's movement given a string of instructions.

  Valid instructions are: "R" (turn right), "L", (turn left), and "A" (advance)
  """
  @spec simulate(robot :: any, instructions :: String.t()) :: any
  def simulate(robot, instructions) do
    instructions
    |> String.graphemes()
    |> Enum.reduce(robot, fn movement, r ->
      unless Enum.member?(@valid_movements, movement),
        do: {:error, "invalid instruction #{movement}"}

      new_dir = new_direction(direction(r), movement)
      create(new_dir, new_position(position(r), new_dir))
    end)
  end

  @doc """
  Return the robot's direction.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec direction(robot :: any) :: atom
  def direction(robot) do
    robot.direction
  end

  @doc """
  Return the robot's position.
  """
  @spec position(robot :: any) :: {integer, integer}
  def position(robot) do
    robot.position
  end

  defp new_direction(current_direction, _movement = "R") do
    case current_direction do
      :north -> :east
      :east -> :south
      :south -> :west
      :west -> :north
    end
  end

  defp new_direction(current_direction, _movement = "L") do
    case current_direction do
      :north -> :west
      :east -> :north
      :south -> :east
      :west -> :south
    end
  end

  defp new_direction(current_direction, _movement) do
    current_direction
  end

  defp new_position(current_position, direction) do
    {x, y} = current_position

    case direction do
      :north -> {x, y + 1}
      :east -> {x + 1, y}
      :south -> {x, y - 1}
      :west -> {x - 1, y}
    end
  end
end
