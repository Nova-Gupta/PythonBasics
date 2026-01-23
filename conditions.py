#switch-case
status = 200
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

# if else case
if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Server Error")
else:
    print("Unknown Status")