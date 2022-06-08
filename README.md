# Multicampus-Semi2
## Best-M4.t3 : 법률 상담 AI
#### Description
 법률 상담의 어려움을 해결하기 위해, 네이버 지식인 전문가 답변을 통해 학습한 AI 모델을 구현해 법률적인 질문에 대한 답변을 생성해주고자 한다

#### Dataset
 네이버 지식인 민사소송 및 집행 카테고리 전문가 답변 약 18,000건
 (훈련용 15,000 건, 검증용 3,000건)

#### Libs
 Pytorch 1.11
 networkx, hanspell, Mecab

#### Models
 Similarity Model (cos-similarity)
 Seq2Seq Model (Bi-GRU, skip-connection, Attention Module)
 koBigBird

#### Results

#### Contributors
 멀티캠퍼스 2차 Semi Project 3조입니다
 신재웅(), 권기일(), 강신웅(), 박찬규