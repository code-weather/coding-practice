'''
- Create a function that'll have input of the required prompts (Can be stored in the main function)
- Append the parameter/argument into the list
- Create another function to view expenses
'''
import csv

def expense_lists (filename):
  a_list = []

  with open(filename) as file:
    reader = csv.reader(file)
    next(reader)
    for grocery in reader:
      a_list.append(grocery[2])

  return a_list

def main ():
  file = "data/expense.csv"
  print(expense_lists(file))

if __name__ == "__main__":
  main()