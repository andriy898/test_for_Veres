class Benzopyla:
    def __init__(self, nazva, potuzhnist_vat, kilkist_obertiv, work_hours=0, public_numeric=0, public_string=" "):
        self.nazva = nazva
        self.__potuzhnist_vat = potuzhnist_vat
        self.__kilkist_obertiv = kilkist_obertiv
        self.work_hours = work_hours  
        self.public_numeric = public_numeric
        self.public_string = public_string

    def nazva(self):
        return self.__nazva

    @nazva.setter
    def nazva(self, value):
        self.__nazva = value

    @property
    def potuzhnist_vat(self):
        return self.__potuzhnist_vat

    @potuzhnist_vat.setter
    def potuzhnist_vat(self, value):
        self.__potuzhnist_vat = value

    @property
    def kilkist_obertiv(self):
        return self.__kilkist_obertiv

    @kilkist_obertiv.setter
    def kilkist_obertiv(self, value):
        self.__kilkist_obertiv = value

    @property
    def work_hours(self):
        return self.__work_hours

    @work_hours.setter
    def work_hours(self, value):
        self.__work_hours = value
        
    def add_work_hours(self, hours):
        self.work_hours += hours

    def __str__(self):
        return f"Benzopyla(nazva={self.nazva}, potuzhnist={self.__potuzhnist_vat} W, kilkist_obertiv={self.__kilkist_obertiv} RPM, " \
               f"work_hours={self.work_hours} hours, public_numeric={self.public_numeric}, public_string='{self.public_string}')"

    def __repr__(self):
        return f"Benzopyla('{self.nazva}', {self.__potuzhnist_vat}, {self.__kilkist_obertiv}, {self.work_hours}, {self.public_numeric}, '{self.public_string}')"

    def __del__(self):
        print(f"Benzopyla '{self.nazva}' is being deleted.")

def main():
    
    benzopyla1 = Benzopyla("Stihl MS 271", 2500, 2800, 20, 123, "Professional")  
    benzopyla2 = Benzopyla("Husqvarna 450", 2200, 2700, 15, 456, "Home Use")      
    benzopyla3 = Benzopyla("Makita UC4041A", 1800, 2600, 5, 789, "Light Duty")    

    benzopyla1.public_numeric = " hello  world "

    print(repr(benzopyla1))
    print(benzopyla2)
    print(benzopyla3)

    
    max_power = benzopyla1.get_potuzhnist_vat()
    max_rpm = benzopyla1.get_kilkist_obertiv()
    max_benzopyla = benzopyla1

    benzopyly = [benzopyla1, benzopyla2, benzopyla3]

    max_work_hours_benzopyla = benzopyly[0]
    for benzopyla in benzopyly:
        if benzopyla.get_work_hours() > max_work_hours_benzopyla.get_work_hours():
            max_work_hours_benzopyla = benzopyla
        print(f"Бензопила з найбільшою кількістю робочих годин: {max_work_hours_benzopyla.get_nazva()} з {max_work_hours_benzopyla.get_work_hours()} годинами.")


if __name__ == "__main__":
    main()