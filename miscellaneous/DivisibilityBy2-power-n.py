# Problem: Divisibility by 2^n
# Link: https://codeforces.com/gym/445741/problem/E

def min_operations(t):
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Calculate the count of powers of 2 in the product of all elements
        count = 0
        for i in a:
            while i % 2 == 0 and i > 0:
                i //= 2
                count += 1
        
        # If the count is already greater than or equal to n, no operations are needed
        if count >= n:
            results.append(0)
        else:
            # Calculate the count of powers of 2 for each index i
            powers = []
            for i in range(1, n + 1):
                power_count = 0
                while i % 2 == 0:
                    i //= 2
                    power_count += 1
                powers.append(power_count)
            
            # Sort the powers in descending order
            powers.sort(reverse=True)
            
            # Find the minimum number of operations required
            total_count = count
            min_ops = -1
            for i, power in enumerate(powers, 1):
                total_count += power
                if total_count >= n:
                    min_ops = i
                    break
            
            results.append(min_ops)
    
    return results


# Get the number of test cases
t = int(input())

# Get the results for the test cases
results = min_operations(t)

# Print the results
for res in results:
    print(res)
