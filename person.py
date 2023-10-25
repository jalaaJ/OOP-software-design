from address import Address

class Person():
    def __init__(self, first, last, dob, phone, address: Address):
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone_number = phone

        # since we have an associatio between a person and an address,
        # we need to add the address in the constructor
        self.addresses = []
        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Exception("Invalid address...")
            self.addresses = address
        else:
            raise Exception("Invalid address...")
        
    def add_address(self, address):
        if not isinstance(address, Address):
            raise Exception("Invalid address...")
        
        self.addresses.append(address)
    
    

