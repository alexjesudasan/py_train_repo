class dept:
    def __init__(self,dept_name,total_strength):
        self.dept_name = dept_name
        self.total_strength = total_strength
    def dept_info(self):
        print(self.dept_name)
        print(self.total_strength)


class head(dept):
    def __init__(self,manager_name,total_reporting,dept_name,total_strength):
        super().__init__(dept_name,total_strength)
        self.manager_name = manager_name
        self.total_reporting = total_reporting

class emp(head):
    def __init__(self,emp_name,salary,manager_name,total_reporting, dept_name, total_strength):
        super().__init__(manager_name,total_reporting,dept_name,total_strength)
        self.emp_name = emp_name
        self.salary = salary
    def emp_profile(self):
        return (f"Employee Name: {self.emp_name}, Salary: {self.salary}, "
                f"Dept Name: {self.dept_name}, Manager Name: {self.manager_name} ")


E1=emp("Priya",40000,"Ravi",5,"SW Engg",10)
E2=emp("Raghu",40000,"Sagar",5,"SW Release",15)
E3=emp("Benny",50000,"Ravi",5,"SW Engg",10)
employees = [E1, E2, E3]
dept_wise = {}

# Group employees department-wise
for e in employees:
    if e.dept_name not in dept_wise:
        dept_wise[e.dept_name] = []
    dept_wise[e.dept_name].append(e)

# Display details department-wise
for dept, emps in dept_wise.items():
    print(f"\nDepartment: {dept}")
    for e in emps:
        print(f"  {e.emp_profile()}")


# print(E1.emp_profile())
# print(E2.emp_profile())
# print(E3.emp_profile())