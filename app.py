from flask import Flask, Response, send_file
from flask_restful import Resource, Api, request
from waitress import serve

from datetime import datetime

import os
os.chdir('storage/')

auth = os.environ.get('APPAUTH')

app = Flask(__name__)
api = Api(app)

class fileTransfer(Resource):
    def get(self):
        reqAuth = request.headers.get('Authorization')
        if auth!=reqAuth:
            return Response('Unauthorised', mimetype='text/csv', status=401)
        else:
            path = request.headers.get('filename')
            if not path:
                files = 'Files on disk: \n' + '\n'.join(os.listdir())
                return Response(files, mimetype='text/csv', status=200)
            else:
                if os.path.isfile(path):
                    return send_file(path, as_attachment=True)
                else:
                    return Response('File not found', mimetype='text/csv', status=404)
    
    def post(self):
        reqAuth = request.headers.get('Authorization')
        if auth!=reqAuth:
            return Response('Unauthorised', mimetype='text/csv', status=401)
        
        # binary data that is sent
        data = request.get_data()

        # write to file
        dt = datetime.now().isoformat().replace(':','-')
        path = request.headers.get('filename')
        if not path:
            path = dt
        with open(path, 'wb') as f:
            f.write(data)
            f.close()

        return Response('Authorised', mimetype='text/csv', status=200)


api.add_resource(fileTransfer, '/')

if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host="0.0.0.0", port=5000)