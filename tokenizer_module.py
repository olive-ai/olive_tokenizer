
# coding: utf-8

# In[3]:


# author = Younggyun Hahm (hahmyg@gmail.com)

# SentencePiece tokenizer is used for training and tokenizing


# In[2]:


import sentencepiece as sp
import os


# In[5]:


try:
    dir_path = os.path.dirname(os.path.abspath( __file__ ))
except:
    dir_path = '.'
    
model_path = dir_path + '/data/tokenizer.model'
tokenizer = sp.SentencePieceProcessor()
tokenizer.Load(model_path)

def tokenize(text):
    tokenized = tokenizer.EncodeAsPieces(text)
    return tokenized

def detokenize(tokens):
    detokenized = ''.join(tokens).replace('▁', ' ').lstrip()
    return detokenized

