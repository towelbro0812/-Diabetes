import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import *
if "data_dictionary" not in st.session_state:
    st.session_state.data_dictionary = {
        'HighBP': None,
        'HighChol': None,
        'CholCheck': None,
        'BMI': None,
        'Smoker': None,
        'Stroke': None,
        'HeartDiseaseorAttack': None,
        'PhysActivity': None,
        'Fruits': None,
        'Veggies': None,
        'HvyAlcoholConsump': None,
        'AnyHealthcare': None,
        'NoDocbcCost': None,
        'GenHlth': None,
        'MentHlth': None,
        'PhysHlth': None,
        'DiffWalk': None,
        'Sex': None,
        'Age': None,
        'Education': None,
        'Income': None
    }

def find_income_range_index(value):
    ranges = [30, 45, 60, 75, 105, 150, 225, 300, 450, 600]
    return next((i + 1 for i, v in enumerate(ranges) if value < v), 11)
def find_age_range_index(age):
    age_ranges = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    return next((i + 1 for i, v in enumerate(age_ranges) if age < v), 13)


HighBP = None
st.title('糖尿病簡易AI診斷系統')
HighBP = st.radio(
        "是否有高血壓？",
        ["Yes", "No"],
        index=None,
    )

HighChol = st.radio(
        "是否有高膽固醇？",
        ["Yes", "No"],
        index=None,
    )

CholCheck = st.radio(
        "過去5年內是否有檢查膽固醇？",
        ["Yes", "No"],
        index=None,
    )

bmi = st.slider(
        "請輸入您的BMI",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1,
        format=None,
    )

Smoker = st.radio(
    "是否有抽菸過至少100支香煙?",
    ["Yes", "No"],
    index=None
)

Stroke = st.radio(
    "是否(曾被告知)有中風？",
    ["Yes", "No"],
    index=None
)

HeartDiseaseorAttack = st.radio(
    "是否有冠心病或心肌梗塞？",
    ["Yes", "No"],
    index=None
)

PhysActivity = st.radio(
    "過去30天內是否有運動?(不包括工作)",
    ["Yes", "No"],
    index=None
)

Fruits = st.radio(
    "每日是否攝取水果？",
    ["Yes", "No"],
    index=None
)

Veggies = st.radio(
    "每日是否攝取蔬菜？",
    ["Yes", "No"],
    index=None
)

HvyAlcoholConsump = st.radio(
    "是否大量飲酒？(男性每週飲酒超過14杯,女性每週飲酒超過7杯)",
    ["Yes", "No"],
    index=None
)

AnyHealthcare = st.radio(
    "是否有任何健康照護？",
    ["Yes", "No"],
    index=None
)

NoDocbcCost = st.radio(
    "過去12個月內是否因費用問題無法看醫生？",
    ["Yes", "No"],
    index=None
)

GenHlth = st.radio(
    "您一般健康狀況如何？",
    ["Excellent", "Very good","Good","Not bad","Poor"],
    index=0
)

MentHlth = st.slider(
        "過去30天內有多少天心理健康不佳？以天數計算，範圍0-30",
        min_value=0.0,
        max_value=30.0,
        value=0.0,
        step=1.0,
        format=None,
    )

PhysHlth = st.slider(
        "過去30天內有多少天身體健康不佳？以天數計算，範圍0-30",
        min_value=0.0,
        max_value=30.0,
        value=0.0,
        step=1.0,
        format=None,
    )

DiffWalk = st.radio(
    "爬樓梯是否有困難？",
    ["Yes", "No"],
    index=None
)

Sex = st.radio(
    "您的性別？",
    ["男", "女"],
    index=None
)

Age = st.slider(
    "請輸入您的年齡",
    min_value=18,
    max_value=99,
    value=0,
    step=1
)

Education = st.radio(
    "您的教育程度？",
    ["沒上學", "小學畢業", "國中畢業", "高中畢業", "大學畢業", "碩士畢業或以上"],
    index=3
)

Income = st.slider(
    "您的年收入(萬)？",
    min_value=0.0,
    max_value=1000.0,
    value=0.0,
    step=1.0
)



st.session_state.data_dictionary['HighBP']   = 1 if HighBP == "Yes"   else 0
st.session_state.data_dictionary['HighChol'] = 1.0 if HighChol == "Yes" else 0.0
st.session_state.data_dictionary['CholCheck']= 1 if CholCheck == "Yes" else 0.0
st.session_state.data_dictionary['BMI']      = bmi
st.session_state.data_dictionary['Smoker']   = 1.0 if Smoker == "Yes" else 0.0
st.session_state.data_dictionary['Stroke']   = 1.0 if Stroke == "Yes" else 0.0
st.session_state.data_dictionary['HeartDiseaseorAttack'] = 1.0 if HeartDiseaseorAttack == "Yes" else 0.0
st.session_state.data_dictionary['PhysActivity'] = 1.0 if PhysActivity == "Yes" else 0.0
st.session_state.data_dictionary['Fruits']   = 1.0 if Fruits == "Yes" else 0.0
st.session_state.data_dictionary['Veggies']  = 1.0 if Veggies == "Yes" else 0.0
st.session_state.data_dictionary['HvyAlcoholConsump'] = 1.0 if HvyAlcoholConsump == "Yes" else 0.0
st.session_state.data_dictionary['AnyHealthcare'] = 1.0 if AnyHealthcare == "Yes" else 0.0
st.session_state.data_dictionary['NoDocbcCost'] = 1.0 if NoDocbcCost == "Yes" else 0.0
st.session_state.data_dictionary['GenHlth']  = float(["Excellent", "Very good","Good","Not bad","Poor"].index(GenHlth)+1)
st.session_state.data_dictionary['MentHlth'] = MentHlth
st.session_state.data_dictionary['PhysHlth'] = PhysHlth
st.session_state.data_dictionary['DiffWalk'] = 1.0 if DiffWalk == "Yes" else 0.0
st.session_state.data_dictionary['Sex'] = 1.0 if Sex == "男" else 0.0
st.session_state.data_dictionary['Age'] = find_age_range_index(Age)
st.session_state.data_dictionary['Education'] = float(["沒上學", "小學畢業", "國中畢業", "高中畢業", "大學畢業", "碩士畢業或以上"].index(Education)+1)
st.session_state.data_dictionary['Income'] = find_income_range_index(Income)


go = st.button("AI診斷")
if go:
    loaded_model = load_model('./models/Final_Model')
    data_unseen = pd.DataFrame([st.session_state.data_dictionary])
#     data_values = [1, 0.0, 1, 30.0, 1.0, 0.0, 1.0, 1, 1, 1, 0, 1, 0.0, 4.0, 3.0, 5.0, 0.0, 1, 9, 6.0, 9.0]
#     data_dictionary = {
#     'HighBP': data_values[0],
#     'HighChol': data_values[1],
#     'CholCheck': data_values[2],
#     'BMI': data_values[3],
#     'Smoker': data_values[4],
#     'Stroke': data_values[5],
#     'HeartDiseaseorAttack': data_values[6],
#     'PhysActivity': data_values[7],
#     'Fruits': data_values[8],
#     'Veggies': data_values[9],
#     'HvyAlcoholConsump': data_values[10],
#     'AnyHealthcare': data_values[11],
#     'NoDocbcCost': data_values[12],
#     'GenHlth': data_values[13],
#     'MentHlth': data_values[14],
#     'PhysHlth': data_values[15],
#     'DiffWalk': data_values[16],
#     'Sex': data_values[17],
#     'Age': data_values[18],
#     'Education': data_values[19],
#     'Income': data_values[20]
# }
#   data_unseen = pd.DataFrame(data_dictionary, index=[0])
    prediction = loaded_model.predict_proba(data_unseen)[:,1]
    # 將ndarray轉成list並且取第一個值然後百分比
    persent = round(prediction.tolist()[0]*100, 2)
    prediction = f"您有{persent}%有糖尿病的風險"
    if persent <= 50:
        st.success(prediction)
    else:
        st.warning("此為參考值，請務必諮詢醫師意見 ")
        st.warning(prediction)
