# https://exercism.io/my/solutions/de82cfa6f14642ea937c0fb134a280ef

defmodule RomanNumerals do
  @symbols {["I", "V"], ["X", "L"], ["C", "D"], ["M", "V"]}

  @spec one_digit({pos_integer, pos_integer}) :: String.t()
  defp one_digit({n, power}) do
    [s1, s5] = elem(@symbols, power)

    case n do
      n when n <= 3 ->
        String.duplicate(s1, n)

      n when n >= 4 and n <= 8 ->
        String.duplicate(s1, max(5 - n, 0)) <> s5 <> String.duplicate(s1, max(n - 5, 0))

      9 ->
        [s5, _] = elem(@symbols, power + 1)
        s1 <> s5
    end
  end

  @doc """
  Convert the number to a roman number.
  """
  @spec numeral(pos_integer) :: String.t()
  def numeral(number) do
    digits = Integer.digits(number)
    powers = Enum.to_list((length(digits) - 1)..0)
    Enum.zip([digits, powers]) |> Enum.map_join(&one_digit/1)
  end
end
