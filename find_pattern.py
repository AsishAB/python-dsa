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
    
print(lcs_memo("absent", "best")) # Should be 3 => b s t