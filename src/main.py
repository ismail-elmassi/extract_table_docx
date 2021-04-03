import argparse
import traceback
from flask import Flask, request, jsonify
from extract_questions_from_word import do_extraction

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'docx'}

app = Flask(__name__, instance_relative_config=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False 
HOST_PORT = 5006

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[len(filename.rsplit('.', 1)) - 1].lower() in ALLOWED_EXTENSIONS

@app.route('/extract_questions', methods=['POST'])
def magic_link():
    if request.method == 'POST':
    	return jsonify(do_extraction(request.args['path']))

def main():
    parser = argparse.ArgumentParser(description='table question extraction')
    parser.add_argument('-p', '--port', type=int, default=HOST_PORT, help='port number')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()
    if args.debug:
        app.debug = True
    app.run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc()
