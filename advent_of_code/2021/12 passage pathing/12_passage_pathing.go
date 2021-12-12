package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type adjacenciesMap map[string][]string

func readInput(filename string) adjacenciesMap {
	graph := adjacenciesMap{}
	data, _ := ioutil.ReadFile(filename)
	for _, line := range strings.Split(string(data), "\n") {
		caves := strings.Split(string(line), "-")
		graph[caves[0]] = append(graph[caves[0]], caves[1])
		graph[caves[1]] = append(graph[caves[1]], caves[0])
	}
	return graph
}

func isSmall(cave string) bool {
	return cave == strings.ToLower(cave)
}

func copyMap(m map[string]bool) map[string]bool {
	c := map[string]bool{}
	for k, v := range m {
		c[k] = v
	}
	return c
}

func countPaths1(target string, smallCavesVisited map[string]bool, graph adjacenciesMap) int {
	if target == "start" {
		return 1
	}

	if isSmall(target) {
		smallCavesVisited[target] = true
	}

	count := 0
	for _, adj := range graph[target] {
		if isSmall(adj) && smallCavesVisited[adj] {
			continue
		}
		count += countPaths1(adj, copyMap(smallCavesVisited), graph)
	}
	return count
}

func countPaths2(target string, smallCavesVisited map[string]bool, extraVisitAvailable bool, graph adjacenciesMap) int {
	if target == "start" {
		return 1
	}

	if isSmall(target) {
		smallCavesVisited[target] = true
	}

	count := 0
	for _, adj := range graph[target] {
		if isSmall(adj) && smallCavesVisited[adj] {
			if !extraVisitAvailable || adj == "end" {
				continue
			}
			count += countPaths2(adj, copyMap(smallCavesVisited), false, graph)
			extraVisitAvailable = true
			continue
		}
		count += countPaths2(adj, copyMap(smallCavesVisited), extraVisitAvailable, graph)
	}
	return count
}

func solvePart1(inputFile string) int {
	graph := readInput(inputFile)
	return countPaths1("end", map[string]bool{}, graph)
}

func solvePart2(inputFile string) int {
	graph := readInput(inputFile)
	return countPaths2("end", map[string]bool{}, true, graph)
}

func main() {
	fmt.Println("Part 1:", solvePart1("12_passage_pathing.input"))
	fmt.Println("Part 2:", solvePart2("12_passage_pathing.input"))
}
