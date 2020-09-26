# https://exercism.io/my/solutions/6a447d0395294e1fab9d686cfc8f6801

defmodule RnaTranscription do
  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RnaTranscription.to_rna('ACTG')
  'UGAC'
  """
  @spec to_rna([char]) :: [char]
  def to_rna(dna) do
    trans = %{?A => ?U, ?C => ?G, ?G => ?C, ?T => ?A}
    Enum.map(dna, fn c -> trans[c] end)
  end
end
