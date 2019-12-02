# olive_tokenizer

구글의 [Sentence Piece](https://github.com/google/sentencepiece) 모델 기반 한국어 Tokenizer 입니다.
한국어 위키피디아를 학습데이터로 사용하였고, vocab size는 32,000개 입니다.

## 요구사항
`python`

# 설치
`pip install sentencepiece`
`git clone https://github.com/olive-ai/olive_tokenizer.git`

# 사용법
```
from olive_tokenizer import tokenizer_module

text = '알베르트 아인슈타인은 독일 태생으로 스위스와 미국에서 활동한 이론물리학자이다.'

#tokenization
tokens = tokenizer_module.tokenize(text)
# ['▁알베르트', '▁아인슈타인', '은', '▁독일', '▁태생', '으로', '▁스위스', '와', '▁미국에서', '▁활동한', '▁이론', '물리학', '자이다', '.']

original_text = tokenizer_module.detokenize(tokens)
# 알베르트 아인슈타인은 독일 태생으로 스위스와 미국에서 활동한 이론물리학자이다.
