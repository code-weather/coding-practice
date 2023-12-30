def convert_to_upper(char):
  """ Complete this function with your solution """

  if int(char) < 65 or int(char) > 90:
    return ord(char)

def main ():
  print(convert_to_upper(str(input("Enter a value: "))))

if __name__ == "__main__":
  main()