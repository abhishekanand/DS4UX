
import ssadata
# What is the longest name in the dataset?
longestName = []
Namelen = 0

for name in ssadata.boys.keys():
    if len(name) > Namelen:
        Namelen = len(name)

for name in ssadata.girls.keys():
    if len(name) > Namelen:
        Namelen = len(name)

for name in ssadata.boys.keys():
    if len(name) == Namelen:
        longestName.append(name)

for name in ssadata.girls.keys():
    if len(name) == Namelen:
        longestName.append(name)

print(len(longestName))
print(Namelen)

#=======
