import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from eunjeon import Mecab

data = pd.read_csv('../data/2.Textranked.csv')

def get_df_token(data):
    mecab = Mecab()
    q_pos = []
    for i in range(len(data)):
        q_pos.append(mecab.pos(data['Question'][i]))
    data['tokens'] = q_pos
    pos = ["NNG","NNP","VV","VA"]
    data['tokens'] = data['tokens'].apply(lambda x: [t for (t, p) in x if p in pos])
    return data

def get_ques_token(question):
    mecab = Mecab()
    ques_token = mecab.pos(question)
    ques_token = ques_remove(ques_token)
    return ques_token

def ques_remove(question) :
    pos = ["NNG","NNP", "VV","VA"]
    ques_token = [[t for (t, p) in question if p in pos]]
    return ques_token

def jaccard_similarity(data, question):

    union = set(data).union(set(question))
    intersection = set(data).intersection(set(question))
    jaccard_sim = len(intersection) / len(union)  

    return jaccard_sim

def jaccard_high(data, question, num):
    # data: 데이터프레임, question: 입력한 텍스트(질문), num: 자카드 유사도 상위 갯수
    data['jaccard_similarity'] = data['tokens'].apply(lambda x: jaccard_similarity(x, question[0]))
    return data[['Question', 'Answer', 'tokens', 'jaccard_similarity']].sort_values(['jaccard_similarity'], ascending=False)[:num]

def tokenized_output(tokens):
    return tokens

def cos_similarity(data, question):
    tfidf_vectorizer = TfidfVectorizer(analyzer='word',
                                       tokenizer=tokenized_output,
                                       preprocessor=tokenized_output,
                                       token_pattern=None)
    
    tfidf_data = tfidf_vectorizer.fit_transform(data['tokens'])
    tfidf_question = tfidf_vectorizer.transform(question)

    data['cosine_similarity'] = cosine_similarity(tfidf_data, tfidf_question).reshape(-1, )

    return data[['Question', 'Answer', 'tokens', 'jaccard_similarity', 'cosine_similarity']].sort_values(['cosine_similarity'], ascending=False)

def cos_high(data):
    if data['cosine_similarity'].iloc[0] >= 0.6:
        return data['Answer'].iloc[0]
    else:
        if len(question) < 200:
            print('seq2seq')
        else:
            print('koGPT2')

