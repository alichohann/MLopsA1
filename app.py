from flask import Flask, render_template, request
import joblib
import numpy as np
from PIL import Image, ImageOps
import base64
import io

app = Flask(__name__)

# Load the trained model
model = joblib.load("mnist_model.pkl")


@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None

    if request.method == "POST":
        # Get the drawing data from the POST request
        drawing_data = request.form["image"]

        # Process and preprocess the drawing data
        preprocessed_data = preprocess_drawing_data(drawing_data)

        # Make a prediction using the model
        prediction = model.predict([preprocessed_data])[0]

    return render_template(
        "index.html",
        prediction=prediction if prediction is not None else None
    )


def preprocess_drawing_data(drawing_data):

    # Decode the base64 image data and convert it to a NumPy array
    image_data = base64.b64decode(drawing_data)
    image = Image.open(io.BytesIO(image_data))
    image = ImageOps.grayscale(image)  # Convert to grayscale
    image = image.resize((28, 28))     # Resize to match the MNIST dataset
    image_array = np.array(image)

    # Flatten the 2D image array to a 1D array (784 values)
    preprocessed_data = image_array.reshape(784) / 255.0

    return preprocessed_data


if __name__ == "__main__":

    app.run(debug=True)

# For Docker
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
