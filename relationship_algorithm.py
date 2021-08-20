def relationship_algorithm(dictionary={},iterations=10):
  
  for i in dictionary:
    dictionary[i]=set(dictionary[i])
  for x in range(iterations):
    for k in dictionary:
        for j in dictionary[k]:
            if j in [c for c in dictionary]:
               dictionary[k]= dictionary[k].union(dictionary[j])
  return dictionary 
gg={1:[2,3,4],3:[8,9,1,6,'hi nandu']}
#example
print(relationship_algorithm(gg))
#output
# 1: {1, 2, 3, 4, 6, 8, 9, 'hi nandu'}, 3: {1, 2, 3, 4, 6, 8, 9, 'hi nandu'}}
