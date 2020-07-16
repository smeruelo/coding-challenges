// https://exercism.io/my/solutions/8f46d3609f3e4ea0946d943cc6ac1d9d

package letter

import "sync"

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

// accFrequency counts the frecuency of each rune in a given text and
// accumulates it in an existing FreqMap, which can be accessed concurrently.
func accFrequency(s string, totalCount FreqMap, mux *sync.Mutex, wg *sync.WaitGroup) {
	defer wg.Done()
	count := Frequency(s)

	mux.Lock()
	for k, v := range count {
		totalCount[k] += v
	}
	mux.Unlock()
}

// ConcurrentFrequency counts the frecuency of each rune in a series of texts.
// Texts are analyzed concurrently.
func ConcurrentFrequency(texts []string) FreqMap {
	totalCount := make(FreqMap)
	var mux sync.Mutex
	var wg sync.WaitGroup

	for _, s := range texts {
		wg.Add(1)
		go accFrequency(s, totalCount, &mux, &wg)
	}
	wg.Wait()

	return totalCount
}
