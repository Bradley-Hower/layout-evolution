import random
import subprocess
import os
import re
from operator import itemgetter

population_size = 100
g_filepath = ''
test_layout_path = os.path.join('genlayouts', 'test')

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


# Writes layout to file in CSV format
def writelayout(group):
  global test_layout_path

  # Write layout to file
  with open(test_layout_path, 'w', encoding='utf-8') as f:
    f.write("TEST\n")
    f.write(" ".join(group[:10]) + "\n")
    f.write(" ".join(group[10:20]) + "\n")
    f.write(" ".join(group[20:]) + "\n")
    f.write("0 1 2 3 3 4 4 5 6 7\n" * 3)


# Runs analysis on layout
def analysis():
  analysis_text = subprocess.run(['./genkey', 'analyze', 'test'], capture_output=True, text=True)

  # Initialize the score variable
  score = None

  # Regex select the score: stringify analysis output, select group
  score = re.search(r"(?<=Score: )([0-9]*).([0-9]*)", str(analysis_text)).group(0)

  # Return the score if found, otherwise return zero
  return float(score) if score else "0"


# Takes population and generates dictionary, keys are layouts, values are analysis scores
def eval_population(population):
  popscores = {}
  for layout in population:
    # Write layout to file
    writelayout(layout)
    # Run analysis
    score = analysis()
    # Add score to dictionary
    popscores[layout] = score
  return popscores


# Takes population's evaluations dictionary, outputs dictionary ranking layouts for population. Location to make worst (change "float" to "-float")
def ranked_population_scores(evals_dict):
  # Sort keys by values. Reassign keys to values, new keys are ranks.
  # Slightly faster alternative to: sorted_scores = sorted(evals_dict.items(), key=lambda kv: float(kv[1]))
  sorted_scores = {k: v for k,v in sorted(evals_dict.items(), key=itemgetter(1))}
  sorted_scores_list = list(sorted_scores.items())
  return sorted_scores_list


# Culls the ranked population. Pushes forward top x% (Ex: 30% or 10%, etc.).
def cull(res_ranked_pop_evals, p_size, select_percent):
  select_gen = []

  for i in range(int(p_size*select_percent)):
    select_gen.append(res_ranked_pop_evals[i][0])

  return select_gen


# Each board in top x% (Ex: 30%) range gets x number of children (ex: 10) for a chance to evolve into next generation
def mult_mutants(boards, mutation_func, children_num, mutation_rnds):
    offspring = []
    for board in boards:
        for _ in range(children_num):
            # Apply mutations to create variation
            mutated_board = mutation_func(board, mutation_rnds)  
            offspring.append(mutated_board)
    return offspring


# Keyboard mutator. X number of random key swaps.
def mutate(child, mutation_rounds):
  # Runs mutation round
  for _ in range(mutation_rounds):
    # Swaps two random keys within each layout
    child_keys = list(child)
    point1, point2 = random.sample(range(len(child_keys)), 2)
    child_keys[point1], child_keys[point2] = child_keys[point2], child_keys[point1]
    child = "".join(child_keys)
  return child


# Round Top X (set to population size) - set to go to next round
def end_cull(results_sorted_end_evals, select_num):
  print(results_sorted_end_evals[0][1])
  print(results_sorted_end_evals[-1][1])
  print("----------")
  return [layout for layout, score in results_sorted_end_evals[:select_num]]


# Writes to CSV file: top one's name and score, worst one last round name and score
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
    results_generation_mutations = mult_mutants(results_cull_30, mutate, 10, 1)

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


generations(100000, population_size)

