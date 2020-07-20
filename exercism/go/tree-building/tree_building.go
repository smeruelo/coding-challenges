// https://exercism.io/my/solutions/467fc5c7042049c8a6465a027a3f23d3

package tree

import (
	"errors"
	"sort"
)

// Record stores the input data to represent an edge in the tree.
type Record struct {
	ID     int
	Parent int
}

// Node represents a node in the tree.
type Node struct {
	ID       int
	Children []*Node
}

// Build receives a series of input records an returns a tree.
func Build(records []Record) (*Node, error) {
	if len(records) == 0 {
		return nil, nil
	}

	// Sort input records.
	// This will ease input data validation and children will be added in order.
	sort.Slice(records, func(i, j int) bool {
		return records[i].ID <= records[j].ID
	})

	nodes := make([]*Node, len(records))
	for i, r := range records {
		// Validate input data
		if r.ID != i || r.Parent > r.ID || r.Parent == r.ID && r.ID != 0 {
			return nil, errors.New("invalid tree")
		}

		nodes[i] = &Node{ID: r.ID}

		// Add current node to parent's children
		p := nodes[r.Parent]
		if r.ID != 0 {
			p.Children = append(p.Children, nodes[i])
		}
	}

	return nodes[0], nil
}
