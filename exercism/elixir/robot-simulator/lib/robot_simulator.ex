# https://exercism.io/my/solutions/2fdb20b632944a8ab6d168ae551396aa

defmodule RobotSimulator do
  defstruct [:direction, position: {}]
  @directions [:north, :east, :south, :west]

  @doc """
  Create a Robot Simulator given an initial direction and position.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec create(direction :: atom, position :: {integer, integer}) :: any
  def create(direction \\ :north, position \\ {0, 0}) do
    case {valid_direction?(direction), valid_position?(position)} do
      {true, true} -> %RobotSimulator{direction: direction, position: position}
      {false, _} -> {:error, "invalid direction"}
      {_, false} -> {:error, "invalid position"}
    end
  end

  @doc """
  Simulate the robot's movement given a string of instructions.

  Valid instructions are: "R" (turn right), "L", (turn left), and "A" (advance)
  """
  @spec simulate(robot :: any, instructions :: String.t()) :: any
  def simulate(robot, instructions) do
    instructions
    |> String.graphemes()
    |> Enum.reduce_while(robot, fn mov, r ->
      case mov do
        "R" -> {:cont, create(new_direction(r, :right), position(r))}
        "L" -> {:cont, create(new_direction(r, :left), position(r))}
        "A" -> {:cont, create(direction(r), new_position(r, :advance))}
        _ -> {:halt, {:error, "invalid instruction"}}
      end
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

  defp valid_position?({x, y}) when is_integer(x) and is_integer(y), do: true

  defp valid_position?(_), do: false

  defp valid_direction?(direction), do: Enum.member?(@directions, direction)

  defp new_direction(robot, _movement = :right) do
    case direction(robot) do
      :north -> :east
      :east -> :south
      :south -> :west
      :west -> :north
    end
  end

  defp new_direction(robot, _movement = :left) do
    case direction(robot) do
      :north -> :west
      :east -> :north
      :south -> :east
      :west -> :south
    end
  end

  defp new_position(robot, _movement = :advance) do
    {x, y} = position(robot)

    case direction(robot) do
      :north -> {x, y + 1}
      :east -> {x + 1, y}
      :south -> {x, y - 1}
      :west -> {x - 1, y}
    end
  end
end
