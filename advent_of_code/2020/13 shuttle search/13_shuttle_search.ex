defmodule ShuttleSearch do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    [earliest, other] = data |> String.split("\n")

    departures =
      other
      |> String.split(",")
      |> Enum.map(fn x ->
        if x == "x" do
          x
        else
          String.to_integer(x)
        end
      end)

    {String.to_integer(earliest), departures}
  end

  def nearest_factor(earliest, departure) do
    d = div(earliest, departure)

    if rem(earliest, departure) == 0 do
      d
    else
      d + 1
    end
  end

  def result({departure, bus}, earliest) do
    (departure - earliest) * bus
  end

  def part_1(earliest, departures) do
    departures
    |> Enum.filter(fn x -> x != "x" end)
    |> Enum.map(fn x -> {x * nearest_factor(earliest, x), x} end)
    |> Enum.sort()
    |> List.first()
    |> result(earliest)
  end

  def egcd(_a, 0), do: {1, 0}

  def egcd(a, b) do
    {x, y} = egcd(b, rem(a, b))
    {y, x - div(a, b) * y}
  end

  def mod_inv(a, b) do
    elem(egcd(a, b), 0)
  end

  def part_2(departures) do
    # Chinese Remainder Theorem
    # (page 163 Laaksonen)
    buses_and_offsets =
      departures
      |> Enum.zip(0..(length(departures) - 1))
      |> Enum.filter(fn {x, _} -> x != "x" end)

    as = Enum.map(buses_and_offsets, fn {m, t} -> Integer.mod(-t, m) end)
    ms = Enum.map(buses_and_offsets, fn {m, _} -> m end)
    xs = Enum.map(ms, fn m -> div(Enum.product(ms), m) end)
    x_invs = Enum.zip_with(xs, ms, fn x, m -> mod_inv(x, m) end)

    [as, xs, x_invs]
    |> Enum.zip()
    |> Enum.map(fn {a, x, x_inv} -> a * x * x_inv end)
    |> Enum.sum()
    |> Integer.mod(Enum.product(ms))
  end
end

{earliest, departures} = ShuttleSearch.read_input("13_shuttle_search.input")

result_1 = ShuttleSearch.part_1(earliest, departures)
IO.puts("Part 1: #{result_1}")

result_2 = ShuttleSearch.part_2(departures)
IO.puts("Part 2: #{result_2}")
