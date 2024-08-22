import os

def generation_top_one():
  # Define the full file path
  file_path = os.path.join('data', 'layout_scores.csv')

  # Write layout to file
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(f"asdf,sdfg\n")


generation_top_one()