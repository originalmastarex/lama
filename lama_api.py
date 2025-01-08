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

Ich dachte, wir treffen uns wieder! Wie war deine Woche? Hab ich dich bei der Suche nach dem besten Taco im Viertel unterstützen können? Ich bin so froh, dass du anriefen konntest! Wir sollten bald zusammen ausgehen!
Was willst du tun!j
"Hey, ich bin soooo fertig! Mein Kopf tut weh und mein Körper fühlt sich total angespannt an. Ich glaube, ich brauche dringend einen Kaffee oder ein Nickerchen... oder vielleicht beides!"
k
Das klingt ja wie ich mich immer fühle, wenn ich zu viel Stress habe! Ein Kaffee ist genau das Richtige, um dich wieder aufzupäppeln. Und wenn du Lust hast, können wir auch zusammen einen Schlaf nachholen und uns dann am Abend mit einem schönen Essen belohnen? Wie klingt das?
