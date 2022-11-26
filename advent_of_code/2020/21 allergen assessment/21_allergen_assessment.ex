defmodule AllergenAssessment do
  def read_input(filename) do
    {:ok, data} = File.read(filename)

    data
    |> String.split("\n")
    |> Enum.map(&parse_food(&1))
    |> Enum.reduce({%{}, %{}}, fn {ing, aller}, {ingredients, allergens} ->
      {
        count_ingredients(ingredients, ing),
        allergen_possibilities(allergens, ing, aller)
      }
    end)
  end

  def parse_food(line) do
    [left, right] = String.split(line, " (contains ")

    {
      String.split(left, " "),
      String.split(String.slice(right, 0..-2), ", ")
    }
  end

  def count_ingredients(ingredients, ing) do
    Enum.reduce(ing, ingredients, fn ing, ingredients ->
      Map.update(ingredients, ing, 1, fn i -> i + 1 end)
    end)
  end

  def allergen_possibilities(potential_allergens, ing, aller) do
    Enum.reduce(aller, potential_allergens, fn a, acc ->
      Map.update(acc, a, MapSet.new(ing), fn v ->
        MapSet.intersection(v, MapSet.new(ing))
      end)
    end)
  end

  def no_allergens(ingredients, potential_allergens) do
    with_allergens =
      Enum.reduce(Map.values(potential_allergens), MapSet.new(), fn s, acc ->
        MapSet.union(s, acc)
      end)

    Enum.reduce(Map.keys(ingredients), 0, fn i, count ->
      if i not in with_allergens do
        count + ingredients[i]
      else
        count
      end
    end)
  end

  def remove_ing(potential_allergens, allergen, ingredient) do
    potential_allergens
    |> Map.keys()
    |> Enum.reduce(potential_allergens, fn a, updated_potential_allergens ->
      Map.update(updated_potential_allergens, a, updated_potential_allergens[a], fn ms ->
        MapSet.delete(ms, ingredient)
      end)
    end)
    |> Map.delete(allergen)
  end

  def identify_allergens(potential_allergens) do
    identify_allergens(potential_allergens, %{})
  end

  def identify_allergens(potential_allergens, identified_allergens)
      when potential_allergens == %{} do
    identified_allergens
  end

  def identify_allergens(potential_allergens, identified_allergens) do
    {aller, ms} =
      Enum.find(Map.to_list(potential_allergens), fn {_, ms} -> MapSet.size(ms) == 1 end)

    [ing] = MapSet.to_list(ms)

    identify_allergens(
      remove_ing(potential_allergens, aller, ing),
      Map.put(identified_allergens, aller, ing)
    )
  end

  def cannonical(allergens) do
    allergens
    |> Map.keys()
    |> Enum.sort()
    |> Enum.map(fn aller -> allergens[aller] end)
    |> Enum.join(",")
  end
end

{ingredients, potential_allergens} = AllergenAssessment.read_input("21_allergen_assessment.input")

part_1 = AllergenAssessment.no_allergens(ingredients, potential_allergens)
IO.puts("Part 1: #{part_1}")

identified_allergens = AllergenAssessment.identify_allergens(potential_allergens)
part_2 = AllergenAssessment.cannonical(identified_allergens)
IO.puts("Part 2: #{part_2}")
