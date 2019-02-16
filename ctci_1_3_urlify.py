def _move_pre_str_2_spaces_back(i, string, length, count):
	for j in range(count):
		string[length - i + count + 2 - j] = string[length - i + count - j]
		string[length - i + count - j] = ' '
	return string

def urlify(string, length):
	count = 0
	for i in range(1,length+1):
		if string[length - i] != " ":
			count += 1
		else:
			string = _move_pre_str_2_spaces_back(i, string, length, count)
			string[length - i] = '%'
			string[length - i + 1] = '2'
			string[length - i + 2] = '0'
			count += 3
	return string


if __name__ == "__main__":
	string = 'ab cd dadsada        '
	strl = list(string)
	trimmed_string = string.strip()
	length = len(trimmed_string)
	res = urlify(strl, length)
	final = ''.join(res)
	print('"' + string + '"')
	print('"' + final + '"')
