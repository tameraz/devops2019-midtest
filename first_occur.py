import sys

# import the argument from the Terminal
inputname = sys.argv[1]
# Create the Dict
dict = {}
# Check if the char is already exist in the dict and if not he add it to the dict
for i in range(len(inputname)):
    if inputname[i] in dict:
        pass
    else:
        dict[inputname[i]] = i
# print the dict
print(dict)
