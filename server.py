from waitress import serve

from movies.wsgi import application

if __name__ == '__main__':
    serve(application, port='8000')
