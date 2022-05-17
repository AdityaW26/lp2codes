from nltk.chat.util import Chat, reflections

pairs =[

    [
        r"hey|hello|hi",
        ["Hi, how are you?"]
    ],
    [
        r"What is your name?",
        ["Hi, i am Chatty."]
    ],
    [
        r"My name is (.*)",
        ["Wow ! Thats a good name."]
    ]
]

print("Start chatting")
chat = Chat(pairs, reflections)
chat.converse()