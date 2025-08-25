def solve(data):
    """
    Ham giai bai toan Smart Zoo Manager.
    - data: danh sach cac chuoi da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    idx = 0
    n = int(data[idx])
    idx += 1
    
    # Khoi tao danh sach dong vat
    animals = {}
    species_count = {"Dog": 0, "Cat": 0, "Bird": 0}
    
    # Doc thong tin N con vat
    for _ in range(n):
        parts = data[idx].split()
        species, name, age, weight = parts[0], parts[1], int(parts[2]), float(parts[3])
        animals[name] = {
            'species': species,
            'age': age,
            'weight': weight
        }
        species_count[species] += 1
        idx += 1
    
    # Doc so lenh Q
    q = int(data[idx])
    idx += 1
    
    result = []
    
    # Xu ly Q lenh
    for _ in range(q):
        command = data[idx].split()
        idx += 1
        
        if command[0] == "SOUND":
            name = command[1]
            species = animals[name]['species']
            if species == "Dog":
                result.append("Woof")
            elif species == "Cat":
                result.append("Meow")
            elif species == "Bird":
                result.append("Chirp")
                
        elif command[0] == "SPECIAL":
            name = command[1]
            species = animals[name]['species']
            if species == "Dog":
                result.append("Fetch")
            elif species == "Cat":
                result.append("Scratch")
            elif species == "Bird":
                result.append("Fly")
                
        elif command[0] == "FEED":
            name = command[1]
            weight_inc = float(command[2])
            animals[name]['weight'] += weight_inc
            # FEED khong can output
            
        elif command[0] == "STAT":
            species = command[1]
            result.append(str(species_count[species]))
    
    return result

def main():
    data = []
    
    # Doc so dong vat
    n = int(input().strip())
    data.append(str(n))
    
    # Doc thong tin N con vat
    for _ in range(n):
        line = input().strip()
        data.append(line)
    
    # Doc so lenh
    q = int(input().strip())
    data.append(str(q))
    
    # Doc Q lenh
    for _ in range(q):
        line = input().strip()
        data.append(line)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()