# -*- coding: utf-8 -*-
"""InfluencerAI-Text-Summarizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SnEJVVcH3yQZJlGUywfWM5nx7IpgzBzB
"""

#this is to test out the best model for analysing large volumes as text

from transformers import pipeline

#model
model = pipeline("summarization") #model="sshleifer/distilbart-cnn-12-6")

def func(article):
  article_length = article.split()
  words = len(article_length)
  if words>900:
    return "Oops!😰, I can't summarize text that long, please shorten the text🥺"
  else:
    return (model(article, max_length=100, do_sample=False))

import gradio as gr

app = gr.Interface(fn=func, inputs="textbox", outputs="textbox", title="InfluencerAI-Summarizer")
app.launch()