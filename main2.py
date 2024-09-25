# PJ VanDussen
# 9/25/2024
# Psedocode Average Quiz Score

#Input
f_name = input('Please enter your first name\n')
score1 = float(input('Enter your first quiz score\n'))
score2 = float(input('Enter your second quiz score\n'))
score3 = float(input('Enter your thrid quiz score\n'))

#Process
total = score1 + score2 + score3 
a_score = total / 3

#Output
print(f'Hello {f_name}, your first score is {score1:.2f}.')
print(f'Your second score is {score2:.2f}.')
print(f'Your third score is {score3:.2f}.')
print(f'Your average score of the three quiz scores is {a_score:.2f}.')