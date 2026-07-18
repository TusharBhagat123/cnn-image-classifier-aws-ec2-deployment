# CNN Image Classifier using Flask and AWS EC2

## Project Overview
This project is a CNN-based Image Classification web application built using TensorFlow and Flask. It classifies images into one of the CIFAR-10 classes.

## Features
- Upload an image
- Predict image class
- Display uploaded image
- Show prediction confidence
- Flask web interface
- Ready for AWS EC2 deployment

## Technologies Used
- Python
- TensorFlow / Keras
- Flask
- HTML
- CSS

## Project Structure
```
cnn-image-classifier-aws-ec2-deployment/
│
├── app.py
├── predict.py
├── train_model.py
├── model.keras
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── uploads/
└── static/
```

## Run the Project

```bash
pip install -r requirements.txt
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Author

Tushar Bhagat