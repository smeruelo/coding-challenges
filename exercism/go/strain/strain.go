package strain

// Ints represents an array of integers
type Ints []int

// Lists represents an array of array of integers
type Lists [][]int

// Strings represents an array of strings
type Strings []string

// Keep receives a predicate and filters out the elements for which that predicate is false
func (in Ints) Keep(f func(int) bool) Ints {
	if in == nil {
		return nil
	}

	out := Ints{}
	for _, n := range in {
		if f(n) {
			out = append(out, n)
		}
	}
	return out
}

// Discard receives a predicate and filters out the elements for which that predicate is true
func (in Ints) Discard(f func(int) bool) Ints {
	if in == nil {
		return nil
	}

	out := Ints{}
	for _, n := range in {
		if !f(n) {
			out = append(out, n)
		}
	}
	return out
}

// Keep receives a predicate and filters out the elements for which that predicate is false
func (in Lists) Keep(f func([]int) bool) Lists {
	if in == nil {
		return nil
	}

	out := Lists{}
	for _, l := range in {
		if f(l) {
			out = append(out, l)
		}
	}
	return out
}

// Keep receives a predicate and filters out the elements for which that predicate is false
func (in Strings) Keep(f func(string) bool) Strings {
	if in == nil {
		return nil
	}

	out := Strings{}
	for _, s := range in {
		if f(s) {
			out = append(out, s)
		}
	}
	return out
}
