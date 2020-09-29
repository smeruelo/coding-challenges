# https://exercism.io/my/solutions/2966a9d0d2bf4f00bced521ddaebb15c

defmodule Bob do
  @spec is_question?(String.t()) :: boolean()
  def is_question?(s), do: String.ends_with?(s, "?")

  @spec is_yell?(String.t()) :: boolean()
  defp is_yell?(s), do: String.upcase(s) == s and String.downcase(s) != s

  @spec is_empty?(String.t()) :: boolean()
  defp is_empty?(s), do: s == ""

  @spec hey(String.t()) :: String.t()
  def hey(input) do
    trimmed = String.trim(input)

    cond do
      is_question?(trimmed) and is_yell?(trimmed) -> "Calm down, I know what I'm doing!"
      is_question?(trimmed) -> "Sure."
      is_yell?(trimmed) -> "Whoa, chill out!"
      is_empty?(trimmed) -> "Fine. Be that way!"
      true -> "Whatever."
    end
  end
end
