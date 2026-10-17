address = "1.1.1.1"

ipAddress = ""
for i in address:
    if "." in i:
        ipAddress = address.replace(".","[.]")

print(ipAddress)