'''Our program will randomly set an arithmetic question for us to answer. If
we get the answer wrong, the program will display the correct answer
and ask if we want to try a new question. If we get it correct, the program
will compliment us and ask if we want a new question. In addition, the
program will keep track of our scores and save the scores in an external
text file. After each question, we can key “-1” to terminate the program.
'''
from random import randint, choice
from os import remove, rename
# def getUserPoint(username):
#     '''This function accepts one parameter, userName. It then opens the file
#     "user_scores.txt" in "r" mode.
#     '''
#     # users_file = open('user_scores.txt', 'r')
#     list_content = []
#     new_str = ''
#     try:
#         with open('user_scores.txt', 'r') as users_files:
#             for line in users_files:
#                 list_content += line.split(', ')
#             for i in range(len(list_content) - 1):
#                 if username in list_content:
#                     users_files.close()
#                     username_index = list_content.index(username)
#                     return int(list_content[username_index + 1])
#     except IOError:
#         user_files = open('user_scores.txt', 'w')
#         user_files.close()
#         return '-1'
#     print(new_str)
#     print(list_content)
# print(getUserPoint('Ann'))
# def updateUserPoints(newuser, username, score):
#     if newuser:
#         users_files = open('user_scores.txt', 'a')
#         username_score = f"\n{username}, {score}"
#         users_files.write(username_score)
#         users_files.close()
#     else:
#         temporary_userfile = open('userScores.tmp', 'w')
#         with open('user_scores.txt', 'r') as users_files:
#             for line in users_files:
#                 temporary_userfile.write(line)
#print(updateUserPoints(True, 'Benny', '158'))
def generate_question():
    operators = ['', '', '', '']
    operands = [0, 0, 0, 0, 0]
    operator_dict = {
        1: '+',
        2: '-',
        3: '*',
        4: '**',
    }
    for i in range(len(operands)):
       operands[i] = randint(1, 9)
    for i in operators:
        operators += operator_dict[randint(1, 4)]
    question_string = ''
    for i in operands: 
        random_operator = choice(operators)
        question_string += str(i) + random_operator
    print(question_string)
    print(eval(question_string))
generate_question()