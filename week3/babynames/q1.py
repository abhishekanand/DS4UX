
import ssadata
# Are there more boy names or girl names?
# What about for particular first letters?
# What about for every first letter?

boys = len(ssadata.boys)
girls = len(ssadata.girls)
print("Boys :", boys ,"girls:", girls)

# What about for every first letter
countboys = 0
countgirls = 0
for name in ssadata.boys.keys():
    if name[0] == 'a':
        countboys += 1

for name in ssadata.girls.keys():
    if name[0] == 'a':
        countgirls += 1

print("For a : BoysName :" ,countboys ,"girlsName:", countgirls)

letters = "abcdefghizflmnopqrstuvwxyz"
for l in letters:
    num_countboys = 0
    num_countgirls = 0
    for name in ssadata.boys.keys():
        if name[0] == l:
            num_countboys += 1
    for name in ssadata.girls.keys():
        if name[0] == l:
            num_countgirls += 1
    print (l," - Boys : ", num_countboys, "Girls : ", num_countgirls )
