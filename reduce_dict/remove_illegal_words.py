from os.path import dirname

INDIR = dirname(__file__)
OUTDIR = dirname(INDIR)

with open(f'{INDIR}/dict_full.txt', 'r') as file:
    oldwords = file.read().split('\n')

with open(f'{OUTDIR}/spellingbee_dict.txt', 'w') as file:
    file.write("")
with open(f'{OUTDIR}/spellingbee_dict.txt', 'a') as file:
    newcount = 0
    for word in oldwords:
        word = word[:-1].lower()
        if len(word) in {1, 2, 3}: continue
        if not word.isalpha(): continue
        if len(set(word)) > 7: continue
        file.write(f"{word}\n")
        newcount += 1
print(f"reduced dictionary from {len(oldwords)} to {newcount}")
