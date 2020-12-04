import design
import jsonschema
import json
import os
from pathlib import Path

event_files = os.listdir(Path.cwd() / 'task_folder' / 'event_files')
schema_files = os.listdir(Path.cwd() / 'task_folder' / 'schema_files')

event_list = list()
schema_list = list()

for i in range(len(event_files)):
    s = Path.cwd() / 'task_folder' / 'event_files' / event_files[i]
    with open(s, 'r', encoding='utf-8') as f:
        message = json.load(f)
    event_list.append(message)
    f.close()

for i in range(len(schema_files)):
    s = Path.cwd() / 'task_folder' / 'schema_files' / schema_files[i]
    with open(s, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    schema_list.append(schema)
    f.close()

with open(Path.cwd() / 'task_folder' / 'meta.schema', 'r', encoding='utf-8') as f:
    meta = json.load(f)
    f.close()

with open(Path.cwd() / 'README.txt', 'a', encoding='utf-8') as f:
    f.write(design.main_header())
    f.write(design.big_line())
    f.close()
for i in range(len(schema_list)):
    validator = jsonschema.Draft7Validator(meta)
    errors = validator.iter_errors(schema_list[i])
    count = 1
    for error in errors:
        s1 = "Meta schema error № %(a)s %(b)s, json schema file - %(c)s" \
             % {"a": i + 1, "b": count, "c": schema_files[i]}
        s2 = "%(d)s" % {"d": error}
        with open(Path.cwd() / 'README.txt', 'a', encoding='utf-8') as f:
            f.write(s1 + '\n')
            f.write(s2 + '\n')
            f.write(design.big_line())
            f.close()
        print('Meta schema error №', i + 1, count, 'json schema file - ', schema_files[i])
        print(error)
        print(design.big_line())
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
            with open(Path.cwd() / 'README.txt', 'a', encoding='utf-8') as f:
                f.write(s1 + '\n')
                f.write(s2 + '\n')
                f.write(design.small_line())
                f.write(s3 + '\n')
                f.write(design.big_line())
                f.close()
            print("Error №", i, j, count, ", json file - ", event_files[j], ", schema file - ", schema_files[i])
            print(count, "th error in ", event_files[j])
            print(error)
            count += 1
            print(design.big_line())
