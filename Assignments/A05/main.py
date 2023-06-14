import csv
import subprocess


# Generate & Run the edited Family Tree data file (family_tree_data.csv)
subprocess.run(['python', 'helper.py'])


# Function Definition
def generate_dot_file(data_file):
  dot_file = "family_tree.dot"

  with open(dot_file, "w") as file:
    file.write("digraph FamilyTree {\n")
    
    for n in data_file:
      pid = n['pid']
      name = n['name']
      gender = n['gender']
      generation = n['generation']
      byear = n['byear']
      dyear = n['dyear']
      years = n['years']
      clan = n['clan']
      spouse_id = n['spouseid']
      parent_id1 = n['parentid1']
      parent_id2 = n['parentid2']

      # Identify gender based on the Node shape
      if gender == "M":
        shape = "box"
      else:
        shape = "circle"
        
      # Assign unique color to each of the clans
      def colorr():
        if clan == "Aztec":
          return f'red'
        elif clan == "Apache":
          return f'green'
        elif clan == "Quechan":
          return f'blue'
        elif clan == "Mazatec":
          return f'pink'
        elif clan == "Zapotec":
          return f'yellow'
        elif clan == "Suma":
          return f'orange'
        elif clan == "Mexica":
          return f'brown'

      # Nodes with clan attributes
      file.write(f'{pid} [label="Name: {name} \\n Gender: {gender} \\n Generation: {generation}\\n {byear}-{dyear} ({years})\\n Clan: {clan}", fillcolor="{colorr()}", style=filled, shape={shape}]\n'
      )

      # Edges: Spouse 
      if spouse_id != "":
        file.write(f'{pid} -> {spouse_id} [label="spouse"]\n')

      # Edges: Parents
      if parent_id1 != "":
        file.write(f'{parent_id1} -> {pid} [label="child"]\n')
      if parent_id2 != "":
        file.write(f'{parent_id2} -> {pid} [label="child"]\n')
        
    file.write("}")


# Read data from CSV files
def read_csv_data(filename):
  data = []

  with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      data.append(row)

  return data

# Generate a .dot file
family_data = read_csv_data("family_tree_data.csv")
generate_dot_file(family_data)