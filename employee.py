class Employee:
    """A sample Employee class"""

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        if not all(isinstance(param, str) for param in [first, last]):
            raise ValueError("First and last names must be strings.")
        if not isinstance(pay, (int, float)) or pay < 0:
            raise ValueError("Pay must be a positive number.")

        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def evaluate_performance(self, rating):
        if rating < 3:
            feedback = "Needs Improvement"
            potential_raise = 1.00  # No raise
        elif 3 <= rating < 4:
            feedback = "Meets Expectations"
            potential_raise = 1.03  # 3% raise
        else:
            feedback = "Exceeds Expectations"
            potential_raise = 1.06  # 6% raise

        return {"feedback": feedback, "potential_raise": potential_raise}

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

class Manager(Employee):
    """A sample Manager class"""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees else []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def __repr__(self):
        return "Manager('{}', '{}', {}, {})".format(self.first, self.last, self.pay, self.employees)

    