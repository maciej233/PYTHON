#!/home/maciej/environments/flask/bin/activate/python python3
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    