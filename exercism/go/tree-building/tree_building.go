// https://exercism.io/my/solutions/467fc5c7042049c8a6465a027a3f23d3

package tree

import (
	"errors"
	"sort"
)

// Record stores the input data to represent an edge in the tree
type Record struct {
	ID     int
	Parent int
}

// Node represents a node in the tree
type Node struct {
	ID       int
	Children []*Node
}

// Build receives a series of input records an returns a tree
// For every ID, the IDs of its children are collected.
// Then, since children have bigger IDs than their parents,
// the tree can be constructed bottom-up
func Build(records []Record) (*Node, error) {
	// If the input data is valid, the tree will have n nodes
	n := len(records)
	if n == 0 {
		return nil, nil
	}

	// Initialize nodes with an impossible ID,
	// so we can use it to check for duplicates.
	nodes := make([]Node, n)
	for i := 0; i < n; i++ {
		nodes[i].ID = -1
	}

	childrenIDs := make([]sort.IntSlice, n)
	for _, r := range records {
		if r.ID < 0 || r.ID >= n || r.Parent < 0 || r.Parent >= n {
			return nil, errors.New("invalid tree (non-continuous")
		}
		if r.ID == 0 && r.Parent != 0 {
			return nil, errors.New("invalid tree (root has parent)")
		}
		if r.ID <= r.Parent && r.ID != 0 {
			return nil, errors.New("invalid tree (wrong hierarchy)")
		}
		if nodes[r.ID].ID != -1 {
			return nil, errors.New("invalid tree (duplicated node)")
		}
		if r.ID != 0 {
			childrenIDs[r.Parent] = append(childrenIDs[r.Parent], r.ID)
		}
		nodes[r.ID].ID = r.ID
	}

	// Add pointers among nodes.
	for i := n - 1; i >= 0; i-- {
		childrenIDs[i].Sort()
		for _, child := range childrenIDs[i] {
			nodes[i].Children = append(nodes[i].Children, &nodes[child])
		}
	}
	return &nodes[0], nil
}
