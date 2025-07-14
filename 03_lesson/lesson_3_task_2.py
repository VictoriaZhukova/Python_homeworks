from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "A32", "+7987665334"),
    Smartphone("Samsung", "A24", "+79876675437"),
    Smartphone("Huawei", "p30", "+79097786553"),
    Smartphone("iPhone", "13", "+7876654438"),
    Smartphone("Xiaomi", "14T", "+79087768909")
           ]


for phone in catalog:
    print(f"{phone.phoneBrand} - {phone.phoneModel}. {phone.number}")
