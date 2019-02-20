from flask import Flask
from flask import jsonify, render_template
import os

app = Flask(__name__, template_folder='.')
import camera

os.environ['DEVICE'] = "/dev/video0"
#os.environ['MJPG_STREAMER_URL'] = ""


camera = camera.CameraController(os.environ['DEVICE'])
mpg_url = os.environ.get('MJPG_STREAMER_URL',"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgUFQkVFhkVFhYYGBUaGRAhGB0iIiAWHx8kKDEjJCYsJx8fLT0tOTAuOjowIys/QDY4TzQ5OjQBCgoKDQ0OGBAPFzUeHSUtNS0tLSstKy0rMC83KzcuLTUrNS0tLS8tKy01Ny03LysrLSsxNTc2MC0rLS0rLSsrLf/AABEIAKgBLQMBIgACEQEDEQH/xAAbAAEBAQADAQEAAAAAAAAAAAAABgECBAUHA//EAC4QAQACAgEDAwIDCQEAAAAAAAABAgMRBBITIQYiMQVBFjJRFSMkQkNhcYGRFP/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwD4aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN0AwAAGgwAAAAawAAAAAAAAAAAAAAAAAAAAAAB7Xpzk/TcM8iPquKs1jpy491313xz4wz4/LeJmJ+3iN/DxQF3S3onJjtTPniOq0W3FMvV47kTXxWIrXU11r+bU2iYjTpcXJ6V431fiW31cOcFq5JtW9um1omItqY/P8A6msTqYSICo5FvTWPn8aOL0TinHl7kz/6JpF7Y5ikRuIv0xfUxOt/q73Kv6O5WXNauSMdbd+dRXLqs9cRj6dVifNY3rfTEz8eOmYkBU/RMXpW/C4lvq/KmvI3friK5p+86mZjxHj41vVvM7j2x2OJj9HxfBfNytaphm0dOe2rRae5XzGpnWtzrWtxFZ3uI4BVcmPSccCYwXtPJnHGp/e+20Y7zufGuqbxSs/NdT4+8xxw4vTFuJXvcmIyxi3/AF+q1+3O6zHT0xPcmNanXTHmYn5lwFraPQ97XnrtWIvj1Ed/3V7nu8/b2f2/TXl+mPH6V52GnHw1isdFcmS1e514uju3yebRqY1NKRG/O4+dIZuwUn038Nfs6eRzp/jI7msW82p9tppG4jWt9MfMT/j5ehlw+h6ditOZe3vnqnpzR7ZmIiLePMxFrW3ER4prW58xQC+n8DW6OPPLiMMe6bdrNuZmZ3WJiOrWp8bm2tRvetMz5PRHIrauTLWm923SmXxPx0/liY8edeaxbXzG4QQDlkrFbTFbxMfrG9T/AN8uIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//2Q==")
pan = 0
tilt = 0
focus = 0



@app.route("/settings")
def settings():
	return jsonify({"mpg_url":mpg_url, "device":os.environ['DEVICE']})
@app.route("/buttons")
def buttons():
	return render_template('./buttons.html', stream_url=mpg_url, focus_min=0, focus_max=1440, focus_step=1, pan_min=0, pan_max=1440,pan_step=1, tilt_min=0, tilt_max=1440, tilt_step=1)

#@app.route('/controls', methods=["GET"])
#def get_controls():
#	return jsonify({"control":""})
@app.route('/controls/pan', methods=["GET"])
def get_pan():
	return jsonify({"control":"pan", "value":pan})
@app.route('/controls/pan', methods=["PATCH"])
def set_pan():
	j = request.get_json()
	pan = j['value']
	return jsonify({"control":"pan", "value":pan})
@app.route('/controls/pan/reset', methods=["POST"])
def reset_pan():
	pass

@app.route('/controls/tilt', methods=["GET"])
def get_tilt():
	return jsonify({"control":"tilt", "value":tilt})
@app.route('/controls/tilt', methods=["PATCH"])
def set_tilt():
	j = request.get_json()
	tilt = j['value']
	return jsonify({"control":"tilt", "value":tilt})

@app.route('/controls/tilt/reset', methods=["POST"])
def reset_tilt():
	pass
@app.route('/controls/focus', methods=["GET"])
def get_focus():
	return jsonify({"control":"focus", "value":focus})
@app.route('/controls/focus', methods=["PATCH"])
def set_focus():
	j = request.get_json()
	focus = j['value']
	return jsonify({"control":"focus", "value":focus})