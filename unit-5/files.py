import re
#find_and_replace(file_name, find_what, replace_with)

def find_and_replace(file_name, find_what, replace_with):
    data = open(file_name)
    f = data.read()
    
    find_idx = f.find(find_what)
    part_before = f[:find_idx]
    part_after = f[find_idx + len(find_what):]
    new = part_before + replace_with + part_after
    print(new)
   

find_and_replace('short_story.txt', 'short', 'good')