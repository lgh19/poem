import random
import math
def enter_words():
    words = []
    print()
    print()
    print("Poem Generator")
    print()
    print("When finished enter \"done\" to create poem")
    print()
    word_input = 'temp'
    word_input = str(word_input)
    while word_input.lower != 'done':
        word_input = input("Enter a word: ")
        word_input = str(word_input)
        if word_input =='done':
            create_poem(words)
            break
        else:
            words.append(word_input)
    
def create_poem(word_array):
    original_array = word_array
    print()
    print("Poem:")
    print("-----------------")
    if len(word_array) == 0:
        print("No words were entered")
    else:
        numbers = []
        poem = []
        lines = []
        while len(numbers) < len(word_array):
            temp = random.randrange(0, len(word_array))
            if temp not in numbers:
                numbers.append(temp)

        total = 0
        while total < (len(word_array)-1):
            stop = (len(word_array)/2)
            stop = math.floor(stop)
            if stop ==1:
                stop = 2
            if stop == 0:
                line_break = len(word_array)-1
                break
            line_break = random.randrange(0, stop)
            total += line_break
            lines.append(line_break)
        
        i = 0
        for n in numbers:
            if n == lines[i]:
                print(word_array[n])
                poem.append(word_array[n])
                if (i+1)< len(lines):
                    i+=1
            else:
                print(word_array[n], end=" ")
                poem.append(word_array[n])

    print()      
    print("-----------------")
    
    print()
    print()
    again = input("Generate new poem with the same words? (Y/N)")
    again = str(again)
    if again.lower() =='y':
        create_poem(original_array)
    elif again.lower() =='n':
        new_poem = input("Do you want to make a new poem? (Y/N)")
        new_poem = str(new_poem)
        if new_poem.lower() == 'y':
            enter_words()

enter_words()
