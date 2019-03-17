package main

import (
	"fmt"
	"math"
)

func main() {
	for i := 0.0; i < 101.0; i += 1.0 {
		MultipleFive := math.Mod(i, 5) == 0.0
		MultipleThree := math.Mod(i, 3) == 0.0
		FibonacciNumber := isFibonacciNumber(i)
		// it isn't very clear to me the exclusive conditions in the text,
		// so obviously this is how I interpreted the text :)
		if MultipleThree && MultipleFive && FibonacciNumber {
			fmt.Println("Pink Flamingo")
		} else if FibonacciNumber == true {
			fmt.Println("Flamingo")
		}

		if MultipleThree && MultipleFive {
			fmt.Println("FizzBuzz")
		} else if MultipleThree {
			fmt.Println("Fizz")
		} else if MultipleFive {
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}

func isFibonacciNumber(x float64) bool {
	first := 5*math.Pow(x, 2) + 4
	second := 5*math.Pow(x, 2) - 4

	squared := math.Sqrt(first)
	isInteger := squared == float64(int64(squared))
	if isInteger {
		return true
	} else {
		squared := math.Sqrt(second)
		return squared == float64(int64(squared))
	}
}
