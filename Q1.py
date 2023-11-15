def sum_of_n_term(a, d, n):

    sum = 0
    for i in range(n):
        term = a + i * d
        sum = sum+term
    return sum

a = int(input("Enter the first term (a) of the arithmetic sequence: "))
d = int(input("Enter the common difference (d) of the arithmetic sequence: "))
n = int(input("Enter the number of terms (n) to sum: "))

if a > 0 and d > 0 and n > 0:
    result = sum_of_n_term(a, d, n)
    print( "The sum of the first", n, "terms of the arithmetic sequence is:", result)
else:
    print("Please enter positive integers only.")