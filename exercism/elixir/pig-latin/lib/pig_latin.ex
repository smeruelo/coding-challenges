# https://exercism.io/my/solutions/5eab678179104a0799d9aefe7c881615

defmodule PigLatin do
  @consonants_3 ["squ"]
  @consonants_2 ["qu"]
  @consonants_1 String.graphemes("bcdfghjklmnpqrstvwxyz")
  @vowels_2 Enum.map(@consonants_1, &("x" <> &1)) ++ Enum.map(@consonants_1, &("y" <> &1))
  @vowels_1 ["a", "e", "i", "o", "u"]
  @consonant_cluster ~r/^[bcdfghjklmnpqrstvwxyz]*/

  @doc """
  Given a `phrase`, translate it a word at a time to Pig Latin.

  Words beginning with consonants should have the consonant moved to the end of
  the word, followed by "ay".

  Words beginning with vowels (aeiou) should have "ay" added to the end of the
  word.

  Some groups of letters are treated like consonants, including "ch", "qu",
  "squ", "th", "thr", and "sch".

  Some groups are treated like vowels, including "yt" and "xr".
  """
  @spec translate(phrase :: String.t()) :: String.t()
  def translate(phrase) do
    String.split(phrase)
    |> Enum.map(&translate_word/1)
    |> Enum.join(" ")
  end

  defp translate_word(word) do
    cluster = hd(Regex.run(@consonant_cluster, word))

    index =
      cond do
        String.starts_with?(word, @vowels_1) -> 0
        String.starts_with?(word, @vowels_2) -> 0
        String.starts_with?(word, @consonants_3) -> 3
        String.starts_with?(word, @consonants_2) -> 2
        true -> String.length(cluster)
      end

    String.slice(word, index..String.length(word)) <> String.slice(word, 0, index) <> "ay"
  end
end
