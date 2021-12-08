package main

import "testing"

const testInputFile = "08_seven_segment_search_test.input"

func TestSolvePart1(t *testing.T) {
	expected := 26
	got := solvePart1(testInputFile)
	if got != expected {
		t.Errorf("Part 1: Expected %d, but got %d.", expected, got)
	}
}

func TestSolvePart2(t *testing.T) {
	expected := 61229
	got := solvePart2(testInputFile)
	if got != expected {
		t.Errorf("Part 2: Expected %d, but got %d.", expected, got)
	}
}
