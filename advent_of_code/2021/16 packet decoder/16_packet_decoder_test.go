package main

import (
	"testing"
)

var inputPart1 = []string{
	"38006F45291300",
	"EE00D40C823060",
	"8A004A801A8002F478",
	"620080001611562C8802118E34",
	"C0015000016115A2E0802F182340",
	"A0016C880162017C3686B18A3D4780",
}

var expectedPart1 = []int{
	9,
	14,
	16,
	12,
	23,
	31,
}

func TestSolvePart1(t *testing.T) {
	for i, in := range inputPart1 {
		got := solvePart1(in)
		if got != expectedPart1[i] {
			t.Errorf("Part 1: Expected %d, but got %d.", expectedPart1[i], got)
		}
	}
}

var inputPart2 = []string{
	"C200B40A82",
	"04005AC33890",
	"880086C3E88112",
	"CE00C43D881120",
	"D8005AC2A8F0",
	"F600BC2D8F",
	"9C005AC2F8F0",
	"9C0141080250320F1802104A08",
}

var expectedPart2 = []int{
	3,
	54,
	7,
	9,
	1,
	0,
	0,
	1,
}

func TestSolvePart2(t *testing.T) {
	for i, in := range inputPart2 {
		got := solvePart2(in)
		if got != expectedPart2[i] {
			t.Errorf("Part 1: Expected %d, but got %d.", expectedPart2[i], got)
		}
	}
}
