from flask import Flask, render_template

from controllers.boulders_controller import boulders_blueprint
from controllers.blocs_controller import blocs_blueprint

app = Flask(__name__)

app.register_blueprint(boulders_blueprint)
app.register_blueprint(blocs_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)