package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type command struct {
	direction string
	units     int
}

type position struct {
	horizontal int
	depth      int
	aim        int
}

func readFileIntoSlice(filename string) []command {
	data, _ := ioutil.ReadFile(filename)
	lines := strings.Split(string(data), "\n")
	commands := make([]command, len(lines))

	var splitted []string
	var units int
	for i, line := range lines {
		splitted = strings.Split(line, " ")
		units, _ = strconv.Atoi(splitted[1])
		commands[i] = command{direction: splitted[0], units: units}
	}

	return commands
}

func updatePosition1(commands []command) position {
	newPos := position{horizontal: 0, depth: 0, aim: 0}

	for _, cmd := range commands {
		switch cmd.direction {
		case "forward":
			newPos.horizontal += cmd.units
		case "up":
			newPos.depth -= cmd.units
		case "down":
			newPos.depth += cmd.units
		}
	}

	return newPos
}

func updatePosition2(commands []command) position {
	newPos := position{horizontal: 0, depth: 0, aim: 0}

	for _, cmd := range commands {
		switch cmd.direction {
		case "forward":
			newPos.horizontal += cmd.units
			newPos.depth += newPos.aim * cmd.units
		case "up":
			newPos.aim -= cmd.units
		case "down":
			newPos.aim += cmd.units
		}
	}

	return newPos
}

func main() {
	commands := readFileIntoSlice("02_dive.input")
	newPos := updatePosition1(commands)
	fmt.Println("Part 1:", newPos.horizontal*newPos.depth)
	newPos = updatePosition2(commands)
	fmt.Println("Part 2:", newPos.horizontal*newPos.depth)
}
