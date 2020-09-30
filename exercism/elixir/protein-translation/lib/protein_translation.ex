# https://exercism.io/my/solutions/1852f6b45ec3406a9dfb6e08f6a99f36

defmodule ProteinTranslation do
  @proteins %{
    "UGU" => "Cysteine",
    "UGC" => "Cysteine",
    "UUA" => "Leucine",
    "UUG" => "Leucine",
    "AUG" => "Methionine",
    "UUU" => "Phenylalanine",
    "UUC" => "Phenylalanine",
    "UCU" => "Serine",
    "UCC" => "Serine",
    "UCA" => "Serine",
    "UCG" => "Serine",
    "UGG" => "Tryptophan",
    "UAU" => "Tyrosine",
    "UAC" => "Tyrosine",
    "UAA" => "STOP",
    "UAG" => "STOP",
    "UGA" => "STOP"
  }

  @doc """
  Given an RNA string, return a list of proteins specified by codons, in order.
  """
  @spec of_rna(String.t()) :: {atom, list(String.t())}
  def of_rna(rna) do
    codons = List.flatten(Regex.scan(~r/.../, rna))
    of_rna(codons, [])
  end

  @spec of_rna(list(String.t()), list(String.t())) :: {atom, list(String.t())}
  def of_rna([], proteins), do: {:ok, Enum.reverse(proteins)}

  def of_rna([head | tail], proteins) do
    case of_codon(head) do
      {:ok, "STOP"} -> {:ok, Enum.reverse(proteins)}
      {:ok, protein} -> of_rna(tail, [protein | proteins])
      {:error, _} -> {:error, "invalid RNA"}
    end
  end

  @doc """
  Given a codon, return the corresponding protein
  """
  @spec of_codon(String.t()) :: {atom, String.t()}
  def of_codon(codon) do
    case @proteins[codon] do
      nil -> {:error, "invalid codon"}
      protein -> {:ok, protein}
    end
  end
end
