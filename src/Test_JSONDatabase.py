from JSONDatabase import Database
from faker import Faker

fake = Faker(["en_US", "zh_CN", "zh_CN", "zh_TW", "fr_FR"])
db = Database("test")
for i in range(100):
    db.add(fake.uuid4(), {
        'name': fake.name(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'email': fake.email()
    })
db.save()
db2 = Database.load_database("test")
print(db2.get_meta())
