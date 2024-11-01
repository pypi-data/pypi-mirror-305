from banglanlp.rootfinder import bstem,load_dataset

word = "বাংলাগুলো"
root_word = bstem(word)
print("Root form:", root_word)


def a():
    print(123)