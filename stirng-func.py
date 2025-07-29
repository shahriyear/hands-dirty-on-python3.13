name = "fahim shahriyear"


print("lower case: ", name.lower())
print("upper case: ", name.upper())
print("strip: ", name.strip())
print("find: ", name.find("F"))
print("find: ", name.find("f"))
print("rfind: ", name.rfind("f"))
print("replace: ", name.replace("shahriyear", "hossain"))
print("split: ", name.split("a"))
capitalize = name.capitalize()
print("capitalize: ", capitalize)

print("isnumeric: ", name.isnumeric())
print("isalpha: ", name.isalpha())
print("isdigit: ", name.isdigit())
print("islower: ", name.islower())
print("isupper: ", name.isupper())
print("isspace: ", name.isspace())


print("center: ", name.center(20, "*"))
print("ljust: ", name.ljust(20, "*"))
print("rjust: ", name.rjust(20, "*"))

print("zfill: ", name.zfill(20))

print("startswith: ", name.startswith("f"))
print("endswith: ", name.endswith("year"))

count = name.count("a")
print("count: ", count)

print("index: ", name.index("a"))

print("rindex: ", name.rindex("a"))

print(help(str))
