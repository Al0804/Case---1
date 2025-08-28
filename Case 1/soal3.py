fruits = [
    {'fruitId': 1, 'fruitName': 'Apel', 'fruitType': 'IMPORT', 'stock': 10},
    {'fruitId': 2, 'fruitName': 'Kurma', 'fruitType': 'IMPORT', 'stock': 20},
    {'fruitId': 3, 'fruitName': 'apel', 'fruitType': 'IMPORT', 'stock': 50},
    {'fruitId': 4, 'fruitName': 'Manggis', 'fruitType': 'LOCAL', 'stock': 100},
    {'fruitId': 5, 'fruitName': 'Jeruk Bali', 'fruitType': 'LOCAL', 'stock': 10},
    {'fruitId': 5, 'fruitName': 'KURMA', 'fruitType': 'IMPORT', 'stock': 20},
    {'fruitId': 5, 'fruitName': 'Salak', 'fruitType': 'LOCAL', 'stock': 150}
]


def total_stock_by_type(data):
    totals = {}
    for fruitname in data:
        totals[fruitname['fruitType']] = totals.get(fruitname['fruitType'], 0) + fruitname['stock']
    return totals

print("3. Total stock per tipe:")
stocks = total_stock_by_type(fruits)
for tipe, total in stocks.items():
    print(f"{tipe}: {total}") 