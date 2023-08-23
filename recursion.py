# Recursive function to calculate the sum of positive integers from 1 to num
def rSigma(num):
    if num > 0:  # Check if num is positive
        return num + rSigma(num - 1)
        # Add the current num to the result of rSigma(num-1)
    return 0  # Return 0 when num is not positive


# Recursive function to calculate the factorial of a positive integer num
def rFact(num):
    if num > 1:  # Check if num is greater than 1
        return num * rFact(num - 1)
        # Multiply the current num with the result of rFact(num-1)
    return 1  # Return 1 when num is 1 (base case for factorial)
