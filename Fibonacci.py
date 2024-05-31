def fibonacci(n):
    # Check if the input is a positive integer
    if n <= 0:
        return "Please enter a positive integer."

    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

# Input: the number of terms you want in the Fibonacci series
num_terms = 10

# Get the Fibonacci series
fib_series = fibonacci(num_terms)

# Print the Fibonacci series
print(f"The first {num_terms} terms of the Fibonacci series are: {fib_series}")
