// Complete the square sum function so that it squares each number passed into it and then sums the results together.

// For example, for [1, 2, 2] it should return 9
// because 1^2 + 2^2 + 2^2 = 9.

package kata

func SquareSum(numbers []int) int {
	s := 0
	for _,n := range numbers {
	  s +=(n*n)
	}
	return s
}