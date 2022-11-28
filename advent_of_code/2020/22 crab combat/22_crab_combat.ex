defmodule CrabCombat do
  def parse_deck(block) do
    block
    |> String.split("\n")
    |> tl()
    |> Enum.map(&String.to_integer/1)
  end

  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n\n")
    |> Enum.map(&parse_deck/1)
  end

  def collect_cards(deck, card) do
    tl(deck) ++ [hd(deck), card]
  end

  def score(deck) do
    length(deck)..1
    |> Enum.zip_with(deck, fn x, y -> x * y end)
    |> Enum.sum()
  end

  def regular_combat(deck_1, []) do
    # IO.puts("Player 1 wins!")
    score(deck_1)
  end

  def regular_combat([], deck_2) do
    # IO.puts("Player 2 wins!")
    score(deck_2)
  end

  def regular_combat(deck_1, deck_2) do
    card_1 = hd(deck_1)
    card_2 = hd(deck_2)

    if card_1 > card_2 do
      regular_combat(collect_cards(deck_1, card_2), tl(deck_2))
    else
      regular_combat(tl(deck_1), collect_cards(deck_2, card_1))
    end
  end

  def new_deck(deck, n) do
    Enum.slice(deck, 1..n)
  end

  def game_to_str(deck_1, deck_2) do
    Enum.join(deck_1, ",") <> ":" <> Enum.join(deck_2, ",")
  end

  def recursive_combat(deck_1, [], _played_games) do
    {score(deck_1), :player_1}
  end

  def recursive_combat([], deck_2, _played_games) do
    {score(deck_2), :player_2}
  end

  def recursive_combat(deck_1, deck_2, played_games) do
    game = game_to_str(deck_1, deck_2)

    if game in played_games do
      {score(deck_1), :player_1}
    else
      played_games = MapSet.put(played_games, game)
      card_1 = hd(deck_1)
      card_2 = hd(deck_2)

      if length(deck_1) > card_1 and length(deck_2) > card_2 do
        case new_recursive_combat_game(new_deck(deck_1, card_1), new_deck(deck_2, card_2)) do
          {_, :player_1} ->
            recursive_combat(collect_cards(deck_1, card_2), tl(deck_2), played_games)

          {_, :player_2} ->
            recursive_combat(tl(deck_1), collect_cards(deck_2, card_1), played_games)
        end
      else
        if card_1 > card_2 do
          recursive_combat(collect_cards(deck_1, card_2), tl(deck_2), played_games)
        else
          recursive_combat(tl(deck_1), collect_cards(deck_2, card_1), played_games)
        end
      end
    end
  end

  def new_recursive_combat_game(deck_1, deck_2) do
    recursive_combat(deck_1, deck_2, MapSet.new())
  end
end

[deck_1, deck_2] = CrabCombat.read_input("22_crab_combat.input")
part_1 = CrabCombat.regular_combat(deck_1, deck_2)
IO.puts("Part 1: #{part_1}")

{score, _winner} = CrabCombat.new_recursive_combat_game(deck_1, deck_2)
IO.puts("Part 2: #{score}")
