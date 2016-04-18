
import ssadata

# How many babies are in the dataset (assuming nobody is counted more than once)?
count = 0

for c in ssadata.boys.values():
    count = count + c

for d in ssadata.girls.values():
    count = count + d

print("Total Babies:",count)
