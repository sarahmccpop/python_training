class HeadsOfDepartment:
    # class variables

    company_name = "McConvilles Coffee"

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def show(self):
        print(
            "Head of Department:",
            self.name,
            self.salary,
            self.department,
            self.company_name,
        )
