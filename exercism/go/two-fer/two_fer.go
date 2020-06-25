// https://exercism.io/my/solutions/1a5af5ece75b49d48733fb0cd439bdf5

package twofer

import "fmt"

func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return fmt.Sprintf("One for %v, one for me.", name)
}
