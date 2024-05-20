txt = input()

unique_symbols = set()

for ch in txt:
    unique_symbols.add(ch)

for ch in sorted(unique_symbols):
    print(f"{ch}: {txt.count(ch)} time/s")