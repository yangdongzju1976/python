def cout_words(filename):
    try:
        with open(filename) as f:
            contents=f.read()
    except FileNotFoundError:
        print(f"Sorry,the file {filename}doesnot exist")
    else:
        words=contents.split()
        num_words=len(words)
        print(f"The file{filename}\thas about {num_words}words.")
filename="story.txt"
cout_words(filename)








































'''from random import choice
player=['a','d','e','g','f']
first_up=choice(player)
print(first_up)

try:
    print(5/0)
except ZeroDivisionError:
    print('you cant divide by zero')
'''