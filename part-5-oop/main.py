from enum import Enum

class EntityType(Enum):
    PHYSICAL = 1
    NON_PHYSICAL = 2

    def __str__(self) -> str:
        if self.value == EntityType.PHYSICAL.value:
            return "Physical"
        elif self.value == EntityType.NON_PHYSICAL.value:
            return "Non Physical"
        else:
            return "Unknown"

class Entity():
    def __init__(self, type: EntityType) -> None:
        self.type = type
    
    def __str__(self) -> str:
        return f"I am an entity of the following type: [{self.type}]"
    
    @classmethod
    def defaultMsg(cls) -> str:
        return "[Entity]"

class Person(Entity):
    def __init__(self, name: str, email: str) -> None:
        super().__init__(EntityType.PHYSICAL)
        self.name = name
        self.email = email
    
    def __str__(self) -> str:
        return f"{super().__str__()}, my name is [{self.name}], this is my email [{self.email}]"

class Employee(Person):
    def __init__(self, name: str, email: str, company_id: int) -> None:
        super().__init__(name, email)
        self.company_id = company_id

    def __str__(self) -> str:
        return f"{super().__str__()} and I have the following company id [{self.company_id}]"

class Company(Entity):
    def __init__(self, name: str) -> None:
        super().__init__(EntityType.NON_PHYSICAL)
        self.name = name
    
    def __str__(self) -> str:
        return f"{super().__str__()} and my name is: [{self.name}]"

class Object(Entity):
    def __init__(self) -> None:
        super().__init__(EntityType.PHYSICAL)
    
    def __str__(self) -> str:
        return super().__str__()

def printHierarchy(e: Entity):
    print(f"is Entity? {isinstance(e, Entity)}")
    print(f"is Company? {isinstance(e, Company)}")
    print(f"is Person? {isinstance(e, Person)}")
    print(f"is Employee? {isinstance(e, Employee)}")


if __name__ == "__main__":

    print("== Basic inheritance calling a supper method")
    # A person
    p = Person("John", "john@gmail.com")
    print("Person to str: ", p)
    printHierarchy(p)

    print("\n== Basic inheritance calling a chainned supper method")
    # An employee
    e = Employee("Mark", "mark@gmail.com", 123)
    print("Employee to str: ", e)
    printHierarchy(e)

    print("\n== Basic inheritance from the same abstract Entity class")
    # A company
    c = Company("Google")
    print("Company to str: ", c)
    printHierarchy(c)

    print("\n== Comparing the type using a dictionary")
    # None
    t = {
        "name": "Mark",
        "email": "mark@gmail.com"
    }
    print("Dict to str: ",t)
    printHierarchy(t)

    print("\n== Converting a dictionary to a real object")
    # Converting to a Person
    tp = Person(**t)
    print("Converted Person to str: ", tp)
    printHierarchy(tp)

    print("\n== Using static methods")
    # Class methods
    print("Static method output: ", Entity.defaultMsg())

    print("\n== Inheriting static methods")
    # Class methods
    print("Static method output: ", Person.defaultMsg())

    # Overhide the default __str__
    print("Overhide the default str: ", Object())

    print(repr(p))