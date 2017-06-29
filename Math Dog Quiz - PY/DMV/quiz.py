#!/usr/bin/env python3

from random import randint

questions = [
    "What is 1 + 1?",
    "Who is the 45th President of the United States?",
    "True or False... The Toronto Maple Leafs have won 13 Stanley Cups.",
    "What was the last year the Toronto Maple Leafs won the Stanley Cup?",
    "True or False... The current Prime Minister of Canada is Pierre Elliot Tredeau."
]

answer_choices = [
    "a) 1 | b) 2 | c) 3 | d) 4\n> ",
    "a) Barack Obama | b) Hillary Clinton | c) Donald Trump | d) Tom Brady\n> ",
    "a) True | b) False?\n> ",
    "a) 1967 | b) 1955 | c) 1987 | d) 1994\n> ",
    "a) True | b) False?\n> "
]

correct_choices = [
    {"b", "2"},
    {"c", "donald trump"},
    {"a", "true", "t"},
    {"a", "1967"},
    {"a", "true", "t"}
]

answers = [
    "1 + 1 is 2",
    "The 45th President is Donald Trump",
    "The Toronto Maple Leaves have won 13 Stanley Cups",
    "The last time the Toronto Maple Leafs won the Stanley Cup was 1967",
    "The current Prime Minister of Canada is Justian Tredeau"
]

def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

if __name__ == "__main__":
    quiz()
