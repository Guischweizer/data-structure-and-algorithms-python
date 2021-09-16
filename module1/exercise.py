# Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

n1 = int(input("Insert the first number: "))
n2 = int(input("Insert the second number: "))
resultsText = "The addition result is: {addition}, the subtraction is: {subtraction}, the multiplication: {multiplication}, and the divsion {division}"

resultsList = [ n1 + n2
  , n1 - n2
  , n1 * n2
  , n1 / n2
  ]

print(resultsText.format(addition = resultsList[0], subtraction = resultsList[1], multiplication = resultsList[2], division = resultsList[3]))
