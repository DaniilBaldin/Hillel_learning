txt = "hello, this is a test message."
x = txt.capitalize()
print(x)

txt = "Hello, This Is A Test Message."
x = txt.casefold()
print(x)

txt = "Test Message"
x = txt.center(50)
print(x)

txt = "Test message. This is a test message."
x = txt.count("message")
print(x)

txt = "My name is Dåniil"
x = txt.encode()
print(x)

txt = "This is a test message!"
x = txt.endswith(".")
print(x)

txt = "M\te\ts\ts\ta\tg\te"
x = txt.expandtabs(5)
print(x)

txt = "This is a test message."
x = txt.find("Message")
print(x)

txt1 = 'My name is {name}, I\'m {age}'.format(name="Daniil", age=29)
txt2 = "My name is {0}, I'm {1}".format("Daniil", 29)
txt3 = "My name is {}, I'm {}".format("Daniil", 29)
print(txt1)
print(txt2)
print(txt3)

txt = "This is a test message."
x = txt.index("message")
print(x)

txt = "Test12"
x = txt.isalnum()
print(x)

txt = "Test message"
x = txt.isalpha()
print(x)

txt = "322544"
x = txt.isdecimal()
print(x)

txt = "201651616"
x = txt.isdigit()
print(x)

txt = "Test_message"
x = txt.isidentifier()
print(x)

txt = "test message!"
x = txt.islower()
print(x)

txt = "01201201240221"
x = txt.isnumeric()
print(x)

txt = "Is this\n a test message #1?"
x = txt.isprintable()
print(x)

txt = "                       "
x = txt.isspace()
print(x)

txt = "This Is A Test Message."
x = txt.istitle()
print(x)

txt = "TEST MESSAGE"
x = txt.isupper()
print(x)

myTuple = ("Audi", "BMW", "Honda")
x = "/".join(myTuple)
print(x)

txt = "apple"
x = txt.ljust(10)
print(x, "is my favorite fruit.")

txt = "This is a TEST MESSAGE"
x = txt.lower()
print(x)

txt = "     apple     "
x = txt.lstrip()
print("Of all fruits", x, "is my favorite")

txt = "My name is Taniil!"
my_name = txt.maketrans("T", "D")
print(txt.translate(my_name))

txt = "This is a test message number one"
x = txt.partition("message")
print(x)

txt = "This is a test text."
x = txt.replace("text", "message")
print(x)

txt = "This is a test message"
x = txt.rfind("test")
print(x)

txt = "This is a test message"
x = txt.rindex("message")
print(x)

txt = "This"
x = txt.rjust(30)
print(x, "is a test message")

txt = "This is a test message"
x = txt.rpartition("is")
print(x)

txt = "Honda, Audi, BMW"
x = txt.rsplit(", ")
print(x)

txt = "     apple     "
x = txt.rstrip()
print("Of all fruits", x, "is my favorite")

txt = "This is a test message"
x = txt.split()
print(x)

txt = "This is a test message,\n This is a test message."
x = txt.splitlines()
print(x)

txt = "This is a test message."
x = txt.startswith("This")
print(x)

txt = "     apple     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "This Is A Test MESSAGE."
x = txt.swapcase()
print(x)

txt = "This is a test message"
x = txt.title()
print(x)

# use a dictionary with ascii codes to replace 84 (T) with 68 (D):
my_dict = {84: 68}
txt = "My name is Taniil!"
print(txt.translate(my_dict))

txt = "This is a test message"
x = txt.upper()
print(x)

txt = "180"
x = txt.zfill(20)
print(x)