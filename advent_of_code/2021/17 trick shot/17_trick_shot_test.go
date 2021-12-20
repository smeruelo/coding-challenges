package main

import (
	"testing"
)

func TestSolvePart1(t *testing.T) {
	expected := 45
	got := solvePart1(area{minX: 20, maxX: 30, minY: -10, maxY: -5})
	if got != expected {
		t.Errorf("Part 1: Expected %d, but got %d.", expected, got)
	}
}

func TestSolvePart2(t *testing.T) {
	expected := 112
	got := solvePart2(area{minX: 20, maxX: 30, minY: -10, maxY: -5})
	if got != expected {
		t.Errorf("Part 2: Expected %d, but got %d.", expected, got)
	}
}
