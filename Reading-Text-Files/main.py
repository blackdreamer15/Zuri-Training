# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    with open("story.txt") as textfile:
        bio = textfile.read()
    return bio


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    num1 =text.count('as')
    num2 = text.count('would')
    return num1, num2


#readfile = read_file_content('story.txt')
#print(readfile)
#print(count_words())
