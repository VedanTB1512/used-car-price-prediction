
from array import array
import streamlit as st
import numpy as np
import pickle


st.title('WELCOME TO  CAR PRICE PREDICATION')

Location = st.selectbox(
     ' Location of car',
     ( 'Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur',
       'Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad'))

st.write('You selected:', Location)


Year= st.slider('year of car  ', 1999, 2019)
st.write("You selected ", Year, 'Car.')

Kilometer_driven= st.slider('Car kilometers driven', 20000,120000)
st.write("You selected ",Kilometer_driven, 'Kilometer_driven Car.')

Fuel_type = st.selectbox(
     'Fuel Type of Car',('CNG', 'Diesel', 'Petrol', 'LPG', 'Electric'))

st.write('You selected:', Fuel_type)

Transmission= st.selectbox(
     'Transmission of Car',('Manual', 'Automatic' ))

st.write('You selected:', Transmission)


Owner_Type= st.selectbox(
     'Owner Type of Car',( 'First', 'Second', 'Fourth & Above', 'Third'))

st.write('You selected:', Owner_Type)

if Location == "Mumbai":
    Location =  0
elif Location== "Pune" :
     Location = 1
elif Location == "Chennai":
     Location = 2
elif Location == "Coimbatore":
     Location = 3
elif Location== "Hyderabad":
     Location = 4
elif Location == "Jaipur":
     Location = 5
elif Location   == "Kochi" :
     Location = 6
elif Location =="Kolkata":
     Location = 7
elif Location == "Delhi":
     Location= 8
elif Location =="Bangalore":
     Location = 9
elif Location == "Ahmedabad":
     Location = 10
else:
     Location = 11


if Fuel_type == "CNG":
     Fuel_type =   0
elif Fuel_type=="Diesel":
     Fuel_type =  1
elif Fuel_type=="Petrol":
     Fuel_type =   2
elif Fuel_type =="LPG":
     Fuel_type =  3
elif Fuel_type =="Electric":
     Fuel_type = 4
else:
     Fuel_type = 5


if Transmission == 'Manual':
    Transmission =   0
elif Transmission =='Automatic' :
     Transmission = 1
else:
     Transmission = 2

if Owner_Type == "First":
     Owner_Type = 0
elif Owner_Type == "Second":
      Owner_Type =1
elif Owner_Type == "Third":
     Owner_Type = 2
elif Owner_Type == "Fourth & Above":
      Owner_Type =3
else:
      Owner_Type =4

Engine= st.number_input(label="Engine of car ", min_value=72.0, max_value=5998.0)
st.write('You selected:',Engine ,'CC')
Mileage= st.number_input(label="Mileage of car", min_value=0.0, max_value=33.54)
st.write('You selected:',Mileage ,'km/kg')
Power= st.number_input(label="Power	of car", min_value=34.2, max_value=560.0)
st.write('You selected:',Power ,'bhp')
Seats= st.number_input(label="Seats of car", min_value=0.0, max_value=10.00)
st.write('You selected:',Seats ,'seats')



inputs = np.array([[Location,2022-Year,Kilometer_driven,Fuel_type,Transmission,Owner_Type,Mileage,Engine,Power,Seats]])

#with open('model.pkl', 'rb') as f:
#    model = pickle.load(f)
model = pickle.load(open('model_rf.pickle','rb'))
prediction = model.predict(inputs)

if st.button('Predict'):
    st.write('Selling price of car is ', float(prediction),'Lakhs')
























