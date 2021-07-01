string_message = 'test message'
new_dict = {i: string_message.count(i) for i in string_message}
print(new_dict)
