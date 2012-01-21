
def gen_guid():
	import uuid
	temp = []

	for i in range(10):
		temp.append(uuid.uuid4())

	return temp


def get_hashvalues(text):

	import hashlib
	
	results = {"md5" : "", "sha1" : "", "sha256" : "" }
	
	results["md5"] = hashlib.md5(text).hexdigest()
	results["sha1"] = hashlib.sha1(text).hexdigest()
	results["sha256"] = hashlib.sha256(text).hexdigest()

	return results

def ascii_table():
	import string

	ascii_pair = lambda char: char+": "+ str(ord(char))
	
	result = {}

	result["uppercase"] = map(ascii_pair, string.ascii_uppercase)
	result["lowercase"] = map(ascii_pair, string.ascii_lowercase)
	result["digits"] = map(ascii_pair, string.digits)
	result["punctuation"] = map(ascii_pair, string.punctuation)

	return result


