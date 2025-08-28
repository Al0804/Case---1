fruits = [
    {'fruitId': 1, 'fruitName': 'Apel', 'fruitType': 'IMPORT', 'stock': 10},
    {'fruitId': 2, 'fruitName': 'Kurma', 'fruitType': 'IMPORT', 'stock': 20},
    {'fruitId': 3, 'fruitName': 'apel', 'fruitType': 'IMPORT', 'stock': 50},
    {'fruitId': 4, 'fruitName': 'Manggis', 'fruitType': 'LOCAL', 'stock': 100},
    {'fruitId': 5, 'fruitName': 'Jeruk Bali', 'fruitType': 'LOCAL', 'stock': 10},
    {'fruitId': 5, 'fruitName': 'KURMA', 'fruitType': 'IMPORT', 'stock': 20},
    {'fruitId': 5, 'fruitName': 'Salak', 'fruitType': 'LOCAL', 'stock': 150}
]

def group_by_type(data):
    groups = {}
    for fruitname in data:
        if fruitname['fruitType'] not in groups:
            groups[fruitname['fruitType']] = []
        groups[fruitname['fruitType']].append(fruitname['fruitName'])
    return groups

print("2. Grouping berdasarkan tipe:")
groups = group_by_type(fruits)
print(f"   Jumlah wadah: {len(groups)}")
for tipe, buah_list in groups.items():
    print(f"{tipe}: {buah_list}")