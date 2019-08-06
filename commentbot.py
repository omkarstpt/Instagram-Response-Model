from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("insta_bot")

trainer = ListTrainer(chatbot)

with open("comments.txt") as fp:
    lines = fp.read().splitlines()
    print(lines)
    n = 2
    split_into_sublists_of_two = [lines[i * n:(i + 1) * n] for i in range((len(lines) + n - 1) // n)]
    for comment_response_pair in split_into_sublists_of_two:
        trainer.train(comment_response_pair)

comment = input("Enter the comment: ")
# if comment == "q":
#     break
response = str(chatbot.get_response(comment))
if "Thank" not in response:
    print("No response")
else:
    print(response)
# trainer.train(comment_file)

# trainer.train([
#     "good",
#     "Thanks!",
# ])

# trainer.train([
#     "nice click",
#     "Thanks!",
# ])

# trainer.train([
#     "looks good",
#     "Thanks!",
# ])

# trainer.train([
#     "wow",
#     "Thanks!",
# ])

# trainer.train([
#     "amazing",
#     "Thanks!",
# ])

# trainer.train([
#     "awesome",
#     "Thanks!",
# ])

# trainer.train([
#     "beautiful",
#     "Thanks!",
# ])

# trainer.train([
#     "pretty",
#     "Thanks!",
# ])

# trainer.train([
#     "bad",
#     "Sorry",
# ])
