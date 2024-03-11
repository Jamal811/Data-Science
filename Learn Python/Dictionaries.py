# key value pair
monthConversions = {
    "Jan": "January",
    "Feb": "Februry",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
monthConversions2 = {
    0: "January",
    1: "Februry",
    2: "April",
    3: "March",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December",
}

# print(monthConversions["Dec"])
# print(monthConversions.get("Sep"))
# print(monthConversions.get("Chao", "Not a Valid Key"))

print(monthConversions2[10])
print(monthConversions2.get(11))

