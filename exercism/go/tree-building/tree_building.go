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
// Input records are sorted. This way, and since children must have bigger IDs than their parents,
// when going through them in decreasing order all its children must have appeared so
// everything needed to complete the node is available.
// We can therefore construct the tree bottom-up.
func Build(r []Record) (*Node, error) {
	// If the input data is valid, the tree will have n nodes
	n := len(r)
	if n == 0 {
		return nil, nil
	}

	sort.Slice(r, func(i, j int) bool { return r[i].ID <= r[j].ID })
	nodes := make([]Node, n)

	for i := n - 1; i >= 0; i-- {
		// Validate input data
		if r[i].ID != i || r[i].Parent > r[i].ID || r[i].Parent == r[i].ID && r[i].ID != 0 {
			return nil, errors.New("invalid tree")
		}

		// Add current node to parent's children
		p := &nodes[r[i].Parent]
		if r[i].ID != 0 {
			p.Children = append(p.Children, &nodes[i])
		}

		// Complete current node
		nodes[i].ID = r[i].ID
		c := nodes[i].Children
		sort.Slice(c, func(j, k int) bool { return c[j].ID < c[k].ID })
	}

	return &nodes[0], nil
}
