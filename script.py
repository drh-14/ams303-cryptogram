from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt
import string

# 5 letter keyword

# shift 4 by 2
# shift 2 by 1

# LEAST

def compute_ic(s, word_length):
    s = s.replace(" ", "").replace("\n", "")
    letters = []
    for i in range(0, len(s), word_length):
        letters.append(s[i])
    n = len(letters)
    freqs = Counter(letters)
    print(sum(freqs[f] * (freqs[f] - 1) for f in freqs) / (n * (n - 1)))
    
def frequency_graph(s):
    s = s.replace(" ", "").replace("\n", "")
    fig, ax = plt.subplots(5,1)
    for i in range(5):
        letters = []
        for j in range(i, len(s), 5):
            letters.append(s[j])
        freqs = {}
        for uppercase_letter in list(string.ascii_uppercase):
            freqs[uppercase_letter] = 0
        for letter in letters:
            freqs[letter] += 1
        freqs = dict(sorted(freqs.items()))
        labels, frequencies = list(freqs.keys()) * 2, list(freqs.values()) * 2
        x = range(len(labels))
        ax[i].bar(x, frequencies, color = "blue")
        ax[i].set_xticks(x,labels)
    fig.suptitle("Frequency Strips")
    plt.show()

def output_frequencies(s):
    res = []
    s = s.replace(" ", "").replace("\n", "")
    for i in range(5):
        letters = []
        for j in range(i, len(s), 5):
            letters.append(s[j])
        ctr = {}
        for ltr in list(string.ascii_uppercase):
            ctr[ltr] = 0
        for l in letters:
            ctr[l] += 1
        sorted_keys = sorted(list(ctr.keys()))
        sorted_values = [ctr[s] for s in sorted_keys]
        res.append(" ".join([str(s) for s in sorted_values]))
    print(" \n".join(res))
            
        
    
def compute_possible_words():
    letters = list(string.ascii_uppercase) * 2
    offsets = [5, 12, 16, 24, 23]
    for i in range(52):
        s = ""
        for o in offsets:
            if  i - o < 0:
                break
            s += letters[i - o]
        if len(s) == 5:
            print(s)

if __name__ == "__main__":
    compute_possible_words()