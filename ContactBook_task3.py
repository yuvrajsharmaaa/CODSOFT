import face_recognition
import cv2
import numpy as np

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.known_face_encodings = []
        self.known_face_names = []

    def add_contact(self, name, phone, email, image_path):
        if name in self.contacts:
            print(f"Contact {name} already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'image_path': image_path}

            # Load the contact's image and encode the face
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(name)

            print(f"Contact {name} added.")

    def view_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

            # Also remove the face encoding and name
            index = self.known_face_names.index(name)
            del self.known_face_encodings[index]
            del self.known_face_names[index]

            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def view_all_contacts(self):
        if self.contacts:
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Image Path: {info['image_path']}")
        else:
            print("No contacts found.")

    def recognize_face(self, image_path):
        # Load the image and find face encodings
        unknown_image = face_recognition.load_image_file(image_path)
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)

        if unknown_face_encodings:
            unknown_face_encoding = unknown_face_encodings[0]
            
            # Compare the face with known faces
            results = face_recognition.compare_faces(self.known_face_encodings, unknown_face_encoding)
            if True in results:
                match_index = results.index(True)
                name = self.known_face_names[match_index]
                self.view_contact(name)
            else:
                print("No matching contact found.")
        else:
            print("No face found in the image.")

def menu():
    book = ContactBook()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Recognize Face")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            image_path = input("Enter image path: ")
            book.add_contact(name, phone, email, image_path)
        elif choice == '2':
            name = input("Enter name: ")
            book.view_contact(name)
        elif choice == '3':
            name = input("Enter name: ")
            book.delete_contact(name)
        elif choice == '4':
            book.view_all_contacts()
        elif choice == '5':
            image_path = input("Enter the path to the image to recognize: ")
            book.recognize_face(image_path)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
