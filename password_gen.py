import sys, random, string

def gen_passwords(number=10, length=8):

	pwds = []

	if number > 100: number = 100
	if length > 100: length = 100

	for i in range(number):
		pwds.append(gen_password(length))
	
	return pwds

def gen_password(length = 8):
	
	passwd = ""
	last = "" 

	for i in range(length):
		
		last = next_char(last)

		passwd += last;

		if i%4==3 and i!=length-1:
			passwd += "-"

	return passwd

def next_char(last_char, use_sym=False):

	vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
	consonants = [i for i in string.letters if i not in vowels]
	symbols = ["@", "#", "$", "%", "&"]

	if not last_char:
		return random.choice(string.letters)

	if last_char in consonants or last_char in string.digits or last_char in symbols:
		return random.choice(vowels)

	if last_char in vowels:
		pct = random.randint(0, 100)

		if pct < 60:
			return random.choice(consonants)
		elif pct < 90:
			return random.choice(string.digits)
		elif use_sym:
			return random.choice(symbols)
		else:
			return random.choice(consonants)


if __name__ == '__main__':

	text = sys.argv[1]

	print gen_password(int(text))
