defmodule RockPaperScissors do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&String.split(&1, " "))
  end

  def translate_round([shape_1, shape_2], dict_1, dict_2) do
    [dict_1[shape_1], dict_2[shape_2]]
  end

  def translate_game(game, dict_1, dict_2) do
    Enum.map(game, &translate_round(&1, dict_1, dict_2))
  end

  def shape_score(:rock), do: 1
  def shape_score(:paper), do: 2
  def shape_score(:scissors), do: 3

  def outcome_score(:lose), do: 0
  def outcome_score(:draw), do: 3
  def outcome_score(:win), do: 6

  def rock_paper_scissors([shape, shape]), do: :draw
  def rock_paper_scissors([:rock, :paper]), do: :win
  def rock_paper_scissors([:rock, :scissors]), do: :lose
  def rock_paper_scissors([:paper, :rock]), do: :lose
  def rock_paper_scissors([:paper, :scissors]), do: :win
  def rock_paper_scissors([:scissors, :rock]), do: :win
  def rock_paper_scissors([:scissors, :paper]), do: :lose

  def round_score([shape_1, shape_2]) do
    shape_score(shape_2) + outcome_score(rock_paper_scissors([shape_1, shape_2]))
  end

  def play(game) do
    Enum.sum(Enum.map(game, &round_score/1))
  end

  def reverse_rock_paper_scissors([shape, :draw]), do: shape
  def reverse_rock_paper_scissors([:rock, :win]), do: :paper
  def reverse_rock_paper_scissors([:rock, :lose]), do: :scissors
  def reverse_rock_paper_scissors([:paper, :win]), do: :scissors
  def reverse_rock_paper_scissors([:paper, :lose]), do: :rock
  def reverse_rock_paper_scissors([:scissors, :win]), do: :rock
  def reverse_rock_paper_scissors([:scissors, :lose]), do: :paper

  def reverse_play(game) do
    Enum.sum(
      Enum.map(game, fn [shape_1, outcome] ->
        shape_2 = reverse_rock_paper_scissors([shape_1, outcome])
        round_score([shape_1, shape_2])
      end)
    )
  end
end

game = RockPaperScissors.read_input("02_rock_paper_scissors.input")
dict_player_1 = %{"A" => :rock, "B" => :paper, "C" => :scissors}

game_1 =
  RockPaperScissors.translate_game(
    game,
    dict_player_1,
    %{"X" => :rock, "Y" => :paper, "Z" => :scissors}
  )

score_1 = RockPaperScissors.play(game_1)
IO.puts("Part 1: #{score_1}")

game_2 =
  RockPaperScissors.translate_game(
    game,
    dict_player_1,
    %{"X" => :lose, "Y" => :draw, "Z" => :win}
  )

score_2 = RockPaperScissors.reverse_play(game_2)
IO.puts("Part 2: #{score_2}")
