# https://exercism.io/my/solutions/78723a69405a4c7d85051bc817058f23

defmodule RotationalCipher do
  @alphabet 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  @lower "abcdefghijklmnopqrstuvwxyz"
  @upper "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  @spec trans_table(shift :: Integer.t()) :: Map.t()
  defp trans_table(shift) do
    lower_rotated = String.slice(@lower, shift..-1) <> String.slice(@lower, 0..(shift - 1))
    upper_rotated = String.slice(@upper, shift..-1) <> String.slice(@upper, 0..(shift - 1))
    alphabet_rotated = String.to_charlist(lower_rotated <> upper_rotated)
    Map.new(List.zip([@alphabet, alphabet_rotated]))
  end

  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """
  @spec rotate(text :: String.t(), shift :: integer) :: String.t()
  def rotate(text, shift) do
    trans = trans_table(shift)
    text |> String.to_charlist() |> Enum.map(&Map.get(trans, &1, &1)) |> List.to_string()
  end
end
