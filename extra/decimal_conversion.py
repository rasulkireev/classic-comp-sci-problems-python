def decimal_to_binary_conversion(decimal: int) -> str:
  list_of_binaries = []

  while True:
    remainder = decimal % 2
    list_of_binaries.append(str(remainder))

    if decimal == 0:
      break

    decimal = int(decimal / 2)

  list_of_binaries.reverse()

  return "".join(list_of_binaries)


if __name__ == '__main__':
  binary = decimal_to_binary_conversion(123)
  print(binary)
