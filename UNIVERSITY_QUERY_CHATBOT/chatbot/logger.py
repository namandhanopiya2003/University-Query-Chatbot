import logging

# Sets up the log file and log format and saves all chat logs into 'chatbot.log'
logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Saves what the user said and what the bot replied into the log file
def log_conversation(user_input, bot_response):
    logging.info(f'User: {user_input}')
    logging.info(f'Bot: {bot_response}')
