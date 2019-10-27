# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, request, jsonify
from flask_cors import CORS
from lib import sound_analysis
import os

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/analyze', methods=['POST'])
def analyze():
    # if os.environ.get("ENVIRONMENT") is not "production":
    #     import pdb; pdb.set_trace()
    skip_web_conversion = request.headers.get('skip-webm') == 'true'
    result = sound_analysis.analyze(request.data, request.headers.get('x-user-id') or 'anon', skip_web_conversion=skip_web_conversion)
    classification = sound_analysis.get_speech_classification(result)
    result["classification"] = classification
    return jsonify(result=result)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
