import jsonschema
import json
import os

event_files = os.listdir(r"D:\PycharmProjects\JSON_validator\task_folder\event")
schema_files = os.listdir(r"D:\PycharmProjects\JSON_validator\task_folder\schema")

event_list = list()
schema_list = list()

for i in range(len(event_files)):
    s = "D:\\PycharmProjects\\JSON_validator\\task_folder\\event\\" + event_files[i]
    with open(s, 'r', encoding='utf-8') as f:
        message = json.load(f)
    event_list.append(message)
    f.close()

for i in range(len(schema_files)):
    s = "D:\\PycharmProjects\\JSON_validator\\task_folder\\schema\\" + schema_files[i]
    with open(s, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    schema_list.append(schema)
    f.close()

with open("D:\\PycharmProjects\\JSON_validator\\task_folder\\meta.schema", 'r', encoding='utf-8') as f:
    meta = json.load(f)
    f.close()

with open("D:\\PycharmProjects\\JSON_validator\\README.txt", 'a', encoding='utf-8') as f:
    f.write("====================JSON-JSONSCHEMA-METASCHEMA VALIDATION ERRORS=================================" + '\n')
    f.write("-------------------------------------------------------------------------------------------------" + '\n')
    f.close()
for i in range(len(schema_list)):
    validator = jsonschema.Draft7Validator(meta)
    errors = validator.iter_errors(schema_list[i])
    count = 1
    for error in errors:
        s1 = "Meta schema error № %(a)s %(b)s, json schema file - %(c)s" \
             % {"a": i + 1, "b": count, "c": schema_files[i]}
        s2 = "%(d)s" % {"d": error}
        with open("D:\\PycharmProjects\\JSON_validator\\README.txt", 'a', encoding='utf-8') as f:
            f.write(s1 + '\n')
            f.write(s2 + '\n')
            f.write(
                "-------------------------------------------------------------------------------------------------" + '\n')
            f.close()
        print('Meta schema error №', i + 1, count, 'json schema file - ', schema_files[i])
        print(error)
        print('-----------------------------------------------------------------------------------------------------')
for i in range(len(schema_list)):
    for j in range(len(event_list)):
        validator = jsonschema.Draft7Validator(schema_list[i])
        errors = validator.iter_errors(event_list[j])
        count = 1
        for error in errors:
            s1 = "Error № %(a)s %(b)s %(c)s, json file - %(d)s, schema file - %(e)s" \
                % {"a": i + 1, "b": j + 1, "c": count, "d": event_files[j], "e": schema_files[i]}
            s2 = "%(f)s th error in %(g)s" % {"f": count, "g": event_files[j]}
            s3 = "%(h)s" % {"h": error}
            with open("D:\\PycharmProjects\\JSON_validator\\README.txt", 'a', encoding='utf-8') as f:
                f.write(s1 + '\n')
                f.write(s2 + '\n')
                f.write("______________________" + '\n')
                f.write(s3 + '\n')
                f.write("-------------------------------------------------------------------------------------------------" + '\n')
                f.close()
            print("Error №", i, j, count, ", json file - ", event_files[j], ", schema file - ", schema_files[i])
            print(count, "th error in ", event_files[j])
            print(error)
            count += 1
            print('---------------------------------------------------------------------------------------------------')
