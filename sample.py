def get_input(word : str) -> str:
    return input(f"enter {word}: ")

name = get_input("name of the little girl")
pet = get_input("type of pet")
adjective1 = get_input("adjective to describe the little girl")
adjective2 = get_input("adjective to describe the pet")
place = get_input("favorite place")
wish = get_input("wish or dream")

story = f"""
Once upon a time, there was a little girl named {name}. She was a very {adjective1} child 
who loved spending time with her {adjective2} {pet}, her best friend in the world.

One sunny afternoon, {name} and her {pet} decided to visit their favorite place, the {place}. 
As they sat together, watching the clouds drift by, {name} whispered to her {pet}, 
"I wish I could {wish} one day."

Her {pet} wagged its tail (or purred happily, depending on the kind of pet!) as if to say, 
"Don't worry, {name}, your dream will come true."

From that day forward, {name} worked hard to make her dream of {wish} a reality. 
And with her {pet} by her side, she knew that anything was possible.
The end.
"""
print("Here is the Story About a little girl!")
print(story)