import random
import time

Operators = ["*", "+", "-"]
Total_problems = 10


def problem_generator():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    o = random.choice(Operators)
    expression = str(a) + " " + o + " " + str(b)
    answer = eval(expression)
    return expression, answer


wrong = 0
input("Press Enter to start!")
print("=====================")

start_time = time.time()

for i in range(Total_problems):

    expression, answer = problem_generator()
    while True:
        guess = input("Problem no. " + str(i + 1) + ": " + expression + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("=====================")
print("Nice work! You finished in " + str(total_time) + " seconds.")
