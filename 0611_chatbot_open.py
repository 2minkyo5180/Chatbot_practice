import streamlit as st
from langchain_community.chat_models import ChatOpenAI

st.set_page_config(page_title="Pregunta lo que quieras") #페이지 이름 설정
st.title("Pregunta lo que quieras, estoy aqui para ayudarte") #페이지 메인 텍스트 설정

import os
#OpenAI 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def generate_response(input_text):
    llm=ChatOpenAI(temperature=0, model_name='gpt-4') #제작할 모델 설정
    st.info(llm.predict(input_text)) #입력한 질문에 대한 llm의 답변을 페이지에 출력

with st.form('Question'): #질문을 입력하고 버튼을 누르면 generate_response의 input_text로 설정됨
    #질문 입력 칸과 예시 질문 만들기
    text=st.text_area('Escribe tu pregunta: ',
                      "¿Qué tipo de modelos de texto proporciona OpenAI?")
    #버튼 활성화
    submitted=st.form_submit_button('ENVIAR')
    generate_response(text)
