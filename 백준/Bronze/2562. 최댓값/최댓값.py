array = []
maxNumber = 0
line = 0

for i in range(0, 9):
  array.append(int(input()))

for i in range(len(array)):
  if maxNumber < array[i]:
    maxNumber = array[i]
    line = i + 1

print(maxNumber)
print(line)