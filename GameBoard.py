# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:48:41 2024

@author: ayyou
"""


def create_jeopardy_board():
    categories = ["Geography", "Science", "Computer Science", "Wentworth"]
    questions = [
        ["$100", "$200", "$300", "$400"],
        ["$100", "$200", "$300", "$400"],
        ["$100", "$200", "$300", "$400"],
        ["$100", "$200", "$300", "$400"]
                ]
    board = "|"
    for i in range(len(categories)):
        board += f"{categories[i]:<15}|"
    board += "\n"
    board += "+"
    for _ in range(len(categories)):
        board += "---------------+"
    board += "\n"

    for j in range(len(questions[0])):
        board += "|"
        for i in range(len(categories)):
            board += f"{questions[i][j]}           |"
        board += "\n"
    board += "+"
    for _ in range(len(categories)):
        board += "---------------+"
    board += "\n"
    return board

print(create_jeopardy_board())