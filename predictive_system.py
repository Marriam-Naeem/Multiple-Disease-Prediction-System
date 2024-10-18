import numpy as np
import pickle



loaded_model = pickle.load(open('heart_model.sav', 'rb'))
input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

input_data= np.asarray(input_data)

input_data = input_data.reshape(1,-1)

prediction = loaded_model.predict(input_data)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')