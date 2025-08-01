# A PYPTHON PROGRAM TO SOLVE SIMPLE QUIZ
print("WELCOME TO PYTHON SIMPLE QUIZ PLATFORM/APP")
print("You are given 4 questions and 3 options,select only the correct option\n")

running = True
import string

while running:
    user_choice = input("To exit this program, kindly enter ('q' to quit) or press ENTER to continue \n")
    if user_choice.lower() == 'q':
        print("GOOD BYE!! YOU EXITED FROM THE PROGRAM")
        break

    try:
        score = 0

        # Question 1
        print("1. what is the capital of Nigeria")
        print("A. Nigeria")
        print("B. Abuja")
        print("C. Calabar")
        answer1 = input("Choose an option: ").strip().upper()
        if answer1 == 'B':
            print("✅✅ CORRECT!! \n")
            score += 1
        else:
            print("❌❌ Wrong!! Try again")

        # Question 2
        print("2. Which country hosted the 17th BRICS Summit on July 6, 2025 ?: ")
        print("A. USA")
        print("B. Brazil")
        print("C. Canada")
        answer2 = input("select an option \n").strip().upper()
        if answer2 == 'B':
            print("✅✅ YOU ARE DOING GOOD!!")
            score += 1
        else:
            print("❌❌ Wrong choice, Try Agian!!")

        # Question 3
        print("3. What was the IMF's global growth forecast for 2025 ? \n")
        print("A. Raised to 3.0%")
        print("B. Below 3.0%")
        print("C. Raised to 2.5%")
        answer3 = input("Choose an option: ").strip().upper()
        if answer3 == 'A':
            print("✅✅ CORRECT!!")
            score += 1
        else:
            print("❌❌ Try Again!!")

        # Question 4
        print("4. what does CPU stand for ?")
        print("A. Central Personal Unit")
        print("B. Computer Processing Unit")
        print("C. Centreal processing Unit")
        answer4 = input("Choose an option: ").strip().upper()
        if answer4 == 'C':
            print("✅✅ CORRECR!!")
            score += 1
        else:
            print("❌❌ Wrong Choice")

        # Final Score
        print(f"Your Final score is: {score}/4")

        if score == 4:
            print("👏👏👏 Excellent!! You got all correct")

        elif score == 3:
            print("👏👏 you did well")

        elif score == 2:
            print("👏 you tried")

        elif score == 1:
            print("👎 practice more next time")

        else:
            print("👎👎 you perform poorly. practice harder next time")



    except ValueError:
        print("Invalid input")

