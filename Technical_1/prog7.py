# Subset problem using recursion

def func(s, i , curr):
    if i == len(s):
        print(curr)
        return
    func(s, i+1, curr)
    func(s, i+1, curr + s[i])

func("apple", 0, "") # Only replace the test string