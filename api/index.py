from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def load_tokenizer_and_model(model="microsoft/DialoGPT-small"):
    """
    Load tokenizer and model instance for some specific DialoGPT model.
    """
    # Initialize tokenizer and model
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForCausalLM.from_pretrained(model)

    # Return tokenizer and model
    return tokenizer, model


def chat_response(history):
    """
    Receive a response given a history
    """

    # Initialize tokenizer and model
    tokenizer, model = load_tokenizer_and_model()

    # Initialize history variable
    chat_history_ids = cur_input = bot_input_ids = None

    for entry in history.split("|"):
        cur_input = tokenizer.encode(entry + tokenizer.eos_token, return_tensors='pt')
        # chat_history_ids = [chat_history_ids, cur_input]
        bot_input_ids = [chat_history_ids, cur_input] if history != '' > 0 else cur_input

    chat_history_ids = model.generate(bot_input_ids, max_length=1250, pad_token_id=tokenizer.eos_token_id)

    return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens = True)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        if "history" in dic:
            message = chat_response(dic["history"])
        else:
            message = "I'm sorry, I didn't catch that"
        self.wfile.write(message.encode())
        return
