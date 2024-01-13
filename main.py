# TASK 1 - CHATBOT WITH RULE-BASED RESPONSES
import re
import long_responses as long 

def message_probability(user_message, recognized_words, single_response = False, required_words=[]):
    message_certainity = 0 
    has_required_words = True

    # To count how many number of words matches with the predefined list of words 
    for word in user_message:
        if word in recognized_words :
            message_certainity += 1 
    
    # To calculate the percentage of recognized words in a user mesage 
    percentage = float(message_certainity)/float(len(recognized_words))

    # To check if the user message contains all the required words
    # for word in required_words:
    #     if word not in user_message:
    #         has_required_words = False
    #         break
    has_required_words = all(word in user_message for word in required_words)


    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0 
    
def check_all_messages(message):
    highes_prob_list = {} 
    def response (bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highes_prob_list 
        highes_prob_list[bot_response] = message_probability(message, list_of_words,single_response,required_words)

#  Respones ---------------------------------------------------------------------------
    response('Hello!',['hello','hi','sup','hey','heyo'], single_response=True)
    response("I am doing great, and you?",['how','are','you','doing'],required_words=['how','you'])
    response("Thank you",['I','love','talking','with','you'],required_words="love")
    response(long.R_EATING,['what','are','you','eating'],required_words=['you','eat'])
    response(long.R_DOING,['what','are','you','doing'],required_words=['you','doing'])

    response(long.R_NAME,['what','is','your','name'],required_words=['your','name'])

    best_match = max(highes_prob_list, key=highes_prob_list.get)  # type: ignore

    return long.unknown() if highes_prob_list[best_match]<1 else best_match


# Function to get the response from the bot 
def getResponse(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response = check_all_messages (split_message)
    return response

# To check the response system
while(True) :
    print('Bot: ' + getResponse(input('You: ' )))
