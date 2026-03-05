from os import walk

_, _, filenames = next(walk("C:\\Users\\Michael\\Python"))

print(filenames)
