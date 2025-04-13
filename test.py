
# Person class mit setter und getter mit toJson() und fromJson() Methoden
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def to_json(self):
        return {"name": self._name, "age": self._age}

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["name"], json_data["age"])



max = Person("Max", 25)

print(max.to_json())

test = {'name': 'Marc', 'age': 23}






marc = Person.from_json(test)

marc.age = max.age+2






print(marc.to_json())

# erkläre serialization und deserialization
# Serialization ist der Prozess, bei dem ein Objekt in ein Format umgewandelt wird, das gespeichert oder übertragen werden kann.
# Deserialization ist der Prozess, bei dem die gespeicherten oder übertragenen Daten zurück in ein Objekt umgewandelt werden.