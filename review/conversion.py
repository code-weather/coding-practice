def convert_to_upper(char):
  """ Complete this function with your solution """
  if char.lower():
    return char.upper()

def main ():
  print(convert_to_upper(str(input("Enter a value: "))))

if __name__ == "__main__":
  main()