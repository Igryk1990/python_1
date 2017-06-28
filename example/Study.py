import json

def choiseNumberBooks(path,number=10):
    fileBooks = open(path,'r')
    booksMap = json.load(fileBooks)
    fileBooks.close()
    choiseBooks = []
    remainingBooks = []
    for i in range(number):
        choiseBooks.append(booksMap['books'][i])
    for i in range(number,len(booksMap['books'])):
        remainingBooks.append(booksMap['books'][i])
    remainingBooksMap = {}
    choiseBooksMap = {}
    choiseBooksMap['books']=choiseBooks
    fileWriteRes01 = open("res01.json", "w")
    json.dump(choiseBooksMap, fileWriteRes01)
    fileWriteRes01.close()
    remainingBooksMap['books'] = remainingBooks
    fileWriteRes02 = open("res02.json", "w")
    json.dump(remainingBooksMap, fileWriteRes02)
    fileWriteRes02.close()

choiseNumberBooks('books',3)



