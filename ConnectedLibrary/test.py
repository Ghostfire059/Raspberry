import os
import package
from package.Library import library

ISBN = "9782355927416"
lib = library.library("test")
print(lib.getName())
d_game = lib.getSerie("D-game")
patate = lib.getSerie("patate")
patate.setTitle("cornichon")
b = d_game.getBook(ISBN)
b.downloadCover()
b2 = patate.getBook(ISBN)
#b.rename("Darwin's Game")
print(lib)



"""
for file in os.listdir(os.path.join(os.getcwd(), "data")):
    print(file)

print(b1.getISBN())
s = serie.serie()
s.addBook(b1)
print(s.getBook(0).getISBN())

util = search.search()

name = util.name(b1.getISBN())
util.tearDown()

pathprint(name)
#img = util.cover(b1.getISBN())
#print(img.get_property("src"))
"""
