

Letters = {'2':"abc",
     '3':"def",
     '4':"ghi",
     '5':"jkl",
     '6':"mno",
     '7':"pqrs",
     '8':"tuv",
     '9':"wxyz"}
# function that creates strings of given letters from ''numbers''
def combination(numbers,path,array_of_sign):
     # if its last digit, lest say You gave 456 and its start with g->gj->gjm (ang here add that string "gim" to the array_of_sign)
     if numbers == '':
          array_of_sign.append(path)
     else:
          # take first digit
          for number in Letters[numbers[0]]:
               #add first sign form digit
               path += number
               # start function again whit different parameters (lest say u start with '234' and now u have '34'
               combination(numbers[1:], path,array_of_sign)
               # if u append array_of_sign get back by one sign and repeat for another sign
               path = path[:-1]

# function checks if the given sequence of numbers is empty, if not combination starts
def letter_combination(numbers):
     if not numbers:
          return []
     else:
          array_of_sign = []
          path=''
          combination(numbers,path,array_of_sign)
          return array_of_sign
if __name__ == "__main__":
    val = input()
    print(letter_combination(val))

