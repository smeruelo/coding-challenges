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

var names = make([]string, len(letters)*len(letters)*maxNum)
var ch = make(chan string)

func init() {
	// Produce all the possible names and shuffle them
	i := 0
	for _, l1 := range letters {
		for _, l2 := range letters {
			for n := 0; n < maxNum; n++ {
				names[i] = fmt.Sprintf("%c%c%03d", l1, l2, n)
				i++
			}
		}
	}
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(names), func(i, j int) {
		names[i], names[j] = names[j], names[i]
	})

	// Start a generator that will write one name at a time in a channel, until exhausted.
	go nameGenerator()
}

func nameGenerator() {
	defer close(ch)
	for _, name := range names {
		ch <- name
	}
}

// Robot represents a named robot
type Robot struct {
	name string
}

// Name returns a robot's name, assigning it one first if needed.
func (r *Robot) Name() (string, error) {
	if r.name == "" {
		var ok bool
		r.name, ok = <-ch
		if !ok {
			return "", errors.New("no more unique names")
		}
	}
	return r.name, nil
}

// Reset clears a robot's name
func (r *Robot) Reset() {
	r.name = ""
}
