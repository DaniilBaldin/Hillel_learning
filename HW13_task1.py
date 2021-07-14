import json

if __name__ == '__main__':
    def main_func():
        pass


def some_func(*args, **kwargs):
    a = list(args)
    b = [a[i:i + 2] for i in range(0, len(a), 2)]
    result = {m: n for m in kwargs for n in b[:1]}
    return result


some_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
          name='name', last_name="last_name", age='age', salary='salary', job='job')

A = some_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
              name='name', last_name="last_name", age='age', salary='salary', job='job')

json_path = json.dumps(A)
print('json_data: ', json_path)
with open('/home/daniil/PycharmProjects/final_result.json', 'w') as file:
    file.write(json_path)
