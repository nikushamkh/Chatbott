from random import choice


def get_random_response():
    random_list: list[str] = [
        "Please try writing something more descriptive",
        "Oh! it appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that",
        "i Can't answer that yet, please try asking something else.."
    ]

    return choice(random_list)


if __name__ == '__main__':
    for i in range(5):
        print(get_random_response())
