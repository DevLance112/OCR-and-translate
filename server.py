from flask import Flask, render_template, request, make_response
from PIL import Image
import pytesseract
from googletrans import Translator
import os

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure upload folder exists

# Set path to Tesseract executable (if on Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the translator
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(image_path)

            # Extract text from the image
            extracted_text = pytesseract.image_to_string(Image.open(image_path).convert('L'))

            # Debugging: Print request.form to check for keys
            print(request.form)  # Log the entire form data for debugging

            # Use .get() method to safely access source and target languages
            # source_lang = request.form.get('source_lang', 'en')  # Default to 'auto'
            target_lang = request.form.get('target_lang', 'zh-cn')  # Default to English

            # Translate the extracted text
            translated_text = translator.translate(extracted_text, src="en", dest=target_lang).text

            # Split original and translated text into lines
            original_lines = extracted_text.split('\n')
            translated_lines = translated_text.split('\n')

            # Create a response and set cookies for original and translated text
            response = make_response(render_template(
                'mobile_index.html',
                original_lines=original_lines,
                translated_lines=translated_lines,
                image_path=image_path,
                zip=zip  # Pass the zip function explicitly
            ))
            response.set_cookie('original_lines', '\n'.join(original_lines))
            response.set_cookie('translated_lines', '\n'.join(translated_lines))

            return response

    # Retrieve data from cookies if available
    original_lines = request.cookies.get('original_lines', '').split('\n')
    translated_lines = request.cookies.get('translated_lines', '').split('\n')
    image_path = None

    return render_template(
        'desktop_index.html' if 'Mobile' not in request.user_agent.string else 'mobile_index.html',
        original_lines=original_lines,
        translated_lines=translated_lines,
        image_path=image_path,
        zip=zip
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
