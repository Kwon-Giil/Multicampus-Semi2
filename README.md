# Multicampus-Semi2

### 빅데이터 프로젝트 2차: 민사 법률 상담 AI 모델

#####  네이버 지식인 법률 전문가 답변 **Q**uestion **A**nswering 모델 구성



#### Dataset

네이버 지식인 민사소송 및 집행 카테고리 전문가 답변

총 약 22,000건 (훈련용 18,000개 검증용 4,000 개)



#### Lib

Pytorch 1.11, networkx, hanspell, Mecab

 

#### Prep

불필요한 인사말 제거 및 네이버 맞춤법 검사기 API 사용

TextRank 알고리즘을 통해 Text Summarization

질문 및 답변에 대한 핵심 문장을 추출해 학습



#### Model

유사도 기반 모델과 Seq2Seq, Transformer 계열 모델 사용

질문의 유사도를 기준으로, 유사도가 높은 질문일 경우 동일한 답변 생성

 유사도가 낮은 질문이 입력됐을 때, 딥러닝 모델을 통해 자연어를 생성해 법률 상담에 대한 적절한 답변 생성

토큰의 길이가 짧을 경우, Seq2Seq 모델 통과 

길 경우, Transformer 계열 모델 통과

RNN 모델은 입력 문장이 길어졌을 시, Gradient Vanshing 문제가 발생하기 때문에, 해당하는 경우에 Attention Machnism을 사용한 Transformer 계열 모델을 사용

 

#### Postp

핵심 문장을 이용해 학습을 진행하므로, 생성된 문장 또한 적절한 후처리를 통해 답변의 형태로 가공

플라스크, 장고 외 하이브리드 앱 구현을 위한 프레임워크를 사용해 웹 혹은 하이브리드 앱 형태로 최종 출력물 제공

