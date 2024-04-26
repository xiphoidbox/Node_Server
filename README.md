## Key Features

- **Mask Detection Service:** Built using TensorFlow and Flask, this service analyzes images to detect if a person is wearing a mask. The service is accessible via a REST API that expects POST requests containing image data.
- **Spam Detection Service:** Utilizes machine learning models trained with scikit-learn and deployed using Flask to classify text as spam or not spam. The service offers an API endpoint for real-time spam detection and another for identifying common spam words in text.
- **Proxy Server:** Developed with Express.js and secured with Helmet.js, this server acts as an intermediary to route requests to the appropriate Flask service. It supports CORS and integrates environment variables for enhanced configuration.

## Technologies Used

- **Backend:** Flask, Express.js, TensorFlow, scikit-learn
- **Security:** Helmet.js, CORS
- **Data Handling:** PIL for image processing, joblib for model loading
- **Logging and Monitoring:** Morgan for logging HTTP requests

## Environment Setup

The services run on separate ports with Flask applications handling AI tasks and the Express.js application managing routing and security. CORS is configured to accept requests from specific domains, ensuring that services can be integrated into front-end applications seamlessly.

## Repository Structure

- `/mask_detector` - Contains the Flask application for the mask detection service.
- `/spam_detector` - Contains the Flask application for spam detection.
- `/proxy_server` - Contains the Express.js application that routes requests to the Flask services.

## Machine Learning Model Code

For those who wish to explore the machine learning models and their training code, concise descriptions are provided alongside the Google Colab notebooks:

- **Mask Detection Model:** The mask detection model is a convolutional neural network (CNN) trained to classify images as either containing individuals wearing masks or not. It utilizes TensorFlow for implementation. Initially, a dataset of labeled images is prepared, resized, and preprocessed for training. Data augmentation techniques like rotation, shifting, and flipping are applied to diversify the training set. The model architecture consists of convolutional layers followed by batch normalization and max-pooling, extracting features from images. To prevent overfitting, dropout and L2 regularization are incorporated. The model is trained using the Adam optimizer to minimize classification loss. After training, its performance is evaluated on a separate test set to measure its accuracy in distinguishing between masked and unmasked individuals. The code for this model can be accessed [here](https://colab.research.google.com/drive/1Z4UB3rhkJDJdTuyfrNFRJBVYR07d2a4t?usp=sharing).

- **Spam Detection Model:** The spam detection model, a logistic regression classifier trained with scikit-learn, categorizes emails as spam or non-spam (ham). It employs TF-IDF vectorization to convert email content into numerical features, enabling the model to discern spam from ham based on their unique characteristics. Furthermore, the model's coefficients unveil pivotal words or features influencing classification. Higher coefficients signify spam indicators, whereas lower coefficients denote non-spam traits. This model efficiently identifies and filters out unwanted spam emails, enhancing email security. The code for this model can be accessed [here](https://colab.research.google.com/drive/1TgGTZpoEaxdNyWcPoc3Zh0NyMFf-y997?usp=sharing).
