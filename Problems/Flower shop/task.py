import itertools
# flower_names = ['rose', 'tulip', 'sunflower']
for i in range(0, len(flower_names)-1):
    for flowers in itertools.combinations(flower_names, i+1):
        print(flowers)
