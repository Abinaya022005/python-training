from abc import ABC, abstractmethod
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def login(self):
        print(f"{self.name} logged in successfully")

class Patient(User):
    def __init__(self, name, email, health_id):
        super().__init__(name, email)
        self.__health_id = health_id
    def get_health_id(self):
        return self.__health_id
    def set_health_id(self, new_id):
        if new_id.startswith("VIMS"):
            self.__health_id = new_id
            print("Health ID updated")
        else:
            print("Invalid Health ID format")

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.specialization = specialization
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    
class Consultation(ABC):
    @abstractmethod
    def prescribe(self):
        pass

class GeneralCheckUp(Consultation):
    def prescribe(self):
        print("Prescription: Take given tablets and rest")

class Surgery(Consultation):
    def prescribe(self):
        print("Prescription: Surgery required")

print("MediFlow HEALTHCARE SYSTEM")
print("patient details")
patient = Patient("Abi", "abi@123", "VIMS1234")
patient.login()
print("Health ID:", patient.get_health_id())
print("\nUPDATE HEALTH ID:")
choice = input("Type YES or NO: ").upper()

if choice == "YES":
    new_id = input("Enter New Health ID: ")
    patient.set_health_id(new_id)
    print("Updated Health ID:", patient.get_health_id())
else:
    print("Health ID not updated")

print("\nEnter Doctor Details")
d_name = input("Name: ")
d_email = input("Email: ")
d_specialization = input("Specialization: ")

doctor = Doctor(d_name, d_email, d_specialization)
doctor.login()
print(doctor)

print("\nConsultation Process")
consultations = [GeneralCheckUp(), Surgery()]

for c in consultations:
    c.prescribe()
 
