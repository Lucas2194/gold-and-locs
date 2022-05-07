import numpy as np

# np.random.seed(5555)
gold = np.random.randint(low = 0, high = 10, size = (7,7))

locs = np.random.randint(low = 0, high = 6, size = (5,2))
# locs = np.array([
#     [0,4],
#     [2,2],
#     [2,3],
#     [5,1],
#     [6,3]
# ])

for loc in locs:
    print(f' W lokalizacji {loc}, wydobyliśmy tyle złota: {gold[loc[0], loc[1]]}')
