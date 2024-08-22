import random

# Keyboard mutator. Two random key swaps.
def mutate(bases, mutation_rounds):

  # Mutations
  def mutations(mutation_bases):
    children_mut_round = []
    bases_length = int(len(mutation_bases[0]))
    
    for i in range(int(len(mutation_bases))):
      point1 = random.randint(0, (bases_length - 1))
      point2 = random.randint(0, (bases_length - 1))
      base_list = list(mutation_bases[i])
      swap1 = base_list[point1]
      swap2 = base_list[point2]
      base_list[point1] = swap2
      base_list[point2] = swap1
      base_back_to_string = "".join(base_list)
      children_mut_round.append(base_back_to_string)
    
    return children_mut_round

  children_mut_x = []

  def mutation_turner(mutation_rnds):
    nonlocal children_mut_x

    for _ in range(mutation_rnds):
      children_mut_x = mutations(bases)
      print(children_mut_x)
  
  mutation_turner(mutation_rounds)
  print(children_mut_x)

  return children_mut_x

mutate(["7532", "1894"], 1)