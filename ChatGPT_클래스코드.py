# Define the parent class Person
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.person_id}, Name: {self.name}")


# Define the Manager class inheriting from Person
class Manager(Person):
    def __init__(self, person_id, name, skill):
        super().__init__(person_id, name)
        self.skill = skill


# Define the Employee class inheriting from Person
class Employee(Person):
    def __init__(self, person_id, name, itSkill):
        super().__init__(person_id, name)
        self.itSkill = itSkill


# Define the Alba class inheriting from Person
class Alba(Person):
    pass


# Test the classes
if __name__ == "__main__":
    # Test Manager class
    managers = []
    for i in range(1, 6):
        manager = Manager(i, f"Manager-{i}", f"Skill-{i}")
        managers.append(manager)

    print("Managers:")
    for manager in managers:
        manager.printInfo()
        print("Skill:", manager.skill)
        print()

    # Test Employee class
    employees = []
    for i in range(1, 6):
        employee = Employee(i, f"Employee-{i}", f"IT Skill-{i}")
        employees.append(employee)

    print("Employees:")
    for employee in employees:
        employee.printInfo()
        print("IT Skill:", employee.itSkill)
        print()

    # Test Alba class
    albas = []
    for i in range(1, 6):
        alba = Alba(i, f"Alba-{i}")
        albas.append(alba)

    print("Albas:")
    for alba in albas:
        alba.printInfo()
        print()
