import json


def get_json_data():
    with open("../files/questions.json", "r") as file:
        content = file.read()
    data = json.loads(content)
    return data


if __name__ == "__main__":
    json_data = get_json_data()

    for question in json_data:
        print(question["question_text"])
        for index, alternative in enumerate(question["alternatives"]):
            print(index + 1, "-", alternative)
        user_choice = int(input("Enter the answer: "))
        question["user_choice"] = user_choice

    score = 0
    for index, question in enumerate(json_data):
        if question["user_choice"] == question["correct_answer"]:
            score += 1
            result = "Correct Answer"
        else:
            result = "Wrong Answer"
        message = f"{index + 1}- {result}  Your answer: {question['user_choice']}, " \
                  f"Correct answer: {question['correct_answer']} "
        print(message)
    print(score, "/", len(json_data))
    print(json_data)
