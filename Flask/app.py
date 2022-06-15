from flask import Flask, render_template, request, redirect
from flask import current_app
import numpy as np
import pandas as pd
import random
from hanspell import spell_checker
import warnings
warnings.filterwarnings('ignore')
from transformers import PreTrainedTokenizerFast,GPT2LMHeadModel
from utils import inference
from utils import textrank
from utils import preprocess

app = Flask(__name__)

GPT = None
GPT_tok = None

@app.route('/')
def index():
    menu = {'ho':1, 'm1':0, 'm2':0}
    return render_template('index.html', menu=menu)

@app.before_first_request
def before_first_request():
    global GPT, GPT_tok
    GPT_tok = PreTrainedTokenizerFast.from_pretrained("./static/models/koGPT2_tokenizer", bos_token='</s>', eos_token='</s>', unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')
    GPT = GPT2LMHeadModel.from_pretrained('./static/models/koGPT2_finetuned')

@app.route('/menu1', methods=['GET', 'POST'])
def menu1():
    menu = {'ho':0, 'm1':1, 'm2':0}
    if request.method == 'GET':
        return render_template('menu1.html', menu=menu)
    else:
        ori_question = request.form['question'].replace('\n','<br>')
        question = textrank.sentence_extraction(ori_question)
        answer = inference.make_answer(question, GPT, GPT_tok)
        answer = spell_checker.check(answer).as_dict()["checked"]

        front = ['안녕하세요. 법률 상담 AI 서비스입니다. 질문에 대한 답변드리겠습니다.',
                 '안녕하십니까? 당신의 상담 결과를 안내드리겠습니다.',
                 '안녕하세요. 상담 내용에 대한 답변드리겠습니다.']
        end = ['질문에 대한 충분한 대답이 됐길 바라며, 자세한 내용은 변호사와 대면하여 진행하시길 바랍니다.']
        random_n = random.randint(0, 2)
        answer = '&nbsp;' + front[random_n] + '<br>' + '&nbsp;' + answer + '<br>' + '&nbsp;' + end[0]

        return render_template('menu1_res.html', menu=menu, question=ori_question, answer=answer)

@app.route('/read', methods=['GET'])
def read():
    menu = {'ho':0, 'm1':0, 'm2':1}
    if request.method == 'GET':
        return render_template('read.html', menu=menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
