package main

import "testing"

const testInputFile = "10_syntax_scoring_test.input"

func TestSolvePart1(t *testing.T) {
	expected := 26397
	got := solvePart1(testInputFile)
	if got != expected {
		t.Errorf("Part 1: Expected %d, but got %d.", expected, got)
	}
}

func TestSolvePart2(t *testing.T) {
	expected := 288957
	got := solvePart2(testInputFile)
	if got != expected {
		t.Errorf("Part 2: Expected %d, but got %d.", expected, got)
	}
}
