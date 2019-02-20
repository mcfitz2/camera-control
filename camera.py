import subprocess

class CameraController:
	def __init__(self, device):
		self.v4l = V4LCTL(device)
	def pan(self, value):
		self.v4l.set_ctrl("rotate_relative", value)
	def tilt(self, value):
		self.v4l.set_ctrl("rotate_relative", value)
	def rotate(self, value):
		self.v4l.set_ctrl("rotate_relative", value)
	def pan_reset(self):
		self.v4l.set_ctrl("pan_reset", "1")
	def tilt_reset(self):
		self.v4l.set_ctrl("tilt_reset", "1")
	def get_pan(self):
		return self.v4l.get_ctrl("pan_relative")
	def get_rotate(self):
		return self.v4l.get_ctrl("rotate_relative")
	def get_tilt(self):
		return self.v4l.get_ctrl("tilt_relative")
	def get_focus(self):
		return self.v4l.get_ctrl("focus")
	def focus(self, value):
		return self.v4l.set_ctrl("focus", value)
class V4LCTL:
	def __init__(self, device):
		self.device = device
	def _execute(self, *args):
		p = subprocess.Popen(["v4l-ctl", "-d", self.device]+args, stdout=subprocess.PIPE)
		return p.communicate()[0]
	def get_ctrl(self, name):
		pass
	def set_ctrl(self, name, value):
		pass

