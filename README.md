# Brain Tumor Detection Using CNN

**Welcome to the Brain Tumor Detection project !**
**Created by : Avnee Joshi, Payal Hazari, Purvika Mandloi**

## About
- This project is a Flask-based web application designed for brain tumor detection. It focuses on developing a deep learning model using Convolutional Neural Networks (CNN) to automatically identify brain tumors from MRI images, distinguishing between tumorous and non-tumorous cases..

#### Key Features:
- **Data Augmentation**: Utilizes ImageDataGenerator for real-time data augmentation, enhancing the model's robustness and generalization.
- **Transfer Learning**: Leverages the pre-trained VGG19 architecture to extract high-level features from images.
- **Custom Layers**: Adds fully connected layers and dropout for regularization, tailored to the classification task.
- **Optimization**: Implements optimizers like SGD and Adam to fine-tune model performance.
- **Callbacks**: Includes ModelCheckpoint, EarlyStopping, and ReduceLROnPlateau to ensure efficient training and prevent overfitting.

#### Technologies Used:
- **TensorFlow/Keras**: The primary framework for building and training the CNN model.
- **Python**: The programming language used for all development tasks.

#### Objective:
- The goal of this project is to create an accurate and efficient tool that can assist healthcare professionals in diagnosing brain tumors from MRI scans, potentially aiding in early detection and treatment.

## Large Files
- Large files for this project are stored in AWS S3. You can download them using the links below:

- [VGG Unfrozen Model](https://brain-tumor-detector-largefiles.s3.amazonaws.com/vgg_unfrozen.h5)
- [VGG19 Model 01](https://brain-tumor-detector-largefiles.s3.amazonaws.com/vgg19_model_01.h5)
- [VGG19 Model 02](https://brain-tumor-detector-largefiles.s3.amazonaws.com/vgg19_model_02.h5)

Feel free to reach out if you have any questions or need further assistance!

