
from urllib.request import urlopen

story = urlopen("https://sixty-north.com/")#open url
story_word = []

for line in story:
    line_word = line.decode('utf8').split()#binary to string = decode #list
    for word in line_word:
        story_word.append(word)#combine list

story.close()

print(story_word)