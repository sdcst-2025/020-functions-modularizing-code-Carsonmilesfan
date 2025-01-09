def A():
    print("Hello")

def B():
    print("How are you")

def C():
    print("Hi")

def D():
    print("thats the wrong answer")

reaper = input("Enter a letter from A, B, or C => ")

if reaper == "A":
    A()
elif reaper == "B":
    B()
elif reaper == "C":
    C()
else:
    D()