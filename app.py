from flask import Flask, Response, send_file
from flask_restful import Resource, Api, request
from waitress import serve

from datetime import datetime

import os

auth = os.environ.get('APPAUTH')
port = os.environ.get('PORT')

app = Flask(__name__)
api = Api(app)

def log(text):
    f = open('storage/log.txt', 'a')
    f.write(text+'\n')
    f.close()

print(f'Starting server ...')

class fileTransfer(Resource):
    def get(self):
        reqAuth = request.headers.get('Authorization')
        if auth!=reqAuth:
            return Response('Unauthorised', mimetype='text/csv', status=401)
        else:
            path = request.headers.get('filename')
            if not path:
                files = 'Files on disk: \n' + '\n'.join(os.listdir('storage'))
                return Response(files, mimetype='text/csv', status=200)
            else:
                if os.path.isfile('storage/'+path):            
                    # log activity  
                    dt = datetime.now().isoformat()
                    log(dt+' << '+ path)
                    return send_file('storage/'+path, as_attachment=True)
                else:
                    return Response('File not found', mimetype='text/csv', status=404)
    
    def post(self):

        # validate creds
        reqAuth = request.headers.get('Authorization')
        if auth!=reqAuth:
            return Response('Unauthorised', mimetype='text/csv', status=401)
        
        # binary data that is sent
        data = request.get_data()

        # write to file
        dt = datetime.now().isoformat()
        path = request.headers.get('filename')
        if not path:
            path = dt.replace(':','-')

        # write
        with open('storage/'+path, 'wb') as f:
            f.write(data)
            f.close()

        # log activity  
        log(dt+' >> '+ path)

        return Response('Authorised', mimetype='text/csv', status=200)

api.add_resource(fileTransfer, '/')

if __name__ == '__main__':
    # app.run(port=port, host="0.0.0.0")
    serve(app, host="0.0.0.0", port=port)
    print(f'Started server at 0.0.0.0:{port}')