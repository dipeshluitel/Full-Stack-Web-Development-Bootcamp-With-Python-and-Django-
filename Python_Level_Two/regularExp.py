import re
patterns = ['apple', 'ball', 'mango']
text = "we know apple a day keeps the Doctor Away"

for pattern in patterns:
    print(f"I'm searching for {pattern}")

    if re.search(pattern,text):
        print("Match")
    else:
        print("No match")