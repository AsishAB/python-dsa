def lcs_recursive(seq1, seq2, idx1 = 0, idx2 = 0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)
    
# print(lcs_recursive("absent", "best")) # Should be 3 => b s t


# Improving the function, by remembering the cases where the sequence is repeatative. This is called memoisation (or simply, memorisation)

def lcs_memo(seq1, seq2):
    memo = {}
    def recurse(idx1 = 0, idx2 = 0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        return memo[key]
    return recurse(0 , 0) # lcs_memo() does not return anything without this. recurse() is an internal function. So, we call the recurse function and return the output from there as the output of lcs_memo() 
    
# print(lcs_memo("absent", "best")) # Should be 3 => b s t


# Find Subsequence using Dynamic Programming

def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2 + 1)] for x in range (n1 + 1) ] # The first row and column of a table is 0
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
    return table[-1][-1]

print(lcs_dp("absent", "best")) # Should be 3 => b s t

# Timestamp :- 8.26.37

def max_profits_recursive(weights, profits, capacity, idx = 0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profits_recursive(weights, profits, capacity, idx + 1)
    else:
        option1 = max_profits_recursive(weights, profits, capacity, idx + 1)
        option2 = profits[idx] + max_profits_recursive(weights, profits, capacity-weights[idx], idx + 1)
        return max(option1, option2)