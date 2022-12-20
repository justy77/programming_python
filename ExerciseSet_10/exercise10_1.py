file = "artists.txt"


def processing_the_file(file):
    f1 = open(file, "r+")
    input_ = f1.read()
    f2 = open(file, "w+")
    f2.write(input_)
    f1.close()
    f2.close()
    print(input_)


processing_the_file(file)
