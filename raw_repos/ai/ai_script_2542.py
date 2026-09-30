import hashlib

def generate_token(algorithm, size, encoding):
	token = hashlib.sha256(os.urandom(size//2)).hexdigest()[:size]
	return token