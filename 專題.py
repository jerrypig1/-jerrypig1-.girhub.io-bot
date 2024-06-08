import time
import discord
import pygame
from playsound import playsound
from discord.ext import commands
from selenium import webdriver
from moviepy.editor import *
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from selenium.webdriver.common.keys import Keys
import os , sys
import random
import cv2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pytube import YouTube
from translate import Translator
from discord.ext.commands import Bot 
import pytube
import youtube_dl
from revChatGPT.V1 import Chatbot
from opencc import OpenCC
import openai
from flask import Flask, request, render_template
openai.api_key = 'sk-lne8uach0oEeRbQx4FJDDnZ4SnH9v92PjYuGDGAC3sVJpR3m'
# openai.api_key = 'sk-kejmL7iGKEUEVS9vrrzvpkpKlLioLaFHUdvf3wvqSrrRFj6m'
openai.api_base = "https://api.chatanywhere.com.cn/v1"
def generate_dialogue(prompt):
    # 設置模型、回答的最大長度和生成的回答數量
    model = 'gpt-3.5-turbo'
    max_tokens = 1000
    num_responses = 1

    # with open('角色設定.txt','r',encoding='utf-8') as file:
    #     role_settings = file.read()
    # with open('角色設定1.txt','r',encoding='utf-8') as file:
    #     role_settings1 = file.read()
    # with open('角色設定2.txt','r',encoding='utf-8') as file:
    #     role_settings2 = file.read()
    # 調用OpenAI的Chat Completion API生成回答
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            # {"role": "system", "content": role_settings},
            # {"role": "system", "content": role_settings1},
            # {"role": "system", "content": role_settings2},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        n=num_responses,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # 解析回應並返回生成的對話
    dialogue = response.choices[0].message.content.strip()
    return dialogue
def translate_to_traditional(simplified_text):
    cc = OpenCC('s2tw')  # 創建OpenCC實例，指定從簡體轉換為繁體
    traditional_text = cc.convert(simplified_text)  # 執行簡體轉繁體轉換
    return traditional_text

with open('角色設定.txt','r',encoding='utf-8') as file:
    role_settings = file.read()
# with open('角色設定1.txt','r',encoding='utf-8') as file:
#     role_settings1 = file.read()
# with open('角色設定2.txt','r',encoding='utf-8') as file:
#     role_settings2 = file.read()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('專題.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form.get('user_input')
    user_input1 = request.form.get('user_input1')
    user_input2 = request.form.get('user_input2')
    # 在这里可以对用户输入的数据进行处理，例如打印它或进行其他操作
    # 提供對話的開頭
    prompt = f'請幫我推薦{user_input}首{user_input1}{user_input2}歌曲並在後面顯示youtube網址'
    print(prompt)
    # 生成對話
    dialogue = generate_dialogue(prompt)
    print(dialogue)
    # dialogue = translate_to_traditional(dialogue)
    # print(dialogue)
    # return dialogue
    dialogue_html = dialogue.replace('\n', '<br>')
    return dialogue_html
    

if __name__ == '__main__':
    app.run()
