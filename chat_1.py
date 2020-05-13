def read_file(filename):
	message = []
	with open(filename, 'r', encoding='utf-8-sig') as file:
		for line in file:
			message.append(line.strip())
	return message

def convert_message(message):
	convert_message = []
	person = None	#預設值為無
	for line in message:	#假如有人名則跳到下一次迴圈
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person :
			convert_message.append(person + ': ' + line + '\n')		
	return convert_message

def write_file(filename, message):
	with open(filename, 'w', encoding='utf-8') as file:
		for line in message:
			file.write(line)


def main():
	message = read_file('input.txt')
	message = convert_message(message)
	write_file('output.txt', message)

main()