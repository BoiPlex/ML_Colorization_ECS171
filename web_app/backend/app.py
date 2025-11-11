"""
Flask Backend for Image Colorization
"""

from flask import Flask

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    """TODO: Implement image colorization prediction endpoint"""
    pass


if __name__ == '__main__':
    app.run(debug=True)
