defmodule NoSpaceLeftOnDevice do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
  end

  def parse_line(line) do
    if String.starts_with?(line, "$") do
      parse_command(line)
    else
      parse_content(line)
    end
  end

  def parse_command(line) do
    ["$" | tokens] = String.split(line, " ")

    case hd(tokens) do
      "ls" ->
        [:command, :ls]

      "cd" ->
        case tl(tokens) do
          [".."] -> [:command, :cd_back]
          [dir_name] -> [:command, :cd, dir_name]
        end
    end
  end

  def parse_content(line) do
    case String.split(line, " ") do
      ["dir", dir_name] -> [:dir, dir_name]
      [size, file_name] -> [:file, String.to_integer(size), file_name]
    end
  end

  def build_filesystem([], fs, _current_dir) do
    fs
  end

  def build_filesystem([line | rest], fs, current_dir) do
    case line do
      [:command, :cd, dir_name] ->
        build_filesystem(rest, fs, path([current_dir, dir_name]))

      [:command, :cd_back] ->
        build_filesystem(rest, fs, remove_last(current_dir))

      [:command, :ls] ->
        populate_dir(rest, fs, current_dir)
    end
  end

  def build_filesystem(input) do
    build_filesystem(tl(input), %{"" => {[], 0}}, "")
  end

  def populate_dir([], fs, current_dir) do
    build_filesystem([], fs, current_dir)
  end

  def populate_dir([[:command | _] | _] = rest, fs, current_dir) do
    build_filesystem(rest, fs, current_dir)
  end

  def populate_dir([[:dir, dir_name] | rest], fs, current_dir) do
    {contents, size} = fs[current_dir]
    dir_path = path([current_dir, dir_name])
    fs = Map.put(fs, dir_path, {[], 0})

    populate_dir(
      rest,
      %{fs | current_dir => {[[:dir, dir_path] | contents], size}},
      current_dir
    )
  end

  def populate_dir([[:file, _, _] = file | rest], fs, current_dir) do
    {contents, size} = fs[current_dir]

    populate_dir(
      rest,
      %{fs | current_dir => {[file | contents], size}},
      current_dir
    )
  end

  def path(dirs), do: Enum.join(dirs, "/")

  def remove_last(dir) do
    dir
    |> String.split("/")
    |> Enum.slice(0..-2)
    |> Enum.join("/")
  end

  def total_size([], _fs, acc) do
    acc
  end

  def total_size([item | rest], fs, acc) do
    case item do
      [:file, size, _] ->
        total_size(rest, fs, acc + size)

      [:dir, dir_path] ->
        total_size(
          rest,
          fs,
          acc + total_size(dir_path, fs)
        )
    end
  end

  def total_size(dir, fs) do
    {contents, _} = fs[dir]
    total_size(contents, fs, 0)
  end

  def part_1(fs) do
    fs
    |> Map.keys()
    |> Enum.map(&total_size(&1, fs))
    |> Enum.filter(fn x -> x <= 100_000 end)
    |> Enum.sum()
  end

  def part_2(fs) do
    space_needed = 30_000_000 - (70_000_000 - total_size("", fs))

    fs
    |> Map.keys()
    |> Enum.map(&total_size(&1, fs))
    |> Enum.filter(fn x -> x >= space_needed end)
    |> Enum.sort()
    |> hd()
  end
end

input = NoSpaceLeftOnDevice.read_input("07_no_space_left_on_device.input")
filesystem = NoSpaceLeftOnDevice.build_filesystem(input)

part_1 = NoSpaceLeftOnDevice.part_1(filesystem)
IO.puts("Part 1: #{part_1}")

part_2 = NoSpaceLeftOnDevice.part_2(filesystem)
IO.puts("Part 2: #{part_2}")
