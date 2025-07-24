from flask import Flask, request
from middleware.parser_wrapper import secure_parse

app = Flask(__name__)

# In-memory store for user behavior (you could replace this with Redis or DB)
suspicious_users = {}

# Max violations before redirect
MAX_VIOLATIONS = 3

app = Flask(__name__)

@app.route("/scan-xml", methods=['POST'])
def upload():
    xml_data = request.data.decode()
    alerts = secure_parse(xml_data)

    if isinstance(alerts, list) and any("[!]" in a for a in alerts):  # flagged
        return "\n".join(alerts), 400
    return "Accepted", 200


@app.route('/blocked')
def blocked():
    return "<h2>You have been blocked due to repeated suspicious activity.</h2>", 403


@app.route('/')
def index():
    return '''
    <h2>Paste XML here</h2>
    <form action="/scan-xml" method="post" enctype="multipart/form-data">
        <textarea name="xml" rows="20" cols="80"></textarea>
        <input type="submit" value="Scan">
    </form>
    '''


@app.before_request
def preprocess_request():
    # For form-encoded submissions (not just raw XML)
    if request.method == 'POST' and request.content_type != 'application/xml':
        if 'xml' in request.form:
            request._cached_data = request.form['xml'].encode()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
