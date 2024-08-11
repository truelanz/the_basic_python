class Funcionario:
    def  __init__(self, name, admissionDate, salary):
        self.name = name
        self.admissionDate = admissionDate
        self.salary = salary
        
    def setEmployee(self, name, admissionDate, salary):
        self.name = name
        self.admissionDate = admissionDate
        self.salary = salary
    
    def setSalary(self, changeSalary):
        self.salary = changeSalary
        
    def getEmployee(self):
        print('(nome: ' + (self.name) + ', Data de admissão: ', (self.admissionDate), ', salario: ', (self.salary), ')')
        
    def __repr__(self):
        return '(nome: ' + (self.name), ', Data de admissão: ', (self.admissionDate), ', salario: ', (self.salary), ')'
    
class Manager(Funcionario):
    def managerEmployee(self, bonus):
        self.bonus = bonus
        self.salary += bonus
        
employee1 = Funcionario('Alan', '15/03/18', 2222)
employee1.getEmployee()

employee2 = Funcionario('Cleber', '11/01/19', 2000)
employee2.getEmployee()
employee2.setEmployee('Cleber', '11/01/19', 2222)
employee2.getEmployee()

employee1.setEmployee('Ovo', 'ovo', 1111)
employee1.getEmployee()

employee1.setSalary(555)
employee1.getEmployee()

employee2.setSalary(2500)
employee2.getEmployee()

manager1 = Manager('Ricado', '02/02/15', 5000)
manager1.managerEmployee(500)
manager1.getEmployee()