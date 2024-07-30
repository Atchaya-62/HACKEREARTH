def largest_number_after_removals(N, K):
    N = str(N)
    stack = []
    to_remove = K
    
    for digit in N:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    
    return ''.join(stack)

N,K=map(int,(input().split()))
print(largest_number_after_removals(N, K))  
