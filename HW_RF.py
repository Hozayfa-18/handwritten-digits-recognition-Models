import pickle
import matplotlib.pyplot as plot
from joblib import load, dump
import numpy as np
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
# with open('./mnist.pkl', 'rb') as f:
#     mnist = pickle.load(f)

# train_data = mnist['data'][0:60000]
# train_labels = mnist['target'][0:60000]
# val_data = mnist['data'][60000:70000]
# val_labels = mnist['target'][60000:70000]

# rf_model = RandomForestClassifier(max_depth=2, random_state=0)
# rf_model = rf_model.fit(train_data, train_labels)

# predictions = rf_model.predict(val_data)
# print(classification_report(val_labels, predictions))

# dump(rf_model,'./RF_FINAL_MODEL.joblib')

rf_model = load('./RF_FINAL_MODEL.joblib')

import PIL

file = r"C:\Users\hozay\OneDrive\Desktop\HW_recognition\digits\digit1.png"
original_img = PIL.Image.open(file)
img_resized = original_img.resize((28, 28), PIL.Image.Resampling.LANCZOS)
img_resized = np.array(img_resized)
img_resized = img_resized[:,:,0]
img_resized = np.invert(np.array([img_resized]))
img_resized = img_resized[0,:,:]
print(img_resized)
white_threshold = 150
mask = img_resized > white_threshold
img_resized[mask] = 255
img_resized[~mask] = 0
plot.imshow(img_resized, cmap=plot.cm.binary)
plot.show()

img_pre = np.array(img_resized)
print(img_pre.shape)
img_pre = img_pre.reshape(784)
prediction = rf_model.predict([img_pre])
print("the Digit is: ",prediction[0])

plot.imshow(original_img, cmap=plot.cm.binary)
plot.show()