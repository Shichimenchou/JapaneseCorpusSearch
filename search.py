with open("corpus.utf") as f:
    corpus = f.readlines()

query = input("Enter a search term: ")

for line in corpus:
    if query in line:
        print(line)
