defmodule JurassicJigsaw do
  @size 12
  @num_cubes 144
  @monster_body [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]

  def tile_borders(tile_with_borders) do
    top = List.first(tile_with_borders)
    bottom = List.last(tile_with_borders)
    left = Enum.map(tile_with_borders, &List.first/1)
    right = Enum.map(tile_with_borders, &List.last/1)

    [top, right, bottom, left]
  end

  def tile_image(tile_with_borders) do
    tile_with_borders
    |> Enum.slice(1..-2)
    |> Enum.map(fn row -> Enum.slice(row, 1..-2) end)
  end

  def parse_tile(block) do
    [header | rest] = String.split(block, "\n")
    [_, tile_num, _] = String.split(header, [" ", ":"])
    tile = Enum.map(rest, &to_charlist/1)

    {
      String.to_integer(tile_num),
      tile_borders(tile),
      tile_image(tile)
    }
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.map(&parse_tile/1)
    |> Enum.reduce({%{}, %{}}, fn {num, borders, image}, {acc1, acc2} ->
      {Map.put(acc1, num, borders), Map.put(acc2, num, image)}
    end)
  end

  def all_other_borders(tile_num, tiles_borders) do
    normal = Map.values(Map.delete(tiles_borders, tile_num))

    flipped =
      Enum.map(normal, fn tile_borders ->
        Enum.map(tile_borders, fn border -> Enum.reverse(border) end)
      end)

    Enum.reduce(normal ++ flipped, [], fn tile_borders, acc -> tile_borders ++ acc end)
  end

  def is_corner?({num, tile_borders}, tiles_borders) do
    all_borders = all_other_borders(num, tiles_borders)

    tile_borders
    |> Enum.map(fn border -> border not in all_borders end)
    |> Enum.count(& &1) == 2
  end

  def corners(tiles_borders) do
    Enum.filter(Map.to_list(tiles_borders), fn {num, tile_borders} ->
      is_corner?({num, tile_borders}, tiles_borders)
    end)
    |> Enum.map(&elem(&1, 0))
  end

  def flip_borders(borders) do
    Enum.map(borders, &Enum.reverse/1)
  end

  def border_matches_tile?(_border, [], []) do
    {false, nil}
  end

  def border_matches_tile?(
        border,
        [dir | rest_dirs],
        [tile_border | rest_tile_borders]
      ) do
    if border == tile_border do
      {true, dir}
    else
      border_matches_tile?(border, rest_dirs, rest_tile_borders)
    end
  end

  def border_matches_tile?(border, {_num, tile_borders}) do
    border_matches_tile?(
      border,
      [:top, :right, :bottom, :left, :ftop, :fright, :fbottom, :fleft],
      tile_borders ++ flip_borders(tile_borders)
    )
  end

  def border_match(_border, []) do
    nil
  end

  def border_match(border, [tile | rest_tiles]) do
    case border_matches_tile?(border, tile) do
      {true, dir} ->
        {num, _} = tile
        {num, dir}

      {false, _} ->
        border_match(border, rest_tiles)
    end
  end

  def tile_matches({num, borders}, other_tiles) do
    Enum.zip_reduce(
      [
        [:top, :right, :bottom, :left, :ftop, :fright, :fbottom, :fleft],
        borders ++ flip_borders(borders)
      ],
      %{},
      fn [o, b], acc ->
        case border_match(b, other_tiles) do
          nil -> acc
          match -> Map.put(acc, {num, o}, match)
        end
      end
    )
  end

  def all_matches(tiles_borders) do
    tiles_borders
    |> Map.to_list()
    |> Enum.reduce(%{}, fn {tile_num, tile_borders}, acc ->
      other_tiles = Map.to_list(Map.delete(tiles_borders, tile_num))
      tile_matches({tile_num, tile_borders}, other_tiles)
      Map.merge(acc, tile_matches({tile_num, tile_borders}, other_tiles))
    end)
  end

  def print(picture) do
    Enum.each(picture, &IO.puts(&1))
  end

  def adjust_orientation(:right, match_dir_on_left) do
    # Expanding from a block to the left. If the matching tile border is
    # match_dir_on_left, the orientation of the matching tile is the given by
    # the returned dictionary. It's like this because there's only 8 possible
    # results after turning/flipping an originally top/right/bottom/left cube
    case match_dir_on_left do
      :left -> %{top: :top, right: :right, bottom: :bottom, left: :left}
      :bottom -> %{top: :fleft, right: :top, bottom: :fright, left: :bottom}
      :fright -> %{top: :fbottom, right: :fleft, bottom: :ftop, left: :fright}
      :ftop -> %{top: :right, right: :fbottom, bottom: :left, left: :ftop}
      :fleft -> %{top: :bottom, right: :fright, bottom: :top, left: :fleft}
      :top -> %{top: :left, right: :bottom, bottom: :right, left: :top}
      :right -> %{top: :ftop, right: :left, bottom: :fbottom, left: :right}
      :fbottom -> %{top: :fright, right: :ftop, bottom: :fleft, left: :fbottom}
    end
  end

  def adjust_orientation(:bottom, match_dir_on_top) do
    case match_dir_on_top do
      :top -> %{top: :top, right: :right, bottom: :bottom, left: :left}
      :fleft -> %{top: :fleft, right: :top, bottom: :fright, left: :bottom}
      :fbottom -> %{top: :fbottom, right: :fleft, bottom: :ftop, left: :fright}
      :right -> %{top: :right, right: :fbottom, bottom: :left, left: :ftop}
      :bottom -> %{top: :bottom, right: :fright, bottom: :top, left: :fleft}
      :left -> %{top: :left, right: :bottom, bottom: :right, left: :top}
      :ftop -> %{top: :ftop, right: :left, bottom: :fbottom, left: :right}
      :fright -> %{top: :fright, right: :ftop, bottom: :fleft, left: :fbottom}
    end
  end

  def turn_90(image) do
    image
    |> Enum.zip()
    |> Enum.map(&Tuple.to_list/1)
    |> Enum.map(&Enum.reverse/1)
  end

  def flip(image, :x) do
    Enum.reverse(image)
  end

  def flip(image, :y) do
    Enum.map(image, &Enum.reverse/1)
  end

  def adjust_cube(image, orientator) do
    case orientator[:left] do
      :left -> image
      :top -> image |> turn_90() |> flip(:y)
      :right -> image |> flip(:y)
      :bottom -> image |> turn_90()
      :fleft -> image |> flip(:x)
      :ftop -> image |> turn_90() |> turn_90() |> turn_90()
      :fright -> image |> turn_90() |> turn_90()
      :fbottom -> image |> turn_90() |> flip(:x)
    end
  end

  @doc "Appends a cube to the right side of an 8-row picture"
  def append_at_end(picture, cube) do
    Enum.zip_with([picture, cube], &List.flatten/1)
  end

  @doc """
  Adds a cube to an incomplete picture that has
  - possibly a multiple of 8 complete rows
  - possibly 8 incomplete rows
  """
  def add_cube(picture, cube_num, cube) do
    if rem(cube_num, @size) != 0 do
      first_cube_row = length(picture) - 8

      if first_cube_row == 0 do
        append_at_end(picture, cube)
      else
        full_rows = Enum.slice(picture, 0..(first_cube_row - 1))
        rest = Enum.slice(picture, first_cube_row..-1)
        full_rows ++ append_at_end(rest, cube)
      end
    else
      picture ++ cube
    end
  end

  def big_picture(@num_cubes, picture, _cubes_orientations, _matches, _images) do
    picture
  end

  def big_picture(i, picture, cubes_orientations, matches, images) do
    {cube_to_expand_from, dir_to_expand_from} =
      if rem(i, @size) != 0 do
        {i - 1, :right}
      else
        {i - @size, :bottom}
      end

    {from_tile_num, from_orientator} = cubes_orientations[cube_to_expand_from]
    from_real_dir = from_orientator[dir_to_expand_from]
    {to_tile_num, to_real_dir} = matches[{from_tile_num, from_real_dir}]
    to_orientator = adjust_orientation(dir_to_expand_from, to_real_dir)
    cube_to_add = adjust_cube(images[to_tile_num], to_orientator)

    big_picture(
      i + 1,
      add_cube(picture, i, cube_to_add),
      Map.put(cubes_orientations, i, {to_tile_num, to_orientator}),
      matches,
      images
    )
  end

  def big_picture(borders, images, corners) do
    matches = JurassicJigsaw.all_matches(borders)
    top_left_corner = choose_corner(corners, matches)

    big_picture(
      1,
      images[top_left_corner],
      %{0 => {top_left_corner, %{top: :top, right: :right, bottom: :bottom, left: :left}}},
      matches,
      images
    )
  end

  def choose_corner(corners, matches) do
    Enum.find(corners, fn tile ->
      Map.has_key?(matches, {tile, :right}) and Map.has_key?(matches, {tile, :bottom})
    end)
  end

  def monster_body_line?([line, indexes]) do
    Enum.all?(Enum.map(indexes, fn i -> Enum.at(line, i) == ?\# end))
  end

  def monster?(sea_block) do
    [sea_block, @monster_body]
    |> Enum.zip_with(fn pair -> monster_body_line?(pair) end)
    |> Enum.all?()
  end

  def find_inner([l1, _l2, _l3], count) when length(l1) < 20 do
    count
  end

  def find_inner(lines, count) do
    if monster?(Enum.map(lines, fn line -> Enum.slice(line, 0..19) end)) do
      find_inner(Enum.map(lines, &tl/1), count + 1)
    else
      find_inner(Enum.map(lines, &tl/1), count)
    end
  end

  def find_outter([line1 | [line2 | [line3 | rest]]], count) do
    find_outter(
      [line2 | [line3 | rest]],
      count + find_inner([line1, line2, line3], 0)
    )
  end

  def find_outter(picture, count) when length(picture) < 3 do
    count
  end

  def find_sea_monsters(picture) do
    turned_90 = picture |> turn_90()
    turned_180 = turned_90 |> turn_90()
    turned_270 = turned_180 |> turn_90()

    possible_pictures = [
      picture,
      turned_90,
      turned_180,
      turned_270
      # tried without flipping first :)
    ]

    Enum.reduce(
      Enum.map(possible_pictures, &find_outter(&1, 0)),
      fn count, acc -> count + acc end
    )
  end

  def count_hashes(picture) do
    Enum.reduce(
      Enum.map(picture, fn line -> Enum.count(line, fn c -> c == ?\# end) end),
      fn count, acc -> count + acc end
    )
  end
end

{borders, images} = JurassicJigsaw.read_input("20_jurassic_jigsaw.input")
corners = JurassicJigsaw.corners(borders) |> IO.inspect(label: "corners")

part_1 = Enum.product(corners)
IO.puts("Part 1: #{part_1}")

picture = JurassicJigsaw.big_picture(borders, images, corners)
num_monsters = JurassicJigsaw.find_sea_monsters(picture)
part_2 = JurassicJigsaw.count_hashes(picture) - num_monsters * 15
IO.puts("Part 2: #{part_2}")
