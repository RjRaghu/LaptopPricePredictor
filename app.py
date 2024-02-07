import streamlit as st
import pickle
import numpy as np
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

Company=st.selectbox('Bran',df['Company'].unique())

Type=st.selectbox('Type',df['TypeName'].unique())

Ram=st.selectbox('Ram(in Gb)',[2,4,6,8,12,16,24,32,64])

Weight=st.number_input('Weight of the Laptop')

Touchscreen=st.selectbox('Touchscreen',['No','Yes'])

Ips=st.selectbox('Ips',['No','Yes'])

screen_size=st.number_input('Screen Size')

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

Cpu=st.selectbox('CPU',df['Cpu brand'].unique())

hdd= st.selectbox('HDD(in Gb)',[0,128,256,512,1024,2048])
sdd= st.selectbox('SDD(in Gb)',[0,128,256,512,1024])

gpu=st.selectbox('Gpu',df['Gpu brand'].unique())
os=st.selectbox('Os',df['os'].unique())


if st.button('Predict Price'):
    # query
    ppi = None
    if Touchscreen == 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0

    if Ips == 'Yes':
        Ips = 1
    else:
        Ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([Company, Type, Ram, Weight, Touchscreen, Ips, ppi, Cpu, hdd, sdd, gpu, os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))