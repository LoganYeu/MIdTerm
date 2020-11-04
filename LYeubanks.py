fname = input("Please enter a file name: ")
fh = open(fname)

cheeses = list()
for line in fh:
    currentCheese = line.split()
    for tCheese in currentCheese:
        if not tCheese in cheeses:
            cheeses.append(tCheese)
            
cheeses.sort()

print (cheeses)

