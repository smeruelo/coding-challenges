defmodule ReportRepair do

def read_input(filename) do
	{:ok, data} = File.read(filename)

	String.split(data, "\n")
	|> Enum.map(&String.to_integer/1)
end

def find_complementary_pair(numbers, sum) do
  with ([head | tail] when tail != []) <- numbers do
	complementary = sum - head
	if complementary in tail do
	  [head, complementary]
	else
	  find_complementary_pair(tail, sum)
	end
  else
	[_head] -> :not_found
  end
end

def find_complementary_threesome(numbers, sum) do
  [head | tail] = numbers
  rest = sum - head
  case find_complementary_pair(tail, rest) do
	[num2, num3] -> [head, num2, num3]
	:not_found -> find_complementary_threesome(tail, sum)
  end
end

end

entries = ReportRepair.read_input("01_report_repair.input")

[num1, num2] = ReportRepair.find_complementary_pair(entries, 2020)
IO.puts("Part 1: #{num1 * num2}")

[num1, num2, num3] = ReportRepair.find_complementary_threesome(entries, 2020)
IO.puts("Part 1: #{num1 * num2 * num3}")
