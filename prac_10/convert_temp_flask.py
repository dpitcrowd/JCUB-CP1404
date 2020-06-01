from flask import Flask

app = Flask(__name__)

@app.route('/home/davide/my_python/convert')
@app.route('/home/davide/my_python/convert/<temp>')



def convert_celsius(temp):
    """ Convert Fahrenheit degrees in Celsius degrees"""
    celsius = (float(temp) - 32) / (9.0 / 5)
    return 'The temperature is {} celsius'.format(temp)


if __name__ == '__main__':
    app.run()
