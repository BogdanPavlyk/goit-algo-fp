import random
from collections import Counter
import matplotlib.pyplot as plt

nums = 1_000_000

rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(nums)]
counts = Counter(rolls)

sorted_keys = sorted(counts.keys())

print("Сума | Імовірність")
print("-----|------------")
for total_sum in sorted_keys:
    prob = counts[total_sum] / nums
    print(f"{total_sum:2}   | {prob:.2%}")

plt.bar(sorted_keys, [counts[key] / nums for key in sorted_keys])
plt.xlabel("Сума двох костей")
plt.ylabel("Імовірність")
plt.title("Монте-Карло")
plt.show()