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
    |> count_words(%{})
  end

  @spec count_words([String.t()], map) :: map
  defp count_words(words, counter) do
    case words do
      [] -> counter
      [head | tail] -> count_words(tail, Map.update(counter, head, 1, fn x -> x + 1 end))
    end
  end
end
