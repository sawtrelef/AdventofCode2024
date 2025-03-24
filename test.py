def hello(name=""):
    if name == False:
        name = ""
    if name != "":
        #name = name.lower()
        #first = name[0].upper()
        #name = first + name[1:]
        name = name.capitalize()
    elif name == "":
        name = "World"

    name = "Hello, " + name + "!"
    return name


test = "bUtTs"

hello = "Hello " + test.capitalize() + "!" if test != "" else "Hello World!"
hello = ("Hello, World!", "Hello, " + test.capitalize() + "!")[test != ""]
hello = {True:"Hello, World!", False: "Hello, " + test.capitalize() + "!"}[test == ""]

print(hello)

test = ""
hello = "Hello " + test.capitalize() + "!" if test != "" else "Hello World!"
print(hello)

test = hello()
print(test)

test = hello(False)
print(test)