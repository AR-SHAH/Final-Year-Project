import tensorflow as tf
import pandas as p
import keras
#import KerasClassifier
#from keras.models import model_from_json
from keras.layers import Dense
from keras.layers import Input
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.layers import Dropout

data = p.read_csv('dataset for training.csv',header=None)

X = data.iloc[:,0:663]

Y = data.iloc[:,663:]

X_train, X_test, Y_train,Y_test = train_test_split(X,Y, random_state=1, test_size=0.30)

model = Sequential()
initializer = tf.keras.initializers.HeUniform()

model.add(Input(shape=663))

model.add(Dense(390, activation='relu',kernel_initializer=initializer))
model.add(Dropout(0.8))
model.add(Dense(390, activation='relu',kernel_initializer=initializer))
model.add(Dropout(0.8))
model.add(Dense(390, activation='relu',kernel_initializer=initializer))
model.add(Dropout(0.8))

model.add(Dense(5,activation = 'sigmoid'))

model.compile(optimizer="adam", loss="binary_crossentropy",metrics=['accuracy'])
model.fit(X_train,Y_train,batch_size=30,epochs = 300)

Y_pred = model.predict(X_test)
Y_pred = (Y_pred > 0.5)

temp_pre = []

for i in range(0,len(Y_pred)):
    w = []
    for j in range(0,5):
        if Y_pred[i][j] == False:
            w.append(0)
        else:
            w.append(1)
    temp_pre.append(w)
        
wrong = 0
correct = 0
ee = Y_test.values.tolist()

for i in range(0,len(Y_pred)):
    if temp_pre[i] == ee[i]:
        correct += 1
    else:
        wrong += 1

acc = (correct) / len(X_test)
acc = acc * 100 

print('acuracy on testing is: ',acc)



if acc>50:
    acc= str(acc)
    model.save(acc)
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)

# model.save_weights("model.h5")


# file = open('model.json', 'r')
# loaded  = file.read()
# file.close()

# #loaded_model = model_from_json(loaded)
# #loaded_model.load_weights("model.h5")

# #loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# #score = loaded_model.evaluate(X, Y, verbose=0)
# #print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))



# #rr1 = loaded_model.predict(X_test)




# model= keras.models.load_model(acc)
# pre=model.predict(X_test)
# # #rr = (rr1>0.5)

# abc = []


# e = Y_test.values.tolist()


# x=(pre>0.5)


# for i in range(0,len(x)):
#     w = []
#     for j in range(0,5):
#         if x[i][j] == False:
#             w.append(0)
#         else:
#             w.append(1)
#     abc.append(w)

# correct = 0
# wrong = 0

# for i in range(0,len(Y_test)):
#     if abc[i] == e[i]:
#         correct += 1
#     else:
#         wrong += 1

# acc = (correct) / len(X_test)
# acc = acc * 100 
# print('acuracy on testing is: ',acc)
