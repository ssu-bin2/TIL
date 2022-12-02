import random

first = random.choice([0,1,2])
second = random.choice([0,1,2])
operator = random.choice(['+','-'])

question = f'{first} {operator} {second} = '
print(question, end = ' ')
user_answer = int(input())

if operator == "+":
    answer = first + second
elif operator == "-":
    answer = first - second

if user_answer == answer:
    print("정답입니다.")
else:
    print("오답입니다.")