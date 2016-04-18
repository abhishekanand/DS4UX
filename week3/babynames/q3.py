
import ssadata

longestName = ""
Namelen = 0

for name in ssadata.boys.keys():
    if len(name) > Namelen:
        Namelen = len(name)
        longestName= name

for name in ssadata.girls.keys():
    if len(name) > Namelen:
        Namelen = len(name)
        longestName= name

print(longestName)
print(Namelen)

#=======
