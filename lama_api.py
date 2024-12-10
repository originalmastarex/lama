import requests


def main():
    ollama_url = "http://212.132.112.15:11434/api/chat"
    ollama_model = "llama3.1:8b-instruct-q5_K_M"

    initial_prompt = "Du bist ein Informationssystem, welches die Fragen von Nutzern bestmöglich beantworten soll."

    data = {
        "model": ollama_model,
        "messages": [
            {
                "role": "system",
                "content": initial_prompt
            },
        ],
        "stream": False,
    }

    while True:
        print("\n\nStelle deine Frage:")
        eingabe = input("> ")
        msg = {
            "role": "user",
            "content": eingabe,
        }

        data["messages"].append(msg)

        response = requests.post(ollama_url, json=data).json();
        answer = response["message"]

        data["messages"].append(answer)

        print(answer["content"])


if __name__ == "__main__":
    main()

print("Max der Kek")