import getModule
import levelOne
import levelTwo

lvlOne = levelOne.categories()
lvlTwo = levelTwo.subCategories(lvlOne)

data = getModule.getter(lvlOne, lvlTwo).json()
print(*data, sep = "\n\n")