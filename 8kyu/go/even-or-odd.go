// DESCRIPTION:
// Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

package kata

func EvenOrOdd(number int) string {
  var res = number % 2
  if res == 0 {
	return "Even" 
  }
	return "Odd"
 
}