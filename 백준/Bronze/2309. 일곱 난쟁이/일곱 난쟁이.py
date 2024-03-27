dwarves = [int(input()) for _ in range(9)]
total_height = sum(dwarves)
found = False

for i in range(9):
    if found:
        break
    for j in range(i + 1, 9):
        if total_height - (dwarves[i] + dwarves[j]) == 100:
            fake1, fake2 = dwarves[i], dwarves[j]
            dwarves.remove(fake1)
            dwarves.remove(fake2)
            dwarves.sort()
            for dwarf in dwarves:
                print(dwarf)
            found = True
            break
