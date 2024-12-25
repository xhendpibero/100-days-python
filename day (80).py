# Day 2: Generate all combinations of 3 digits
def generate_combinations():
    combinations = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                combinations.append(f"{i}{j}{k}")
    return combinations

# Print all combinations
all_combinations = generate_combinations()
for combo in all_combinations:
    print(combo)
