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

// records is a sortable collection of Record elements.
type records []Record

// Len returns the size of a slice []Record.
func (r records) Len() int {
	return len(r)
}

// Less compares two elements of a slice []Record.
func (r records) Less(i, j int) bool {
	return r[i].ID <= r[j].ID
}

// Swap interchanges two elements of a slice []Record.
func (r records) Swap(i, j int) {
	r[i], r[j] = r[j], r[i]
}

// Node represents a node in the tree.
type Node struct {
	ID       int
	Children []*Node
}

// Build receives a series of input records an returns a tree
// Input records are sorted. This way, and since children must have bigger IDs than their parents,
// when going through them in decreasing order all its childrem must have appeared so
// everything needed to complete the node is available.
// We can therefore construct the tree bottom-up.
func Build(r records) (*Node, error) {
	// If the input data is valid, the tree will have n nodes
	n := len(r)
	if n == 0 {
		return nil, nil
	}

	sort.Sort(r)
	nodes := make([]Node, n)
	childrenIDs := make([]sort.IntSlice, n)

	for i := n - 1; i >= 0; i-- {
		// Validate input data
		if r[i].ID != i {
			return nil, errors.New("invalid tree")
		}
		if r[i].ID == 0 && r[i].Parent != 0 {
			return nil, errors.New("invalid tree (root has parent)")
		}
		if r[i].Parent >= r[i].ID && r[i].ID != 0 {
			return nil, errors.New("invalid tree (wrong hierarchy)")
		}

		// This node is some other's child (unless it's the root)
		if r[i].ID != 0 {
			childrenIDs[r[i].Parent] = append(childrenIDs[r[i].Parent], r[i].ID)
		}
		// Current node's children must have already appeared, so we can create node
		nodes[i].ID = r[i].ID
		childrenIDs[i].Sort()
		for _, child := range childrenIDs[i] {
			nodes[i].Children = append(nodes[i].Children, &nodes[child])
		}
	}
	return &nodes[0], nil
}
