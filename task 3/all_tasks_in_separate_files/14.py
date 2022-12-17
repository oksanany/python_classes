def evenSq(lst):
    ans = [str(int(i)**2) for i in lst if int(i[-1]) % 2 == 0]
    return ans
print(evenSq(['43141', '32441', '431', '4154', '43121']))