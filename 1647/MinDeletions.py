############
# Solved!  #
############
from collections import Counter

def minDeletions(s: str) -> int:
    result = 0
    freqs = []
    counter = Counter(s)
    sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1]))
    for key, freq in sorted_counter.items():
        while((freq in freqs) == True):
            freq -= 1
            result += 1
        if(freq >= 1 and (freq not in freqs)):
            freqs.append(freq)
    return result

if(__name__) == '__main__':
    test = "ceabaacb"
    print(minDeletions(test))
