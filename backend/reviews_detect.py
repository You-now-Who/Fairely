import re
# import speech_recognition as sr
import nltk
from nltk.stem import WordNetLemmatizer
# nltk.download()
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
# # from keras.models import load_model
# from tensorflow.keras.models import load_model
# model = load_model('chatbot_model.h5', compile=False)
# import json
# import random


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



def check_all_messages(message, code):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    if code == "FAKE_REVIEW":
        response('YES', ['nice', 'product', 'cool', 'product', 'my', 'kids', 'love', 'it'], single_response=True)
        # response('NO', ["lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", ], single_response=True)
        

    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return "UNKNOWN" if highest_prob_list[best_match] < 1 else best_match

def get_secondary_response(user_input, code):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message, code)
    return response

# PREPROCESSING DATA
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))


if __name__ == '__main__':
        print(get_secondary_response("ProsAwesome build. Velocity sensitive keys. Built in arpeggiator and chord mode are very handy. Useful free software packages available. Light and travel friendly. Reasonable price.ConsTouchPads are a little hardOverall worth buying!", "FAKE_REVIEW"))