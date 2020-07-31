// https://exercism.io/my/solutions/b176b173287d4e2598b135de4b92f0ec

package robotname

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

var numPossibleNames = 26 * 26 * 1000
var usedNames = map[string]bool{}
var random = rand.New(rand.NewSource(time.Now().UnixNano()))

// Robot represents a named robot
type Robot struct {
	name string
}

// Name returns a robot's name, assigning it one first if needed.
func (r *Robot) Name() (string, error) {
	if r.name != "" {
		return r.name, nil
	}
	if len(usedNames) >= numPossibleNames {
		return "", errors.New("no more unique names")
	}
	r.name = randomName()
	for usedNames[r.name] {
		r.name = randomName()
	}
	usedNames[r.name] = true
	return r.name, nil
}

// Reset clears a robot's name
func (r *Robot) Reset() {
	r.name = ""
}

// randomName returns a pseudo-random string in the form [A-Z][A-Z][0-9][0-9][0-9]
func randomName() string {
	letter1 := random.Intn(26) + 'A'
	letter2 := random.Intn(26) + 'A'
	num := random.Intn(1000)
	return fmt.Sprintf("%c%c%03d", letter1, letter2, num)
}
