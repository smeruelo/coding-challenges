# https://exercism.io/my/solutions/5f8238ec135c478f8e2602905b477898

defmodule WordCount do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    sentence
    |> String.downcase()
    |> String.split(~r{[^[:alnum:]\-]}u, trim: true)
    |> Enum.frequencies()
  end
end
