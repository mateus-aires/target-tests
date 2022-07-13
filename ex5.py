string = input()
result = ""

for i in range(len(string)-1, -1, -1):
    result += string[i]

print(result)