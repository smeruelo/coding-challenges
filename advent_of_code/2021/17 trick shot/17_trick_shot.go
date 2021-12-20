package main

import "fmt"

type area struct {
	minX int
	maxX int
	minY int
	maxY int
}

type position struct {
	x int
	y int
}

type velocity struct {
	x int
	y int
}

func (p *position) step(v velocity) {
	p.x += v.x
	p.y += v.y
}

func (v *velocity) step() {
	if v.x > 0 {
		v.x--
	} else if v.x < 0 {
		v.x++
	}
	v.y--
}

func (a *area) includes(pos position) bool {
	return pos.x >= a.minX && pos.x <= a.maxX && pos.y >= a.minY && pos.y <= a.maxY
}

func simulate(targetArea area, v velocity) bool {
	currentPos := position{x: 0, y: 0}
	for !targetArea.includes(currentPos) && currentPos.y >= targetArea.minY {
		currentPos.step(v)
		v.step()
	}
	return targetArea.includes(currentPos)
}

func solvePart2(targetArea area) int {
	count := 0
	for y := targetArea.minY; y <= -1*targetArea.minY; y++ {
		for x := targetArea.maxX; x > 0; x-- {
			v := velocity{x: x, y: y}
			if simulate(targetArea, v) {
				count++
			}
		}
	}
	return count
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func highestY(targetArea area, v velocity) int {
	pos := position{x: 0, y: 0}
	for v.x != 0 && v.y != 0 {
		pos.step(v)
		v.step()
	}
	return pos.y
}

func solvePart1(targetArea area) int {
	highest := 0
	y := -1 * (targetArea.minY + 1)
	for x := targetArea.maxX; x > 0; x-- {
		v := velocity{x: x, y: y}
		highest = max(highest, highestY(targetArea, v))
	}
	return highest
}

func main() {
	targetArea := area{minX: 288, maxX: 330, minY: -96, maxY: -50}
	fmt.Println("Part 1:", solvePart1(targetArea))
	fmt.Println("Part 2:", solvePart2(targetArea))
}
