import block

class blockchain:

	def __init__(self):
		self.chain = []
		self.chain.append(block(0, date.datetime.now(), {"text":"Genesis Block"}, "")

	def append(self, data):
		last_block = self.chain[-1]
		index = last_block.index + 1
		timestamp = date.datetime.now()
		hash = last_block.hash
		chain.append(block(index, timestamp, data, hash))

