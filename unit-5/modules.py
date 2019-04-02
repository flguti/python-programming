import stories as st

print(st.get_story())

story = {'tittle' : 'filme' , 'author' : 'someone'}
st.add_story(story)

rect = st.Rectangle(10,5)

print(rect.area())