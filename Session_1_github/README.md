import itertools

def dummy_tsp(distance_matrix):
    """
    Dummy TSP solver using brute-force.
    Args:
        distance_matrix (list of list): Square matrix of distances between cities.
    Returns:
        tuple: (Best route as list, total distance as int)
    """
    n = len(distance_matrix)
    cities = list(range(n))
    min_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities[1:]):  # Fix the first city
        route = [0] + list(perm) + [0]  # return to start
        distance = 0
        for i in range(len(route) - 1):
            distance += distance_matrix[route[i]][route[i + 1]]

        if distance < min_distance:
            min_distance = distance
            min_route = route

    return min_route, min_distance


# ----------------------------------------
# 🔽 Sample Usage
# ----------------------------------------

if __name__ == "__main__":
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, cost = dummy_tsp(dist_matrix)
    print("Best Route:", route)
    print("Total Cost:", cost)

    # ----------------------------------------
    # 📝 Auto-generate README.md
    # ----------------------------------------

    readme_content = f"""# 🧭 Travelling Salesman Problem Solver

This project provides a basic implementation of the **Travelling Salesman Problem (TSP)** using a brute-force approach in Python.

---

## 🚀 Features

- Brute-force TSP solver using permutations
- Simple and readable Python implementation
- Distance matrix input
- Prints optimal route and total cost
- Ready for extension with more advanced algorithms

---

## 🧪 Sample Output


---

## 🛠️ How to Use

1. Run the script:

```bash
python tsp_solver.py

with open("README.md", "w") as f:
    f.write(readme_content)

print("\n✅ README.md generated successfully!")
