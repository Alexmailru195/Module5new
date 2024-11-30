from quiz_functions import load_data, get_user_level, base_program, get_result, save_results
from levels import get_level

def main():
    data = load_data("data.json")
    user_name = input("Введите ваше имя: ").strip()

    test_words = get_user_level(data)
    test_answers = base_program(test_words)
    result = get_level(sum(1 for correct in test_answers.values() if correct))

    print(f"\nВаш ранг: {result}")
    save_results(user_name, test_answers)

if __name__ == "__main__":
    main()