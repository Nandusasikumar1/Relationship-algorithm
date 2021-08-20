def relationship_algorithm(dictionary={},iterations=100):
  F={}
  for i in dictionary:
    F[i]=set(dictionary[i])
  for x in range(iterations):
    for k in F:
      try:
        for j in F[k]:
          if j!=k:
            F[k].update(set([z for z in F[j] if z!=k]))
          else:
            pass
      except:
        pass
  return F
#example
D={1:[7,4,5,2],2:[1,3,10],3:[1,2],4:[3,2],40:[100,123,154]}
print(relationship_algorithm(D))
#output
#{1: {2, 3, 4, 5, 7, 10}, 2: {1, 3, 4, 5, 7, 10}, 3: {1, 2, 4, 5, 7, 10}, 4: {1, 2, 3, 5, 7, 10}, 40: {154, 123, 100}}


