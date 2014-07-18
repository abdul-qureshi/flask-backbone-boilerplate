import os
from flask import Flask, render_template
from flask.ext import assets

app = Flask(__name__)
env = assets.Environment(app)

# Tells flask-assets where to look for coffee
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'coffee'),
    os.path.join(os.path.dirname(__file__), 'bower_components')
]

env.register(
    'js_view',
    assets.Bundle(
        'jquery/dist/jquery.min.js',
        assets.Bundle(
            'view.coffee',
	    filters=['coffeescript']
        ),
	output='js_view.js'
    )
)

@app.route('/')
def hello_world():
    """Render home page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
