from flask import Flask, request
from middleware.parser_wrapper import run_xxe_check

app = Flask(__name__)

# In-memory store for user behavior (you could replace this with Redis or DB)
suspicious_users = {}

# Max violations before redirect
MAX_VIOLATIONS = 3




app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    xml_data = request.data.decode()

    if run_xxe_check(xml_data):
        return "Blocked: Suspicious XML detected", 400

    return "XML accepted and safe to process", 200



@app.route('/blocked')
def blocked():
    return "<h2>You have been blocked due to repeated suspicious activity.</h2>", 403


@app.route('/')
def index():
    return '''
        <h2>Upload XML</h2>
        <form method="POST" action="/upload">
            <textarea name="xml" rows="10" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''


@app.before_request
def preprocess_request():
    # For form-encoded submissions (not just raw XML)
    if request.method == 'POST' and request.content_type != 'application/xml':
        if 'xml' in request.form:
            request._cached_data = request.form['xml'].encode()


if __name__ == '__main__':
    app.run(debug=True)
