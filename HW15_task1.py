import json

with open("/home/daniil/PycharmProjects/HW.json", 'r') as json_file:
    data = json.loads(json_file.read())
print(data)


class Employees:
    pass

    def __init__(self):
        with open("/home/daniil/PycharmProjects/HW.json", 'r') as json_file:
            data = json.loads(json_file.read())
        print(data)

    @staticmethod
    def func(json_file):
        with open("/home/daniil/PycharmProjects/HW.json", 'r') as json_file:
            data = json.loads(json_file.read())
        print(type(data))
        for k, v in data.items():
            print(v)
        print(dict(data))

    @staticmethod
    def employee_names():
        with open("/home/daniil/PycharmProjects/HW.json", 'r') as json_file:
            data = json.loads(json_file.read())
        for employees in data['employee']:
            return employees['lastName']


    print(employee_names())

    @staticmethod
    def items_sorted():
        with open("/home/daniil/PycharmProjects/HW.json", 'r') as json_file:
            data = json.loads(json_file.read())
            for k, v in data.items():
                first_employee = v[0]
                list_x = [(i, n) for i, n in first_employee.items()]
                print(list_x)
                second_employee = v[1]
                list_x = [(i, n) for i, n in second_employee.items()]
                print(list_x)
                third_employee = v[2]
                list_x = [(i, n) for i, n in third_employee.items()]
                print(list_x)


# По значению определяете тип и сортируете по типу
result_int_f = []
result_string_f = []
result_float_f = []
result_none_f = []
result_bool_f = []
for k, v in data.items():
    first_employee = v[0]
    for x, y in first_employee.items():
        NoneType = type(None)
        if isinstance(y, bool):
            result_bool_f.append(x)
        elif isinstance(y, int):
            result_int_f.append(x)
        elif isinstance(y, str):
            result_string_f.append(x)
        elif isinstance(y, float):
            result_float_f.append(x)
        elif isinstance(y, NoneType):
            result_none_f.append(x)
result_first = {"Tom Cruise": {"int": result_int_f,
                               "string": result_string_f,
                               "float": result_float_f,
                               "none_type": result_none_f,
                               "bool": result_bool_f}}
result_int_s = []
result_string_s = []
result_float_s = []
result_none_s = []
result_bool_s = []
for k, v in data.items():
    second_employee = v[1]
    for x, y in second_employee.items():
        NoneType = type(None)
        if isinstance(y, bool):
            result_bool_s.append(x)
        elif isinstance(y, int):
            result_int_s.append(x)
        elif isinstance(y, str):
            result_string_s.append(x)
        elif isinstance(y, float):
            result_float_s.append(x)
        elif isinstance(y, NoneType):
            result_none_s.append(x)
result_second = {"Maria Sharapova": {"int": result_int_s,
                                     "string": result_string_s,
                                     "float": result_float_s,
                                     "none_type": result_none_s,
                                     "bool": result_bool_s}}

result_int_t = []
result_string_t = []
result_float_t = []
result_none_t = []
result_bool_t = []
for k, v in data.items():
    third_employee = v[2]
    for x, y in third_employee.items():
        NoneType = type(None)
        if isinstance(y, bool):
            result_bool_t.append(x)
        elif isinstance(y, int):
            result_int_t.append(x)
        elif isinstance(y, str):
            result_string_t.append(x)
        elif isinstance(y, float):
            result_float_t.append(x)
        elif isinstance(y, NoneType):
            result_none_t.append(x)
result_third = {"James Bond": {"int": result_int_t,
                               "string": result_string_t,
                               "float": result_float_t,
                               "none_type": result_none_t,
                               "bool": result_bool_t}}

final_result = {"first employee": result_first,
                "second employee": result_second,
                "third employee": result_third}
print(final_result)


def json_dump_method():
    json_data = json.dumps(final_result, indent=3)
    print('json_data: ', json_data)
    print('type(json_data): ', type(json_data))
    with open('/home/daniil/PycharmProjects/final_result.json', 'w') as file:
        file.write(json_data)
