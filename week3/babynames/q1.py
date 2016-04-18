
import ssadata

boys = len(ssadata.boys)
girls = len(ssadata.girls)
print("Boys :" ,boys ,"girls:", girls)

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
