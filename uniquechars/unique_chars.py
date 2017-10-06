# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# Should print out:
# ["n", "g", "r", "m"]


def unique_characters(my_string):
    output = []
    for i in my_string:
        output.append(i)
    return output

        
print(unique_characters("anagram"))