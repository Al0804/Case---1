fruits = [
    {'fruitId': 1, 'fruitName': 'Apel', 'fruitType': 'IMPORT', 'stock': 10},
    {'fruitId': 2, 'fruitName': 'Kurma', 'fruitType': 'IMPORT', 'stock': 20},
    {'fruitId': 3, 'fruitName': 'apel', 'fruitType': 'IMPORT', 'stock': 50},
    {'fruitId': 4, 'fruitName': 'Manggis', 'fruitType': 'LOCAL', 'stock': 100},
    {'fruitId': 5, 'fruitName': 'Jeruk Bali', 'fruitType': 'LOCAL', 'stock': 10},
    {'fruitId': 5, 'fruitName': 'KURMA', 'fruitType': 'IMPORT', 'stock': 20},
    {'fruitId': 5, 'fruitName': 'Salak', 'fruitType': 'LOCAL', 'stock': 150}
]

def find_issues(data):
    issues = []
    
    ids = [fruitname['fruitId'] for fruitname in data]
    duplicates = [id for id in set(ids) if ids.count(id) > 1]
    if duplicates:
        issues.append(f"ID duplikat: {duplicates}")
        
        
    names = [fruitname['fruitName'] for fruitname in data]
    names_lower = [name.lower() for name in names]
    case_problems = []
    for i, name1 in enumerate(names_lower):
        for j, name2 in enumerate(names_lower):
                if i < j and name1 == name2 and names[i] != names[j]:
                    case_problems.append(f"'{names[i]}' vs '{names[j]}'")


    if case_problems:
        issues.append(f"Inkonsistensi: {case_problems}")
        return issues

print("4. Masalah data:")
issues = find_issues(fruits)
for issue in issues:        
    print(f"{issue}") 
    
    