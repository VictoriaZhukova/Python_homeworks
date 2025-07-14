from address import Address
from mailing import Mailing

m = Mailing(to_address=Address(111234, "Krasnoyarsk", "Lenina",3, 4),
            from_address=Address(432654, "Omsk", "Kruglaya", 6, 45),
            cost=500,
            track="N65")


print(f'Отправление {m.track} из {m.from_address.index}, {m.from_address.city}, {m.from_address.street}, {m.from_address.house}-{m.from_address.apartment} в {m.to_address.index}, {m.to_address.city}, {m.to_address.street}, {m.to_address.house}-{m.to_address.apartment}. Стоимость {m.cost} рублей.')


