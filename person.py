class Person:
    def __init__(self,name,geburstag,wohnort):
        self.name = name
        self.geburtstag = geburstag
        self.wohnort = wohnort

    def __str__(self):
        return f"{self.name}"

    def count(self,x):
        for i in range(x):
            print(i)

if __name__ == "__main__":
    ich = Person("Moritz","27.10","Hückelhoven")
    print(ich.geburtstag)