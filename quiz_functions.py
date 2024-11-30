import json

def load_data(filename):
    with open(filename, "r", encoding='utf-8') as f:
        return  json.load(f)

def get_user_level(data):
    user_input = input("Выберите уровень сложности \nлегкий, средний, тяжелый.\n").strip().lower()
    if user_input == 'легкий':
        return data["questions"][0]
    elif user_input == 'средний':
        return data["questions"][1]
    elif user_input == 'тяжелый':
        return data["questions"][2]
    else:
        print("Выбран уровень: легкий по умолчанию.")
        return data["questions"][0]

def base_program(words):
    answers = {}
    for word, translation in words.items():
        print(f"\nПрограмма: {word}, {len(translation)} букв, начинается на '{translation[0]}'...")
        user_answer = input("Ваш ответ: ").strip().lower()
        is_correct = user_answer == translation
        answers[word] = is_correct

        if is_correct:
            print(f"Программа: Верно! {word.capitalize()} — это {translation}.")
        else:
            print(f"Программа: Неверно. {word.capitalize()} — это {translation}.")

    return answers

def get_result(answers, levels):
    correct_answers = [word for word, correct in answers.items() if correct]
    incorrect_answers = [word for word, correct in answers.items() if not correct]
    score = sum(1 for correct in answers.values() if correct)

    print("Правильно отвечены слова:")
    for word in correct_answers:
        print(word)

    print("\nНеправильно отвечены слова:")
    for word in incorrect_answers:
        print(word)

    return levels.get(str(score), "Неизвестный ранг")

def save_results(name, answers):
    with open(f"{name}_result.json", "w", encoding='utf-8') as f:
        json.dump(answers, f, ensure_ascii=False, indent=4)
        print(f"Результаты сохранены в файл: {name}_results.json")