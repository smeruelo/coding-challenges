// https://exercism.io/my/solutions/b176b173287d4e2598b135de4b92f0ec

package robotname

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const maxNum = 1000

var numPossibleNames = len(letters) * len(letters) * maxNum
var usedNames = make(map[string]struct{}, numPossibleNames)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func randomName() (string, error) {
	if len(usedNames) >= numPossibleNames {
		return "", errors.New("no more unique names")
	}
	for {
		name := fmt.Sprintf("%c%c%03d",
			letters[rand.Intn(len(letters))],
			letters[rand.Intn(len(letters))],
			rand.Intn(maxNum),
		)
		_, ok := usedNames[name]
		if !ok {
			usedNames[name] = struct{}{}
			return name, nil
		}
	}
}

// Robot represents a named robot
type Robot struct {
	name string
}

// Name returns a robot's name, assigning it one first if needed.
func (r *Robot) Name() (string, error) {
	if r.name == "" {
		name, err := randomName()
		if err != nil {
			return "", err
		}
		r.name = name
	}
	return r.name, nil
}

// Reset clears a robot's name
func (r *Robot) Reset() {
	r.name = ""
}
