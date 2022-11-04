"""
This is main file
"""
import argparse
from flask import Flask, request, jsonify
from extract_questions_from_word import do_extraction

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'docx'}

APP = Flask(__name__, instance_relative_config=True)
APP.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP.config['JSON_AS_ASCII'] = False
HOST_PORT = 5006


def allowed_file(fname):
    """allowed file function"""
    return '.' in fname and \
           fname.rsplit('.', 1)[len(fname.rsplit('.', 1)) - 1].lower() in \
           ALLOWED_EXTENSIONS


@APP.route('/extract_questions', methods=['POST'])
def magic_link():
    """magic link function"""
    if request.method == 'POST':
        return jsonify(do_extraction(request.args['path']))
    return None


def main():
    """main function"""
    parser = argparse.ArgumentParser(description='table question extraction')
    parser.add_argument('-p', '--port', type=int, default=HOST_PORT, help='port number')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()
    if args.debug:
        APP.debug = True
    APP.run(host='0.0.0.0', port=args.port)


if __name__ == '__main__':
    main()
