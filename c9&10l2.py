#Jacob Sexton 7/1/25

filename = input("Enter the name of the file you wish to process: ")

try:
    #open
    file = open(filename, "r")
    #proccess
    text = file.read()
    #close
    file.close()

    words = text.split()
    total_words = len(words)

    capitalized_words = 0
    for word in words:
        #I love the .isupper, makes this so much simplier
        if word[0].isupper():
            capitalized_words += 1

    print("The file",filename,"contains", total_words,"words of which",capitalized_words, "are capitalized.")
    

except FileNotFoundError:
    print("Sorry, the file does not exist.")
