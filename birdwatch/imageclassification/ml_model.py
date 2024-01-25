import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

# Disable GPU usage
tf.config.set_visible_devices([], 'GPU')


# # Provide the path to your saved model
print("Current working directory:", os.getcwd())

model_path = 'imageclassification/bird_classification_model.h5'
model = load_model(model_path)


# class_labels=['Abbott’s Babbler Malacocincla abbotti',
#  'Black Bittern (Dupetor flavicollis)',
#  'Blue-eared Kingfisher Alcedo meninting',
#  'Blue-naped Pitta Pitta nipalensis',
#  'Broad-billed Warbler Tickellia hodgsoni',
#  'Cheer Pheasant (Catreus wallichii)',
#  'Chestnut Munia Lonchura atricapilla',
#  'Cinereous Vulture Aegypius monachus',
#  'Golden Babbler Stachyris chrysaea',
#  'Gould’s Shortwing Brachypteryx stellata',
#  'Great Bittern Botaurus stellaris',
#  'Great Hornbill (Buceros bicornis)',
#  'Great Slaty Woodpecker Mulleripicus pulverulentus',
#  'Ibisbill Ibidorhyncha struthersii',
#  'Indian Courser Cursorius coromandelicus',
#  'Indian Grassbird - Graminicola bengalensis',
#  'Indian Nightjar Caprimulgus asiaticus',
#  'Knob-billed Duck Sarkidiornis melanotos',
#  'Northern Pintail Anas acuta',
#  'Painted Stork Mycteria leucocephala',
#  'Purple Cochoa Cochoa purpurea',
#  'Red-headed Trogon Harpactes erythrocephalus',
#  'Red-headed Vulture Sarcogyps calvus',
#  'Red-necked Falcon Falco chicquera',
#  'Ruby-cheeked Sunbird Anthreptes singalensis',
#  'Rusty-fronted Barwing Actinodura egertoni',
#  'Saker Falcon Falco cherrug',
#  'Silver-eared Mesia Leiothrix argentauris',
#  'Slaty-legged Crake Rallina eurizonoides',
#  'Spot-bellied Eagle Owl Bubo nipalensis',
#  'Sultan Tit Melanochlora sultanea',
#  'Swamp Francolin Francolinus gularis',
#  'Tawny-bellied Babbler Dumetia hyperythra',
#  'Thick-billed Green Pigeon Treron curvirostra',
#  'White-throated Bulbul Alophoixus flaveolus',
#  'White-throated Bushchat Saxicola insignis',
#  'Yellow-rumped Honeyguide - Indicator xanthonotus',
#  'Yellow-vented Warbler Phylloscopus cantator']

class_labels =['Malacocincla abbotti',
 'Dupetor flavicollis',
 'Alcedo meninting',
 'Pitta nipalensis',
 'Tickellia hodgsoni',
 'Catreus wallichii',
 'Lonchura atricapilla',
 'Aegypius monachus',
 'Stachyris chrysaea',
 'Brachypteryx stellata',
 'Botaurus stellaris',
 'Buceros bicornis',
 'Mulleripicus pulverulentus',
 'Ibidorhyncha struthersii',
 'Cursorius coromandelicus',
 'Graminicola bengalensis',
 'Caprimulgus asiaticus',
 'Sarkidiornis melanotos',
 'Anas acuta',
 'Mycteria leucocephala',
 'Cochoa purpurea',
 'Harpactes erythrocephalus',
 'Sarcogyps calvus',
 'Falco chicquera',
 'Anthreptes singalensis',
 'Actinodura egertoni',
 'Falco cherrug',
 'Leiothrix argentauris',
 'Rallina eurizonoides',
 'Bubo nipalensis',
 'Melanochlora sultanea',
 'Francolinus gularis',
 'Dumetia hyperythra',
 'Treron curvirostra',
 'Alophoixus flaveolus',
 'Saxicola insignis',
 'Indicator xanthonotus',
 'Phylloscopus cantator']


from PIL import Image

def predictClassLabel(image):
    # Load and preprocess the image
    img = Image.open(image)
    img = img.resize((224, 224))  # Adjust the size based on your model's input size

    # Convert the image to an array
    img_array = np.array(img) / 255.0  # Normalize pixel values to be between 0 and 1
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make predictions
    predictions = model.predict(img_array)

    # Assuming predictions is a one-hot encoded array, find the predicted class index
    predicted_class_index = np.argmax(predictions)

    # Print the predicted class label (replace 'class_labels' with your actual class labels)
    predicted_class_label = class_labels[predicted_class_index]
    print("Predicted Class Label:", predicted_class_label)
    return predicted_class_label

#to prevent the model loading when I am learning an API i have commented the above code with a dummy function

# the following code is just a dummy
# def predictClassLabel(image):
#     return "Dummy text"

