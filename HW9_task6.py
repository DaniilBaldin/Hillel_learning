# Шифровка сообщения
result = []
message = "encrypted message"
keys = {'a': 574, 'b': 242, 'c': 334, 'd': 394, 'e': 324, 'f': 584,
        'g': 264, 'h': 344, 'i': 284, 'k': 404, 'l': 414, 'm': 484,
        'n': 374, 'o': 564, 'p': 594, 'r': 504, 's': 364, 't': 384,
        'u': 494, 'v': 444, 'w': 572, 'x': 242, 'y': 332, 'z': 392,
        }
message = list(message)
# Получение соответствий цифр для букв.
for symbol in message:
    for key in keys:
        if key == symbol:
            result.append(keys[key])
print(result)

# Расшифровка сообщения
result_encrypted = []
encrypted_message = result
keys = {'a': 574, 'b': 242, 'c': 334, 'd': 394, 'e': 324, 'f': 584,
        'g': 264, 'h': 344, 'i': 284, 'k': 404, 'l': 414, 'm': 484,
        'n': 374, 'o': 564, 'p': 594, 'r': 504, 's': 364, 't': 384,
        'u': 494, 'v': 444, 'w': 572, 'x': 242, 'y': 332, 'z': 392,
        }
new_keys = {v: k for k, v in keys.items()}
print(new_keys)

for num in encrypted_message:
    for key in new_keys:
        if key == num:
            result_encrypted.append(new_keys[key])
print(result_encrypted)
final_result = ' '.join([str(elem) for elem in result_encrypted])
print(final_result)
