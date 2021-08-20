def relationship_algorithm(dictionary={},iterations=10):
  F={}
  for i in dictionary:
    F[i]=set(dictionary[i])
  for x in range(iterations):
    for k in F:
        for j in F[k]:
            if j in [c for c in F ]:
               F[k]= F[k].union(F[j])
  return F
gg={1:[2,3,4],3:[8,9,1,6,'hi nandu']}
#example
print(relationship_algorithm(gg))
#output
# 1: {1, 2, 3, 4, 6, 8, 9, 'hi nandu'}, 3: {1, 2, 3, 4, 6, 8, 9, 'hi nandu'}}
