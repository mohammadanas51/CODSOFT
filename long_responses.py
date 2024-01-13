import random

R_EATING = " I dont like eating anything because I am a bot!"

R_DOING = "I am assisting you with your queries!"

R_NAME = "My name is Chatterbox!"


def unknown() :
    response = ["I'm sorry, I didn't quite understand that. Can you please rephrase your question?",
                "I'm not sure I follow. Could you provide more details or ask in a different way?",
                "Oops! It seems like I'm not on the same page. Mind giving me another shot with a different question?",
                "Can you please provide more context or ask a different question?"][random.randrange(4)]
    return response