package main

import "testing"

const testInputFile = "14_extended_polymerization_test.input"

func TestSolvePart1(t *testing.T) {
	expected := 1588
	got := solvePart1(testInputFile)
	if got != expected {
		t.Errorf("Part 1: Expected %d, but got %d.", expected, got)
	}
}

func TestSolvePart2(t *testing.T) {
	expected := 2188189693529
	got := solvePart2(testInputFile)
	if got != expected {
		t.Errorf("Part 2: Expected %d, but got %d.", expected, got)
	}
}
