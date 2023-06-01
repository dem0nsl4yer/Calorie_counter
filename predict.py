import tensorflow
from PIL import Image
import requests
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.image as img

def predict_class(model, images, show = True):
  for img in images:
    img = image.load_img(img, target_size=(299, 299))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img /= 255.                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    food_list = ['baby_back_ribs', 'baklava', 'beef_tartare', 'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'caprese_salad', 'carrot_cake', 'cheese_plate', 'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'creme_brulee', 'cup_cakes', 'donuts', 'falafel', 'foie_gras', 'french_toast', 'fried_calamari', 'fried_rice', 'frozen_yogurt', 'greek_salad', 'huevos_rancheros', 'ice_cream', 'lasagna', 'macaroni_and_cheese', 'miso_soup', 'mussels', 'onion_rings', 'oysters', 'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck', 'pizza', 'pork_chop', 'poutine', 'ramen', 'red_velvet_cake', 'risotto', 'seaweed_salad', 'shrimp_and_grits', 'spring_rolls', 'steak', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles']
    food_list.sort()

    pred_value = food_list[index]
    if show:
        plt.imshow(img[0])                           
        plt.axis('off')
        plt.title(pred_value)
        plt.show()
        print(pred_value)
    
    print('Reality check----->>>>')
    cal = {}
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    query = pred_value.replace("_"," ")
    response = requests.get(api_url + query, headers={'X-Api-Key': 's9S3fiY9BWYZtpCebS71Rg==Qk1nbauJKhKE9k8R'})
    if response.status_code == requests.codes.ok:
        result = response.json()
        #cal['total'] = result['items'][0]
        cal['Real name'] = result['items'][0]['name']
        #cal['Calories_consumed'] = f'"{.2f}".format(float(result["items"][0]["calories"])/100) cal/g'
        cal['Calories_consumed'] = "{:.2f} cal/g".format(float(result["items"][0]["calories"]) / 100)
        print(cal)
    else:
        print("Error:", response.status_code, response.text)