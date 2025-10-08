# Science Quiz in Python
name= input("what's your name ?")
print('*********************************************************')
print(f'----------{name} Welcome to my science quiz!------------')
print('*********************************************************')          

intro=input('would you like to start the quiz (yes or no) ? ').lowere
def science_quiz():
    score = 0
    print("🔬 Welcome to the Science Quiz!\n")

    questions = [
        {
            "question": "1. What planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "2. What is H2O commonly known as?",
            "options": ["A. Oxygen", "B. Hydrogen", "C. Water", "D. Salt"],
            "answer": "C"
        },
        {
            "question": "3. What gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"],
            "answer": "B"
        },
        {
            "question": "4. What part of the human body controls balance?",
            "options": ["A. Heart", "B. Lungs", "C. Brain", "D. Ear"],
            "answer": "D"
        },
        {
            "question": "5. What is the speed of light?",
            "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 1,000 km/s", "D. 30,000 km/s"],
            "answer": "A"
        }
    ]

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}\n")

    print(f"🎯 You got {score}/{len(questions)} correct!")
    if score == len(questions):
        print("🌟 Excellent! You're a science genius!")
    elif score >= 3:
        print("👍 Good job!")
    else:
        print("🧩 Keep learning, you'll get better!")

science_quiz()
