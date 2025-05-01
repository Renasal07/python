def add_two_numbers_challenge():
    print("🧠 Welcome to the 'Add Two Numbers' Challenge!")
    print("👉 You will be given two numbers.")
    print("📝 Your task is to add them together and type the correct answer.")
    print("Let's begin!\n")

    # Two numbers for the user to add
    num1 = 4
    num2 = 7

    print(f"🤔 What is {num1} + {num2}?")

    try:
        # Get user input
        user_input = input("💬 Type your answer here: ")
        user_answer = int(user_input)

        # Check the answer
        correct_answer = num1 + num2
        if user_answer == correct_answer:
            print("✅ Correct! Great job!")
        else:
            print(f"❌ Oops! That's not right. The correct answer is {correct_answer}.")
    except ValueError:
        print("⚠️ That wasn't a number. Please enter a valid whole number next time.")

    print("\n🎉 Thanks for playing!")

add_two_numbers_challenge()