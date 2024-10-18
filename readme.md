# Image to Text with Translation

This project is a web application that allows users to upload images, extract text using Optical Character Recognition (OCR), and translate the extracted text into different languages. The application is built using Flask and integrates with Google Translate for translation functionality.

## Features

- Upload an image and extract text from it.
- Auto-detect the language of the extracted text.
- Translate the text into the desired target language.
- Responsive design for both desktop and mobile devices.
- View the original text alongside its translation in a clear format.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Google Cloud Translation API**: For translating text between languages.
- **Tesseract OCR**: An OCR engine for extracting text from images.
- **HTML/CSS**: For structuring and styling the web application.

## Installation

To get started with this project, follow the instructions below:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-to-text-translation.git
   cd image-to-text-translation
   ```

2. Create a virtual environment (optional):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment (optional):
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```
    - On macOS/Linux:
    ``` bash
    source venv/bin/activate
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    required to install [tesseract-ocr](https://github.com/tesseract-ocr/tesseract)

5. Set up your Google Cloud credentials for the Translation API.

6. Run the application:
    ```bash
    python server.py
    ```

7.Open your browser and go to http://LOCAL_IP_ADDRESS:5000 to access the application.

Usage
1. Choose an image file that contains text.
2. Select the source language (or use auto-detect).
3. Choose the target language for translation (default is Simplified Chinese).
4. Click "Upload and Translate" to process the image.
5. View the original and translated text displayed side by side.


Acknowledgments
- Flask for the web framework.
- Tesseract OCR for the OCR functionality.
- Google Cloud Translation API for language translation.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome!
