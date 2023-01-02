# todo:dictionaries

customer = {
    "name": "trần anh tuấn",
    "age": 21,
    "is_verified": True
}

print(customer)

# lấy thông tin trong dict => key
print(f"Tên bạn là : {customer['name']}")
print(f"Tuổi bạn là : {customer['age']}")

print(f"Tên bạn là : {customer.get('name')}")
print(f"Tên bạn là : {customer.get('Name')}")

print(customer.get("birth_date", "2002-12-03"))
print(customer)

# tạo key và gắn giá trị cho key
customer["age"] = 20
print(customer)

# dùng trong th ko có key thì sẽ tạo value cho key này nhưng key ko đc đưa vào dict
customer["birth_date"] = "2002-12-03"
print(customer)

# example
phone = input("phone : ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

out = ""
for item in phone:
    out += digits_mapping[item]

print(out)
