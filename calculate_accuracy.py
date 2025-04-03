result_file = "infer_results.txt"

total = 0
correct = 0

with open(result_file, "r") as f:
    for line in f:
        total += 1
        if line.strip().endswith("True"):
            correct += 1

if total > 0:
    accuracy = correct / total
    error_rate = 1 - accuracy
    print(f"Total: {total}")
    print(f"Correct (True): {correct}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Error Rate: {error_rate * 100:.2f}%")
else:
    print("No results found.")
