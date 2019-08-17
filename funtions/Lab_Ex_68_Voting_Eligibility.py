# Program to square an entered number using Lambda/Anonymous functions
def is_eligible_to_vote(age_now):
    return age_now >= 18


age = int(input('Enter Your Age - '))
if is_eligible_to_vote(age):
    print("Congratulations you are eligible to cast vote")
else:
    print("Sorry you are not eligible to cast vote")
