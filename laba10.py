class Humanity:
    def __init__(self, name, age):
        self.name = name          # Публічний атрибут
        self.__age = age          # Інкапсуляція: приватний атрибут (починається з __)

    # Метод для отримання доступу до приватного атрибуту (Getter)
    def get_age(self):
        return self.__age

    # Метод, який буде перевизначено (Поліморфізм)
    def introduce(self):
        return f"Я представник людства. Мене звати {self.name}."

    def breathe(self):
        return f"{self.name} дихає повітрям."

# Наслідування: Клас Student наслідує Humanity
class Student(Humanity):
    def __init__(self, name, age, course, college_name):
        # Виклик конструктора батьківського класу
        super().__init__(name, age)
        self.course = course
        self.college_name = college_name

    # Поліморфізм: Перевизначення методу батьківського класу
    def introduce(self):
        return (f"Я студент {self.course}-го курсу коледжу {self.college_name}. "
                f"Мене звати {self.name}, мені {self.get_age()} років.")

    def study(self):
        return f"{self.name} пише лабораторну роботу з програмування."

# --- Перевірка роботи ---

# Створюємо об'єкти
person = Humanity("Олександр", 45)
student = Student("Тарас", 18, 2, "ТФК Луцьк")

print(person.introduce())
print(student.introduce())  # Виклик перевизначеного методу (Поліморфізм)
print(student.study())
