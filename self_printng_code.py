
with open("self_printng_code.py", "r") as file:
    print(file.read())
    file.close()

with open("self_printng_code.py", "a") as file:
    code = '''print("this is generated") \n'''
    file.write(code)
    file.close()
print("this is generated") 
