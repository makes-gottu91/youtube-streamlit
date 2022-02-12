import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('お問い合わせ1')
expander1.write('お問い合わせ1内容を書く')

expander2 = st.expander('お問い合わせ2')
expander2.write('お問い合わせ2内容を書く')

expander3 = st.expander('お問い合わせ3')
expander3.write('お問い合わせ3内容を書く')



# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# text = st.text_input('あなたの趣味をおしえてください')

# 'コンディション：', condition
# 'あなたの趣味は', text, 'です。'

# option = st.selectbox(
#     'あなたの好きな数字をおしえてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は', option, 'です。'

# if st.checkbox('show image'):
#     img = Image.open('./ダウンロード.jpeg')
#     st.image(img, caption='John Mayer', use_column_width=True)