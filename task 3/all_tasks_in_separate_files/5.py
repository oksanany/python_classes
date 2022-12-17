vowels = 'aoeiuy'
vowels += vowels.upper()
string = input()
ans = ''.join([s for s in string if s not in vowels])
print(ans)