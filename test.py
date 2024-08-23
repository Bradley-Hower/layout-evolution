import subprocess
import re

def analysis():
  analysis_text = subprocess.run(['./genkey', 'analyze', 'test'], capture_output=True, text=True)

  # Initialize the score variable
  score = None

  # Regex select the score: stringify analysis output, select group
  score = re.search(r"(?<=Score: )([0-9]*).([0-9]*)", str(analysis_text)).group(0)

  # Return the score if found, otherwise return zero
  score_output = score if score else "0"
  return score_output
