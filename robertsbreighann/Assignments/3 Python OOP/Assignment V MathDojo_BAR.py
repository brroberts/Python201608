class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, param1, *params):
		if not isinsance(ele, (float, int)): continue
		self.result += ele

	if not params: return self
		
	for ele in param1:
			if not isinsance(ele, (float, int)): continue
			self.result += ele

	for ele2 in params:
			if not isinsance(ele2, (float, int)): continue
			self.result += ele2


	def subtract(self, param1, *params):
		if not isinsance(ele, (float, int)): continue
		self.result -= ele

	if not params: return self
		
	for ele in param1:
			if not isinsance(ele, (float, int)): continue
			self.result -= ele

	for ele2 in params:
			if not isinsance(ele2, (float, int)): continue
			self.result -= ele2






md = MathDojo()
print md.add(2).add(2,5).sbtract(3, 2).result
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
