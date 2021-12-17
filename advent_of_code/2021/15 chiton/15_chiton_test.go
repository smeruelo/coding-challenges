package main

import "testing"

const testInputFile = "15_chiton_test.input"

func TestSolvePart1(t *testing.T) {
	expected := 40
	got := solvePart1(testInputFile)
	if got != expected {
		t.Errorf("Part 1: Expected %d, but got %d.", expected, got)
	}
}

func TestSolvePart2(t *testing.T) {
	expected := 315
	got := solvePart2(testInputFile)
	if got != expected {
		t.Errorf("Part 2: Expected %d, but got %d.", expected, got)
	}
}
