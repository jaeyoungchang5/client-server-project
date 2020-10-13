'''
Final Project - Web Startup
SBPD_library.py
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)
'''

class _ethnicities_database:

	def __init__(self):
		

	def load_ethnicities(self, ethnicity_file):
		f = open(ethnicity_file)
		for line in f:
			line = line.rstrip()

		f.close()

if __name__ == "__main__":
	edb = _ethnicities_database()
