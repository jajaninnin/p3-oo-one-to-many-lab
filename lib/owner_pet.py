class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not valid. choose from {Pet.PET_TYPES}")
        self.pet_type = pet_type
        self.owner = owner       
        Pet.all.append(self)
    
    def __repr__(self):
        return f"name={self.name}, pet_type={self.pet_type}, owner={self.owner}"
    
    def __lt__(self, other):
        if isinstance(other, Pet):
            return self.name < other.name
        return NotImplemented

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return Pet.all

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all)