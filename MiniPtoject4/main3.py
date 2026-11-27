import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)

print("Добро пожаловать в игру «Угадай животное»!")
user_input = input("Напишите START, чтобы начать игру: ").strip()

if user_input.upper() == "START":
    print("\nДумаю над загадкой... Пожалуйста, подожди \n")

    prompt = (
        "Придумай одно случайное животное для игры в угадайку. "
        "Также придумай ровно три запрещенных слова, которые нельзя использовать при объяснении этого животного. "
        "Верни ответ строго в таком формате:\n"
        "Животное: [Название животного]\n"
        "Запрещённые слова:\n"
        "1. [Слово 1]\n"
        "2. [Слово 2]\n"
        "3. [Слово 3]"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        print(response.text)

    except Exception as e:
        print(f"Произошла ошибка при обращении к API: {e}")
else:
    print("Жаль! Если захочешь сыграть, перезапусти программу и введи START.")