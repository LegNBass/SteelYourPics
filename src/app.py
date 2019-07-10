import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    import os
    os.system('pwd && ls')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=os.environ.get('DEBUG', False)
    )