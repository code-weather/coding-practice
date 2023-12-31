def convert_to_upper(char):
  """ Complete this function with your solution """

  ascii_value = ord(char)
  lower_case = chr(ascii_value - 32)

  if 97 <= ascii_value <= 122:
    return lower_case
  elif 65 <= ascii_value <= 90:
    return char
  return "?"

def main ():
  print(convert_to_upper(str(input("Enter a value: "))))

if __name__ == "__main__":
  main()