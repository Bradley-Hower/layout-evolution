import random
import subprocess
import os
import re

population_size = 10
g_filepath = ''

# Creates CSV File. If name already exists, iterates. Creates headings: Top one's name and score, worst one last round name and score.
def init_filepath():
  global g_filepath
  # Define the full file path
  counter = 1
  file_path = os.path.join('data', f"layout_scores_{counter}.csv")
  while os.path.exists(file_path):
    file_path = os.path.join('data', f"layout_scores_{counter}.csv")
    counter += 1

  g_filepath = file_path

  # Write layout to file. 
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(f'"Best","Best Score","Worst Last Round","Worst Last Round Score"\n')

# Creates population 1st generation
def init_population(pop_size):
  keyboard_chars = list("zqj?x'kv.,bwygpfmucdlhrsinoate")
  population = []

  # Initialization with random layout
  for i in range(pop_size):
    random_genome = keyboard_chars[:]
    random.shuffle(random_genome)
    str_random_genome = "".join(random_genome)
    population.append(str_random_genome)
  return population

# Writes layout to file
def writelayout(group):
  # Define the full file path
  file_path = os.path.join('genlayouts', 'test')

  # Write layout to file
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(f"TEST\n{group[0]} {group[1]} {group[2]} {group[3]} {group[4]} {group[5]} {group[6]} {group[7]} {group[8]} {group[9]}\n{group[10]} {group[11]} {group[12]} {group[13]} {group[14]} {group[15]} {group[16]} {group[17]} {group[18]} {group[19]}\n{group[20]} {group[21]} {group[22]} {group[23]} {group[24]} {group[25]} {group[26]} {group[27]} {group[28]} {group[29]}\n0 1 2 3 3 4 4 5 6 7\n0 1 2 3 3 4 4 5 6 7\n0 1 2 3 3 4 4 5 6 7")

# Runs analysis on layout
def analysis():
  analysis_text = subprocess.run(['./genkey', 'analyze', 'test'], capture_output=True, text=True)

  # Initialize the score variable
  score = None

  # Regex select the score: stringify analysis output, select group
  score = re.search(r"(?<=Score: )([0-9]*).([0-9]*)", str(analysis_text)).group(0)

  # Return the score if found, otherwise return zero
  score_output = score if score else "0"
  return score_output


# Takes population and generates dictionary, keys are layouts, values are analysis scores
def eval_population(population):
  popscores = {}
  for i in range(len(population)):
    # Write layout to file
    writelayout(population[i])
    # Run analysis
    score = analysis()
    # Add score to dictionary
    popscores[population[i]] = score
  return popscores



# Takes population's evaluations dictionary, outputs dictionary ranking layouts for population. Location to make worst (change "float" to "-float")
def ranked_population_scores(evals_dict):
  # Sort keys by values. Reassign keys to values, new keys are ranks.
  sorted_scores = sorted(evals_dict.items(), key=lambda kv: (float(kv[1]), kv[0]))

  return sorted_scores



# Culls the population. Pushes forward top x% (Ex: 30% or 10%, etc.).
def cull(results_sorted_pop_evals, p_size, select_percent):
  select_gen = []

  for i in range(int(p_size*select_percent)):
    select_gen.append(results_sorted_pop_evals[i][0])

  return select_gen



# Each board in top x% (Ex: 30%) range gets x number of children (ex: 10) for a chance to evolve into next generation
def mult_mutants_base(boards, children_num):
  offspring = []
  for i in range(int(len(boards))):
    for _ in range(children_num):
      offspring.append(boards[i])
  
  return offspring



# Keyboard mutator. X number of random key swaps.
def mutate(bases, mutation_rounds):
  children_mut_x = []

  # Mutator: swaps key pair
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

  # Machine which runs the number of mutation rounds
  def mutation_generator(mutation_rnds):
    nonlocal children_mut_x

    for _ in range(mutation_rnds):
      children_mut_x = mutations(bases)
  
  mutation_generator(mutation_rounds)
  return children_mut_x


# Round Top X (set to population size) - set to go to next round
def end_cull(results_sorted_end_evals, select_num):
  select_gen = []
  print(results_sorted_end_evals[0][1])
  print(results_sorted_end_evals[-1][1])
  print("----------")
  for i in range(select_num):
    select_gen.append(results_sorted_end_evals[i][0])

  return select_gen

# Writes to csv file: top one's name and score, worst one last round name and score
def generation_top_one(results_ranked_pop_scores):
  global g_filepath
  with open(g_filepath, 'a', encoding='utf-8') as f:
    f.write(f'"{results_ranked_pop_scores[0][0]}",{results_ranked_pop_scores[0][1]},"{results_ranked_pop_scores[-1][0]}",{results_ranked_pop_scores[-1][1]}\n')


def generations(total_generations, pop_s):
  global g_filepath
  # Population at start of generation  
  init_filepath()
  generation_population = init_population(pop_s)

  # First Generation
  results_eval_pop = eval_population(generation_population)
  results_ranked_pop_scores = ranked_population_scores(results_eval_pop)

  # Rankings at beginning of a generation
  beginning_ranking = results_ranked_pop_scores

  # Subsequent Generations
  for i in range(total_generations):
    print(f"Generation: {i+1}")
    # Top 10%
    results_cull_10 = cull(beginning_ranking, pop_s, 0.1)

    # Top 30%
    results_cull_30 = cull(beginning_ranking, pop_s, 0.3)

    # Multiply and mutate - 10 children, 3 mutatation swaps
    results_mult_mutants_base = mult_mutants_base(results_cull_30, 10)
    results_generation_mutations = mutate(results_mult_mutants_base , 3)

    # Top 10% of population + Top 30% multiplied and mutated
    generation_competition = results_cull_10 + results_generation_mutations

    # End of generations evaluations
    results_end_eval_population = eval_population(generation_competition)

    # End of generations ranking
    results_end_ranked_population_scores = ranked_population_scores(results_end_eval_population)

    beginning_ranking = results_end_ranked_population_scores
    generation_population = end_cull(results_end_ranked_population_scores, pop_s)

    # Record
    generation_top_one(results_end_ranked_population_scores)
  
  # Closing Message
  print("====================")
  print(f"Run of {total_generations} generations completed.")
  with open(g_filepath) as f:
    for line in (f.readlines() [-1:]):
        print("Final generations best and worst:")
        print(line, end ='')


generations(5, population_size)