from flask import Flask, render_template
import uuid

app = Flask(__name__)

cache_id = str(uuid.uuid4())

@app.route('/4-hbnb/')
def hbnb():
    return render_template('4-hbnb.html', cache_id=cache_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
