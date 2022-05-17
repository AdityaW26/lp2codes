questions = [
    'Do you have cold?',
    'Do you have cough?',
    'Do you have sore throat?',
    'Do you experience any problem in breathing?',
    'Do you feel weakness in your body?',
    'Do you experience difference in taste?'
]

print("-------------------------------------------------------------------------------------------------")
print("Welcome to Covid-19 symptoms check center !")
print("We will ask a questionaire about the symptoms you are going through.")
print("Your answers to this questionaire will decide if you have Covid-19 or not.")
print("-------------------------------------------------------------------------------------------------")
print()

score = 0
for q in questions:
    yn = input("Q"+str(questions.index(q)+1) + ". " + q + " (y/n) - ")
    if yn=='y' or yn=='Y':
        s = int(input("On a scale of 1-10, how would you rate the symptom? - "))
        score += s
    print()
# max score 60
# 60-45 Extreme, 45-30 Severe, 30-15 Mild, 15-0 No

if score>=45:
    print("You are showing Extreme symptoms of Covid-19.")
    print("You are requested to visit nearest Covid-19 center.")
elif score>=30:
    print("You are showing Severe symptoms of Covid-19.")
    print("You are requested to consult a doctor and take necessary precautions.")
elif score>=15:
    print("You are showing Mild symptoms of Covid-19.")
    print("It may be a false positive case.")
    print("You are requested to take a Covid-19 test and isolate yourself for 14 days.")
else:
    print("You are showing No symptoms of Covid-19.")
    print("Congratulations you are free from Covid-19. But it is advised to remain isolated and take necessary precautions.")