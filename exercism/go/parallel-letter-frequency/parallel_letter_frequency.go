// https://exercism.io/my/solutions/8f46d3609f3e4ea0946d943cc6ac1d9d

package letter

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

// ConcurrentFrequency counts the frecuency of each rune in a series of texts,
// which are analyzed concurrently.
func ConcurrentFrequency(texts []string) FreqMap {
	count := make(FreqMap)
	ch := make(chan FreqMap, 10)

	for _, text := range texts {
		go func(s string) {
			ch <- Frequency(s)
		}(text)
	}

	for range texts {
		for k, v := range <-ch {
			count[k] += v
		}
	}

	return count
}
