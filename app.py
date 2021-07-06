from flask import Flask
import rakeAndSplay

app = Flask(__name__)

@app.route("/")
sigthAngle, resultant = chairAngles(15, 22)

print("Sighting:  {0} \nResultant: {1}".format(
    round(sigthAngle, 1), round(resultant, 1)))