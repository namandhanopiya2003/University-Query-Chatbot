import logging

logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_conversation(user_input, bot_response):
    logging.info(f'User: {user_input}')
    logging.info(f'Bot: {bot_response}')
