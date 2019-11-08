'''
Write a python program with appropriate comments that accepts an input text file from user and performs the following operations:

- Reads the file and finds the longest word in the file and writes the length of the longest word, longest word, and its line number in the source file to a result file (all the results should be in a single line separated by comma). Also, print the results on the console

- Writes another file that contains all lines starting and including the line that contains longest word in the source file till the end of file.

- If the input file is not found then the program should print appropriate error message and keep prompting the user until a valid file is entered. Please use exception handling to accomplish this.
'''

#getting input for file
def input_file():  
  while True:
    input_file = input("File name:")
    try:
      with open(input_file, 'r') as x:
        return x.readlines()         
    except EnvironmentError:
      print("Wrong name, try again!")

#length of the longest word, longest word, its line number
def result_file(longestword,wordline):
  x = open("result_file.txt", 'w')
  result = str(len(longestword)) + ", " + longestword + ", " + str(wordline)
  x.write(result)
  x.close

#longest word and the rest of the file
def result2_file(inputfile,wordline):
  y = open("result2_file.txt", 'w')
  for i in range(wordline,len(inputfile)):
    y.write(inputfile[i])
  y.close

def main():
  inputfile = input_file()
  wordline = 0
  longestword = ""
  cnt = 1
  for i in inputfile:
    longestword_of_line = sorted(i.split(), key = len)[-1]
    if len(longestword_of_line) > len(longestword):
      longestword = longestword_of_line
      wordline = cnt
    cnt += 1
  print(str(len(longestword)) + ", " + longestword + ", " + str(wordline))
  result_file(longestword,wordline)
  result2_file(inputfile,wordline)
main()
