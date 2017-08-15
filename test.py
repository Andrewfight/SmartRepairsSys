# coding: utf-8
from hfut import Student
import json

stu = Student('2016212039', 'ssh19970912', 'hf')
info = stu.get_my_info()
info_json = json.dumps(info)
print info_json.decode("unicode-escape")
