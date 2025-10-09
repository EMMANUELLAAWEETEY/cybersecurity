#!/bin/bash
#function ato create acalculator
##asigning an operand a,numbers

#!/bin/bash

# Function to perform calculation
calculate() {
    echo "Enter the first number:"
    read num1

    echo "Enter the operation (+, -, *, /):"
    read op

    echo "Enter the second number:"
    read num2

    # Perform the calculation based on the operation
    case $op in
        +)
            result=$(echo "$num1 + $num2" | bc)
            ;;
        -)
            result=$(echo "$num1 - $num2" | bc)
            ;;
        \*)
            result=$(echo "$num1 * $num2" | bc)
            ;;
        /)
            if [ "$num2" -eq 0 ]; then
                echo "Error: Division by zero!"
                exit 1
            else
                result=$(echo "$num1 / $num2" | bc)
            fi
            ;;
        *)
            echo "Invalid operation!"
            exit 1
            ;;
    esac

    echo "Result: $result"
}

# Main function to call calculate
calculate


