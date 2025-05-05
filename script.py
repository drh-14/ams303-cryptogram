from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt
import string

# 5 letter keyword

def compute_ic(s):
    s = s.replace(" ", "").replace("\n", "")
    letters = []
    for i in range(0, len(s), 5):
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
            n = len(letters)
            freqs = {}
            for uppercase_letter in list(string.ascii_uppercase):
               freqs[uppercase_letter] = 0
            for letter in letters:
                freqs[letter] += 1
            labels = sorted(list(freqs.keys())) * 2
            frequencies = sorted(list(freqs.values())) * 2
            x = range(len(labels))
            ax[i].bar(x, frequencies, color = "blue")
            ax[i].set_xticks(x,labels)
    fig.suptitle("Frequency Strips")
    plt.show()
    
if __name__ == "__main__":
    frequency_graph("""OZYRD TDZTK TNAGW JSHAS OZIRW LQPQH OZIKF TIYSA KOIRS MVIVO 
TSIPL MCMRT BZIMD THZVO MHBMN LBDPT DMAKN THAEB MRITC GEDNB 
XDKQH YBYMN ZEDPT XKAGC TQDTR ZOYGG KHVAI ICUMH LHXSF REOKF 
LUIRS LQZQH OZICU OZICU OCJTN KNYAH UMZGT XEOVO TWISL FMYGD 
TSDTN JSZVR OLDQT ZDOSF LSSAT DYIPO LZBWB KWIGW VEZVT BHVAR 
XYYWB KCOVO TDHG
""")