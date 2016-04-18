
import ssadata



# What about for every first letter
count = 0

for c in ssadata.boys.values():
    count = count + c

for d in ssadata.girls.values():
    count = count + d

print("Total Babies:",count)
