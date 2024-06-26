from flask import Flask, Response
from flask_restful import Resource, Api, request
from waitress import serve

from datetime import datetime
import os
os.chdir(r'/workspaces/puzzles/webserver/data/')
auth = os.environ.get('APPAUTH')

app = Flask(__name__)
api = Api(app)

class fileTransfer(Resource):
    def get(self):
        return {'doc': 'this is a test server for academic purposes'}
    
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

        # upload to disk
        fileList = '\n'.join(os.listdir())
        return Response(fileList, mimetype='text/csv', status=200)


api.add_resource(fileTransfer, '/')

if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host="127.0.0.1", port=5000)