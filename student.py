from person import Person

class Student(Person):
    def __init__(self,matr,semester,name,geburstag,wohnort):
        super().__init__(name,geburstag,wohnort)
        self.matr = matr
        self.semester = semester

    def to_json(filename):
        # speichere alle infos in json-datei
        ...

    def __str__(self):
        return f"{self.matr} - {self.name}"

    def __eq__(self,other):
        if self.matr == other.matr:
            return True
        return False
    
    def __gt__(self,other):
        pass

if __name__ == "__main__":
    student1 = Student("6047157",5,"Moritz","27.10","Hückelhoven")
    student2 = Student("6047157",5,"Moritz","27.10","Hückelhoven")

    if student1 == student2:
        print("gleich")

