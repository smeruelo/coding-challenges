package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strings"
)

type segments []rune

type patterns struct {
	two   segments
	three segments
	four  segments
	five  []segments
	six   []segments
}

type entry struct {
	patterns patterns
	values   []string
}

func countUniques(entries []entry) (count int) {
	for _, e := range entries {
		for _, v := range e.values {
			if len(v) == 2 || len(v) == 3 || len(v) == 4 || len(v) == 7 {
				count++
			}
		}
	}
	return count
}

type translationTable map[rune]rune

const sevenSegments = "abcdefg"

func stringToSegments(s string) segments {
	runes := make(segments, len(s))
	for i, r := range s {
		runes[i] = r
	}
	return runes
}

func segmentsToString(runes segments) string {
	s := ""
	for _, r := range runes {
		s += string(r)
	}
	return s
}

func readInput(filename string) []entry {
	data, _ := ioutil.ReadFile(filename)
	entries := make([]entry, 0)
	for _, line := range strings.Split(string(data), "\n") {
		parts := strings.Split(string(line), " | ")
		p := strings.Split(string(parts[0]), " ")
		v := strings.Split(string(parts[1]), " ")
		patterns := patterns{}
		for _, pattern := range p {
			segments := stringToSegments(pattern)
			switch len(segments) {
			case 2:
				patterns.two = segments
			case 3:
				patterns.three = segments
			case 4:
				patterns.four = segments
			case 5:
				patterns.five = append(patterns.five, segments)
			case 6:
				patterns.six = append(patterns.six, segments)
			}
		}
		entries = append(entries, entry{patterns: patterns, values: v})
	}
	return entries
}

func segmentInSet(segment rune, set segments) bool {
	for _, s := range set {
		if s == segment {
			return true
		}
	}
	return false
}

func intersection(sets []segments) segments {
	commonSegments := make(segments, 0)
	for _, segment := range sevenSegments {
		common := true
		for _, set := range sets {
			common = common && segmentInSet(segment, set)
		}
		if common {
			commonSegments = append(commonSegments, segment)
		}
	}
	return commonSegments
}

func segmentsMissingInPatternsSix(p6 []segments) segments {
	missingSegments := segments{}
	for _, p := range p6 {
		s := difference(stringToSegments(sevenSegments), p)[0]
		missingSegments = append(missingSegments, s)
	}
	return missingSegments
}

func difference(set, itemsToRemove segments) segments {
	rest := make(segments, 0)
	for _, s := range set {
		if !segmentInSet(s, itemsToRemove) {
			rest = append(rest, s)
		}
	}
	return rest
}

func reverse(t translationTable) translationTable {
	r := make(translationTable)
	r[t['a']] = 'a'
	r[t['b']] = 'b'
	r[t['c']] = 'c'
	r[t['d']] = 'd'
	r[t['e']] = 'e'
	r[t['f']] = 'f'
	r[t['g']] = 'g'
	return r
}

func translateValues(wrongValues []string, t translationTable) (correctValues []string) {
	rt := reverse(t)
	for _, wv := range wrongValues {
		s := make(segments, 0)
		for _, ws := range wv {
			s = append(s, rt[ws])
		}
		sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
		correctValues = append(correctValues, segmentsToString(s))
	}
	return correctValues
}

func segmentsToDecimalDigit(segments string) int {
	switch segments {
	case "abcefg":
		return 0
	case "cf":
		return 1
	case "acdeg":
		return 2
	case "acdfg":
		return 3
	case "bcdf":
		return 4
	case "abdfg":
		return 5
	case "abdefg":
		return 6
	case "acf":
		return 7
	case "abcdefg":
		return 8
	case "abcdfg":
		return 9
	}
	return -1
}

func decode(values []string) int {
	num := 0
	for i, v := range values {
		num += int(math.Pow10(3-i) * float64(segmentsToDecimalDigit(v)))
	}
	return num
}

func deduceTranslationTable(patterns patterns) translationTable {
	// logic:
	// number 1 = CF, so:
	//   C can be any of the two segments in patterns.two (2)
	//   F can be any of the two segments in patterns.two
	// number 7 = ACF, so:
	//   A is the segment in patterns.three that is not in patterns.two
	// number 4 = BCDF, so:
	//   B can be any of the two segments in patterns.four that are not in patterns.two
	//   D can be any of the two segments in patterns.four that are not in patterns.two (1)
	// there are 3 numbers with 5 digits:
	//   number 2 = A CDE G   |    ADG appear in all of them (and we already know A)
	//   number 3 = A CD FG   |>>  BE  appear in just one
	//   number 5 = AB D FG   |    so:
	//   there are 3 segments common to all patterns.five
	//     D can be any of the those that aren't A: intersection with (1) gives us D
	//     G can be any of the those that aren't A: G is the one that we don't assign to D
	//     B is the one in (1) that we don't assign to D
	// there are 3 numbers with 6 digits:
	//   number 0 = ABC EFG   |
	//   number 6 = AB DEFG   |>>  DCE 'missing'
	//   number 9 = ABCD FG   |
	// DCE must match with the 3 segments missing in patterns.six, and we already know D
	// C can be one of the other two: intersection with (2) gives us C
	// E can be one of the other two: E is the one that we don't assign to C
	// F is the one in (2) that we don't assign to C

	t := make(translationTable)
	cf := patterns.two
	t['a'] = difference(patterns.three, patterns.two)[0]
	bd := difference(patterns.four, patterns.two)

	dg := difference(intersection(patterns.five), segments{t['a']})
	t['d'] = intersection([]segments{dg, bd})[0]
	t['g'] = difference(dg, bd)[0]
	t['b'] = difference(bd, dg)[0]

	ce := difference(segmentsMissingInPatternsSix(patterns.six), segments{t['d']})
	t['c'] = intersection([]segments{ce, cf})[0]
	t['e'] = difference(ce, cf)[0]
	t['f'] = difference(cf, ce)[0]

	return t
}

func solvePart1(inputFile string) int {
	entries := readInput(inputFile)
	return countUniques(entries)
}

func solvePart2(inputFile string) int {
	entries := readInput(inputFile)

	sum := 0
	for _, entry := range entries {
		translator := deduceTranslationTable(entry.patterns)
		correctValues := translateValues(entry.values, translator)
		num := decode(correctValues)
		sum += num
	}

	return sum
}

func main() {
	fmt.Printf("Part 1: %d\n", solvePart1("08_seven_segment_search.input"))
	fmt.Printf("Part 2: %d\n", solvePart2("08_seven_segment_search.input"))
}
