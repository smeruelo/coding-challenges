# https://exercism.io/my/solutions/2966a9d0d2bf4f00bced521ddaebb15c

defmodule Bob do
  @spec is_question?(String.t()) :: boolean()
  defp is_question?(sentence) do
    String.match?(sentence, ~r/\?[[:blank:]]*$/)
  end

  @spec is_yell?(String.t()) :: boolean()
  defp is_yell?(sentence) do
    String.match?(sentence, ~r/[[:upper:]+]/) and not String.match?(sentence, ~r/[[:lower:]+]/)
  end

  @spec is_empty?(String.t()) :: boolean()
  defp is_empty?(sentence) do
    not String.match?(sentence, ~r/[[:alnum:]]+/)
  end

  @spec hey(String.t()) :: String.t()
  def hey(input) do
    cond do
      is_question?(input) and is_yell?(input) -> "Calm down, I know what I'm doing!"
      is_question?(input) -> "Sure."
      is_yell?(input) -> "Whoa, chill out!"
      is_empty?(input) -> "Fine. Be that way!"
      true -> "Whatever."
    end
  end
end
