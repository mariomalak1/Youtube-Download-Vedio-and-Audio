def get_type(mime_type_str):
	type_str = ""
	for i in mime_type_str[::-1]:
		if i == "/":
			break
		type_str += i
	return type_str[::-1]

def get_type_2(mime_type_str):
	counter = 0
	cond = True
	type_str = ""
	while(cond):
		if mime_type_str[counter] == "/":
			while(counter < len(mime_type_str) - 1):
				counter += 1
				type_str += mime_type_str[counter]

			cond = False
		counter += 1

