package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
)

type astNode struct {
	version  int
	nodeType string
	children []astNode
	literal  int
}

func hexToBin(hex string) string {
	bin := ""
	for _, char := range hex {
		digit, _ := strconv.ParseUint(string(char), 16, 32)
		bin += fmt.Sprintf("%04b", digit)
	}
	return bin
}

func subpacketsLength(bin string, index int) (int, int) {
	len, _ := strconv.ParseInt(bin[index:index+15], 2, 32)
	return int(len), index + 15
}

func numberOfSubpackets(bin string, index int) (int, int) {
	num, _ := strconv.ParseInt(bin[index:index+11], 2, 32)
	return int(num), index + 11
}

func decodeOperands(bin string, index int, mode byte) ([]astNode, int) {
	operands := []astNode{}
	var num, len, newIndex int
	var node astNode
	if mode == '0' {
		len, index = subpacketsLength(bin, index)
		for newIndex = index; newIndex < index+len; {
			node, newIndex = decodePacket(bin, newIndex)
			operands = append(operands, node)
		}
	} else {
		num, newIndex = numberOfSubpackets(bin, index)
		for decodedSubpackets := 0; decodedSubpackets < num; decodedSubpackets++ {
			node, newIndex = decodePacket(bin, newIndex)
			operands = append(operands, node)
		}
	}
	return operands, newIndex
}

func decodeOperator(bin string, index int) (astNode, int) {
	version := getVersion(bin, index-3)
	mode := bin[index+3]
	operands, newIndex := decodeOperands(bin, index+4, mode)
	node := astNode{
		version:  version,
		nodeType: bin[index : index+3],
		children: operands,
		literal:  -1,
	}
	return node, newIndex
}

func getVersion(bin string, index int) int {
	version, _ := strconv.ParseInt(bin[index:index+3], 2, 32)
	return int(version)
}

func decodeLiteral(bin string, index int) (astNode, int) {
	version := getVersion(bin, index-6)
	var newIndex int
	strNumber := ""
	for newIndex = index; ; newIndex += 5 {
		strNumber += bin[newIndex+1 : newIndex+5]
		if bin[newIndex] == '0' {
			break
		}
	}
	decNumber, _ := strconv.ParseInt(strNumber, 2, 64)
	node := astNode{
		version:  version,
		nodeType: "100",
		children: []astNode{},
		literal:  int(decNumber),
	}
	return node, newIndex + 5
}

func decodePacket(bin string, index int) (astNode, int) {
	if bin[index+3:index+6] == "100" {
		return decodeLiteral(bin, index+6)
	}
	return decodeOperator(bin, index+3)
}

func applySum(operands []astNode) int {
	sum := 0
	for _, node := range operands {
		sum += evalNodePart2(node)
	}
	return sum
}

func applyProduct(operands []astNode) int {
	product := 1
	for _, node := range operands {
		product *= evalNodePart2(node)
	}
	return product
}

func applyMin(operands []astNode) int {
	min := evalNodePart2(operands[0])
	for i, node := range operands {
		if i == 0 {
			continue
		}
		op := evalNodePart2(node)
		if op < min {
			min = op
		}
	}
	return min
}

func applyMax(operands []astNode) int {
	max := evalNodePart2(operands[0])
	for i, node := range operands {
		if i == 0 {
			continue
		}
		op := evalNodePart2(node)
		if op > max {
			max = op
		}
	}
	return max
}

func applyGreaterThan(operands []astNode) int {
	op1 := evalNodePart2(operands[0])
	op2 := evalNodePart2(operands[1])

	if op1 > op2 {
		return 1
	}
	return 0
}

func applyLessThan(operands []astNode) int {
	op1 := evalNodePart2(operands[0])
	op2 := evalNodePart2(operands[1])

	if op1 < op2 {
		return 1
	}
	return 0
}

func applyEqual(operands []astNode) int {
	op1 := evalNodePart2(operands[0])
	op2 := evalNodePart2(operands[1])

	if op1 == op2 {
		return 1
	}
	return 0
}

func evalNodePart2(node astNode) int {
	var value int
	switch node.nodeType {
	case "000":
		value = applySum(node.children)
	case "001":
		value = applyProduct(node.children)
	case "010":
		value = applyMin(node.children)
	case "011":
		value = applyMax(node.children)
	case "100":
		value = node.literal
	case "101":
		value = applyGreaterThan(node.children)
	case "110":
		value = applyLessThan(node.children)
	case "111":
		value = applyEqual(node.children)
	}
	return value
}

func solvePart2(hex string) int {
	bin := hexToBin(hex)
	ast, _ := decodePacket(bin, 0)
	return evalNodePart2(ast)
}

func applyVersion(children []astNode) int {
	sum := 0
	for _, node := range children {
		sum += evalNodePart1(node)
	}
	return sum
}

func evalNodePart1(node astNode) int {
	value := node.version
	if node.nodeType != "100" {
		value += applyVersion(node.children)
	}
	return value
}

func solvePart1(hex string) int {
	bin := hexToBin(hex)
	ast, _ := decodePacket(bin, 0)
	return evalNodePart1(ast)
}

func main() {
	hex, _ := ioutil.ReadFile("16_packet_decoder.input")
	fmt.Println("Part 1:", solvePart1(string(hex)))
	fmt.Println("Part 2:", solvePart2(string(hex)))
}
