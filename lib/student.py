class Student:
    def hello(self):
        return "Hey there!"
    
    def raise_hand(self):
        return "Teacher, I have a question."

class ChattyStudent(Student):
    def hello(self):
        return "Hey there! I'm a chatty student."
    
    def raise_hand(self):
        return "Teacher, I have something to say!"
