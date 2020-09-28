# https://exercism.io/my/solutions/dafbf740fdfb4091a0912bd816df7d4d

defmodule SecretHandshake do
  @actions ["jump", "close your eyes", "double blink", "wink"]

  @doc """
  Determine the actions of a secret handshake based on the binary
  representation of the given `code`.

  If the following bits are set, include the corresponding action in your list
  of commands, in order from lowest to highest.

  1 = wink
  10 = double blink
  100 = close your eyes
  1000 = jump

  10000 = Reverse the order of the operations in the secret handshake
  """
  @spec commands(code :: integer) :: list(String.t())
  def commands(code) do
    bin_code = Integer.to_string(code, 2)

    action_bits =
      bin_code
      |> String.slice(-min(4, String.length(bin_code)), 4)
      |> String.pad_leading(4, "0")
      |> String.to_charlist()

    reverse_if_needed = fn lst ->
      if code >= 16 and String.at(bin_code, -5) == "1", do: lst, else: Enum.reverse(lst)
    end

    List.zip([action_bits, @actions])
    |> Enum.map(fn {bit, action} -> if bit == ?1, do: action end)
    |> Enum.reject(&is_nil/1)
    |> reverse_if_needed.()
  end
end
