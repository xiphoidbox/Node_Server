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
