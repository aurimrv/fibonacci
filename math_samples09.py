class MathSamples:
	@staticmethod
	def fibonacci(n):
		if(n == 0):
			return 0
		if(n <= 2):
			return 1;
		return self.fibonacci(n-1) + self.fibonacci(n-2);
