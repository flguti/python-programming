


#reading a file
f = open('short_story.txt', 'r')
data = f.read()


#always close file after opening
f.close()

print(data)

#write to a file
f = open('short_story.txt', 'w')
f.write('This is now a new story\n')
