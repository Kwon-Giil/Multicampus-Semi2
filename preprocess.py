import kss
from hanspell import spell_checker
import re

def spell_check(text):
    try:
        if len(text) > 500:
            pass
        else:
            text = spell_checker.check(text).as_dict()["checked"]
    except:
        pass
    return text

def sentence_split(text):
    sen = []
    for sent in kss.split_sentences(text):
        sen.append(sent)
    result = '\n'.join(sen)
    return result

def clean_text(text):
    text = re.sub(r'[@%\\*=()/~&\+á?\xc3\xa1\-\|\:\;\!\-\,\_\~\$\'\"\“]', '', text) #remove punctuation 
    text = re.sub(r'\.\.+', '.', text) #점이 두 개 이상 반복되는 부분 제거
    text = re.sub(r'\u200B', '', text) #폭 없는 공백 제거
    text = text.lower() #lower case 
    text = re.sub(r'\s+', ' ', text) #remove extra space 
    text = re.sub(r'<[^>]+>','',text) #remove Html tags
    text = re.sub(r'\.', '', text) #점 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)
    text = re.sub('[ +]', " ", text)
    text = re.sub("\n", "", text)
    text = re.sub("[A-Za-z]", "", text)
    text = re.sub('[0*]', '', text)
    text = re.sub(r'\s+', ' ', text) #remove spaces
    text = re.sub(r"^\s+", '', text) #remove space from start 
    text = re.sub(r'\s+$', '', text) # remove space from the end
    return text 