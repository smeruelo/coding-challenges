// https://exercism.io/my/solutions/1a5af5ece75b49d48733fb0cd439bdf5

// Package twofer provides awesome friendship tools :)
package twofer

import "fmt"

// ShareWith returns a generous message.
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
