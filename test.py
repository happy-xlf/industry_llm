

message = [{'role': 'system', 'content': 'The user provides a question and you provide SQL. You will only respond with SQL code...每月生产信息;\n\n\n'}, {'role': 'user', 'content': '2023年8月7日生产信息情况'}, {'role': 'assistant', 'content': "SELECT *\nFROM day_message\nWHERE `date` = '2023-08-07';"}, {'role': 'user', 'content': '2023年9月生产信息状况'}]


query = message[-1]['content']
message.pop(-1)


print(query)
print(message)
