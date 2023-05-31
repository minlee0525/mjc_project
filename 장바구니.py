import streamlit as st 
import pandas as pd
import openpyxl as op
from openpyxl.drawing.image import Image
#openpyxl Image 클래스와 중복되므로 PIL은 pi로 설정
from PIL import Image as pi

values = st.slider(
    '상품가격 설정',
    0.0, 100000.0,(2500.0, 65000.0))
st.write('선택 범위:', values)

title = st.text_input(
    label='상품검색',
    placeholder='상품명 입력'
)
st.write(f'선택상품 : {title}')

# MySQL 서버 연결 설정
import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mart_item',
    charset='utf8'
)

# 입력된 상품 검색
if title:
    # SQL 쿼리문 작성
    query = f"SELECT * FROM itemdb WHERE PRDT_NM LIKE '%{title}%'"

    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # 검색 결과 출력
    if results:
        st.write("검색 결과:")
        for row in results:
            st.write(f"상품명: {row[6]}, 가격: {row[8]}")
    else:
        st.write("검색 결과가 없습니다.")

# 연결 종료
conn.close()
