
def getNext(pattern):
    length = len(pattern)
    nextIndex = [0] * length

    for i in range(1, length):
        j = nextIndex[i-1]
        while j > 0 and pattern[j] != pattern[i]:
            j = nextIndex[j-1]
        nextIndex[i] = j+1 if pattern[j] == pattern[i] else j
    # while j < length:
    #     if i == -1 or pattern[i] == pattern[j]:
    #         i += 1
    #         nextIndex[j] = i
    #         j += 1
    #     else:
    #         i = nextIndex[i-1]
    return nextIndex

def kmp_search(pattern, string):
    kmp_table = getNext(pattern)
    ans = []
    j = 0
    #kmp_table[i] = k, means p[:k] == p[i-k:i]
    for i in range(len(string)):
        while j > 0 and pattern[j] != string[i]:
            j = kmp_table[j-1]
        if pattern[j] == string[i]:
            j += 1
        if j == len(pattern):
            # get one match, then we can go to kmp_table[j-1] to check
            ans.append(i-j+1)
            j = kmp_table[j-1]
    return ans


if __name__ == "__main__":
    print kmp_search('aaa', 'aaaaabcaaabc')