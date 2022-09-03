from insaneintents import GenericAssistant
import dotenv
import os
dotenv.load_dotenv()

modname = os.getenv("MODELNAME")

assistant = GenericAssistant('intents/intents.json', model_name='aina')
def start(train=True):
    if train:
        assistant.train_model()
        assistant.save_model()
    else:
        assistant.load_model()

done = False

def get(message, uname=None, cname=modname.capitalize()):
    x = str(eval('f"'+str(assistant.request(message))+'"'))
    return x

def cli():
    "Talk to the model in CLI, re-trains model before initialising CLI"
    while not done:
        m = input("IN@AINA<< :: ")
        res = get(m,uname="InSaiyan")
        print(res)