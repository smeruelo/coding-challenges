// https://exercism.io/my/solutions/741b0cefdb5141eeaf2d81ca70adf131

package raindrops

import "strconv"

// Convert returns funny strings
func Convert(number int) string {
	type Raindrop struct {
		factor   int
		response string
	}

	raindrops := []Raindrop{
		{3, "Pling"},
		{5, "Plang"},
		{7, "Plong"},
	}

	output := ""
	for _, r := range raindrops {
		if number%r.factor == 0 {
			output += r.response
		}
	}

	if output == "" {
		return strconv.Itoa(number)
	}
	return output
}
