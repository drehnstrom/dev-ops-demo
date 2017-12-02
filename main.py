import logging
from Converter import Converter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    model = {"title":"Welcome DevOps Fans to our great program!!!!!!!!!"}
    return render_template('index.html', model=model)

@app.route("/temp-converter")
def tempconverter():
    model = {"title":"Temp Converter",
             "converter":Converter()}
    return render_template('temp_converter.html', model=model)
 
 
@app.route("/convert-temp", methods=['POST'])
def convert_temp():

    try:
        temptoconvert = float(request.form["temp"])
    except:
        temptoconvert = 0.0


    toC = request.form.get('toCelsius', False)
    conv = Converter()
    conv.setTemp(temptoconvert)

    if toC == False:
        conv.toFahrenheit()
    else:
        conv.toCelsius()


    model = {"title":"Temp Converter!",
             "converter":conv}
    return render_template('temp_converter.html', model=model)
    

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)