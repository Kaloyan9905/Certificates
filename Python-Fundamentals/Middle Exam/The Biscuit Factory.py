import math

biscuits = int(input())
workers_count = int(input())
number_biscuits_per_30_days = int(input())

day_3_biscuits = workers_count * biscuits

total_biscuits = 0
diff = 0

for i in range(1, 30):
    if i % 3 == 0:
        total_biscuits += math.floor(0.75 * biscuits * workers_count)
    else:
        total_biscuits += biscuits * workers_count

diff = total_biscuits - number_biscuits_per_30_days
production = abs((diff / number_biscuits_per_30_days) * 100)

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > number_biscuits_per_30_days:
    print(f"You produce {production:.2f} percent more biscuits.")
else:
    print(f"You produce {production:.2f} percent less biscuits.")
