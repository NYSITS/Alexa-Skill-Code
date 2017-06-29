#!/usr/bin/env python3

import random

questions = {
    'Who is president of USA?':
    ('\na. Myself\nb. His Dad\nc. His Mom\nd. Barack Obama\n', 'd'),
    'What is the capital of USA?':
    ('\na. Zimbabwe\nb. New York\nc. Washington\nd. Do Not Exist\n', 'c')
}

def ask_question(questions):
    item = random.choice(list(questions.items()))
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = input('Hit \"a", \"b", \"c" or \"d" for your answer\n>')
    return (attempt, answer)

tries = 0
for question_number in range(5):
    while True:
        attempt, answer = ask_question(questions)
        if attempt not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT!!! Only hit \'y\' or \'n\' for your response')
        elif attempt == answer:
            print('Correct')
            stop_asking = False
            break
        elif tries == 1: # Specify the number of tries to fail the answer        
            print('Incorrect!!! You ran out of your attempts')
            stop_asking = True
            break
        else:
            tries += 1
            print('Incorrect!!! Try again.')
    if stop_asking:
        break
