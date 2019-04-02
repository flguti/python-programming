from random import randint

stories = [{'title': 'The Lord of the Rings', 'author': 'JRR Tolkien'},
{'title': 'The Great Gatsby', 'author': 'F Scott Fitsgerald'},
{'title':'Harry Potter Series', 'author': 'JK Rowling'}]


def get_story():
   idx = randint(0, len(stories) - 1)
   return stories[idx]

def add_story(story):
    stories.append(story)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = (self.length * self.width)
        return area