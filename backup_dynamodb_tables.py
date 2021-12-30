import boto3
import json
import os
from decimal import Decimal

REGION = os.getenv("REGION")
dynamodb = boto3.resource("dynamodb", region_name=REGION)
tables = []


for i in range(4):  # BACKUP_TABLE_NAME_1
    TABLE_NAME = "BACKUP_TABLE_NAME_" + str(i)
    if os.environ[TABLE_NAME] != "NULL":
        print("Backing up TABLE_NAME=", os.environ[TABLE_NAME])
        tables.append(os.environ[TABLE_NAME])

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

for table in tables:
    full_path = './BackupFolder/dynamodb_backup/'
    file_name = table + ".json"
    completePath = os. path. join(full_path, file_name)
    print(completePath)
    file = open(completePath, "w+")
    table = dynamodb.Table(table)
    response = table.scan()  # Backup Dynamodb Table Contents
    json_object = json.dumps(response["Items"], indent=4, default=default)
    file.write(json_object)
    file.close()