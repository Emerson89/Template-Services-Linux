#!/bin/python3

import subprocess
import json

services = subprocess.check_output("systemctl list-units --all --state enabled,running --type service | sed -n '/^[[:lower:]]/p'", shell=True)
services_decoded = services.decode("utf-8")

list = []
list_of_services = services_decoded.split("\n")

for v in list_of_services:
      list.append({"{#SERVICENAME}": v})
raw = {"data": list}
print(json.dumps(raw))
