package main

import (
	"fmt"
	"math"
)

func main() {
	for i := 0.0; i < 101.0; i += 1.0 {
		multiple_five := math.Mod(i, 5) == 0.0
		multiple_three := math.Mod(i, 3) == 0.0
		fibonacci_number := is_fibonacci_number(i)

		if multiple_three && multiple_five && fibonacci_number {
			fmt.Println("Pink Flamingo")
		} else if fibonacci_number == true {
			fmt.Println("Flamingo")
		}

		if multiple_three && multiple_five {
			fmt.Println("FizzBuzz")
		} else if multiple_three {
			fmt.Println("Fizz")
		} else if multiple_five {
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}

func is_fibonacci_number(x float64) bool {
	first := 5*math.Pow(x, 2) + 4
	second := 5*math.Pow(x, 2) - 4

	squared := math.Sqrt(first)
	is_integer := squared == float64(int64(squared))
	if is_integer {
		return true
	} else {
		squared := math.Sqrt(second)
		return squared == float64(int64(squared))
	}
}
