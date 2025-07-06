# sort_dict_comparison.py

# ============================================
# Task 1: Dataset
# ============================================
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# ============================================
# Task 2.1: AI-Suggested Code (GitHub Copilot)
# ============================================
def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

sorted_data = sort_by_key(data.copy(), "age")
print("AI-Suggested Sorted Data:")
print(sorted_data)

# ============================================
# Task 2.2: Manual Implementation (Bubble Sort)
# ============================================
def sort_by_key_manual(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

sorted_manual = sort_by_key_manual(data.copy(), "age")
print("\nManual Sorted Data:")
print(sorted_manual)

# ============================================
# Task 2.3: Comparison Summary (Efficiency)
# ============================================

"""
Comparison Summary:

- The AI-suggested code uses Python's built-in `sorted()` function, which is optimized (Timsort, O(n log n)).
- The manual version uses a simple bubble sort (O(n²)), which is slower for large datasets.

Result:
The AI-suggested version is more efficient, concise, and pythonic.
It is better suited for real-world applications, while the manual version is good for learning purposes.
"""
