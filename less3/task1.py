res = {n: 0 for n in range(2, 10)}

for i in range(2, 100):
    for key in res.keys():
        if i % key == 0:
            res[key] += 1

for key, count in res.items():
    print(f'{key}: {count}')
