from collections import Counter
import numpy as np

# 5 letter keyword

def compute_ic(s, start_index, group_size):
    s = s.replace(" ", "").replace("\n", "")
    letters = []
    for i in range(start_index, len(s), group_size):
        letters.append(s[i])
    n = len(letters)
    freqs = Counter(letters)
    print(sum(freqs[f] * (freqs[f] - 1) for f in freqs) / (n * (n - 1)))
    

if __name__ == "__main__":
    compute_ic("""OZYRD TDZTK TNAGW JSHAS OZIRW LQPQH OZIKF TIYSA KOIRS MVIVO 
TSIPL MCMRT BZIMD THZVO MHBMN LBDPT DMAKN THAEB MRITC GEDNB 
XDKQH YBYMN ZEDPT XKAGC TQDTR ZOYGG KHVAI ICUMH LHXSF REOKF 
LUIRS LQZQH OZICU OZICU OCJTN KNYAH UMZGT XEOVO TWISL FMYGD 
TSDTN JSZVR OLDQT ZDOSF LSSAT DYIPO LZBWB KWIGW VEZVT BHVAR 
XYYWB KCOVO TDHG
""", 0, 6)