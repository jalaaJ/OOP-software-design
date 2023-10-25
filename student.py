from address import Address
from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, first, last, dob, phone, address: Address, international=False):
        super().__init__(first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enroll: Enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid enroll...")
        
        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False
    
    def is_part_time(self):
        return len(self.enrolled) <= 3
    
    
    

        