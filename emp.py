'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 01-08-24
    @Title: Employee wages per month


'''

import random
from abc import abstractmethod ,ABC
import json

class Employee_monthly_wage:

    def __init__(self, full_day_working_hrs=8, half_day_working_hrs=4, wage_per_hr=20, total_working_days=20, total_working_hrs=100):
        
        """
        
        Description:
            Initialize an Employee_monthly_wage object with given parameters.

        Parameters:
            full_day_working_hrs (int): Number of hours for a full working day.
            half_day_working_hrs (int): Number of hours for a half working day.
            wage_per_hr (int): Wage per hour.
            total_working_days (int): Total number of working days in a month.
            total_working_hrs (int): Total number of working hours in a month.
        
        
        """
        self.full_day_working_hrs = full_day_working_hrs
        self.half_day_working_hrs = half_day_working_hrs
        self.wage_per_hr = wage_per_hr
        self.total_working_days = total_working_days
        self.total_working_hrs = total_working_hrs

    def employee_attendance(self):
        
        """
        
        Description:
            Function to randomly determine an employee's attendance status.
            0: Absent
            1: Present
            2: Half-day

        Returns:
            int: A random choice representing attendance status (0, 1, or 2).
        
        
        """
        
        # Randomly choose an attendance status from [0, 1, 2]
        attendance = random.choice([0, 1, 2])
        return attendance

    def calculate_wage_of_employee(self, attendance):
        
        """
        
        Description:
            Function to calculate the wage of an employee based on their attendance.

        Parameters:
            attendance (int): Attendance status, where 0 represents absent and 1 represents present.

        Returns:
            int: The wage of the employee based on their attendance:
                - 0 for no attendance
                - Wage for full-day attendance if present
        
        """
        
        if attendance == 0:
            return 0  # No attendance, no wage
        if attendance == 1:
            return self.full_day_working_hrs * self.wage_per_hr  # Full-day attendance

    def calculate_part_time_wage_of_employee(self):
        
        """
        
        Description:
            Function to calculate the wage of an employee for part-time work.
            This assumes a fixed part-time wage for half-day work.

        Returns:
            int: The total wage for part-time work, calculated as half_day_working_hrs * wage_per_hr.
        
        
        """
        
        return self.half_day_working_hrs * self.wage_per_hr  # Wage for part-time work

    def each_day_wage(self):
        
        """
        
        Description:
            Function to calculate the daily wage based on attendance status.

        Returns:
            int: The wage for that particular day based on attendance.
        
        
        """
        
        # Get attendance status from employee_attendance function
        attendance = self.employee_attendance()
        
        # Calculate wage based on attendance status using pattern matching
        match attendance:
            case 0:
                wage = self.calculate_wage_of_employee(attendance)  # No attendance
            case 1:
                wage = self.calculate_wage_of_employee(attendance)  # Full-day attendance
            case 2:
                wage = self.calculate_part_time_wage_of_employee()  # Half-day attendance

        # Return the calculated wage
        return wage

    def montly_wage(self):
        
        """
        
        Description:
            Function to calculate the monthly wages by collecting daily wages for each day in the month.

        Returns:
            list: A list containing the wages for each day of the month.
        
        
        """
        
        # Initialize an empty list to store the wages for each day of the month
        month_wages = []
        day = hrs = 0     # Initialize counters for days and hours
        curr_day = 0      # Initialize index for the current day in the month_wages list
        
        # Iterate through each day of the month and calculate the wage for that day
        while (day < self.total_working_days) and (hrs < self.total_working_hrs):  # Continue until either the number of days reaches 'total_working_days' or total hours reach 'total_working_hrs'
            month_wages.append(self.each_day_wage())  # Append the wage of each day to the list
            
            if month_wages[curr_day] == 0:
                day += 1  # Increment day count if the wage is 0 (absent)
                hrs += 0  # No hours added for absent days
                curr_day += 1  # Move to the next day in the month_wages list
            elif month_wages[curr_day] == self.full_day_working_hrs * self.wage_per_hr:
                day += 1  # Increment day count for a full working day
                hrs += self.full_day_working_hrs  # Add full hours for a full working day
                curr_day += 1  # Move to the next day in the month_wages list
            else:
                day += 1  # Increment day count for a half-working day
                hrs += self.half_day_working_hrs  # Add hours for a half-working day
                curr_day += 1  # Move to the next day in the month_wages list

        # Return the list of monthly wages
        return month_wages
    
    @staticmethod
    def count_leave_half_full_days(month_wages):
        
        """
        
        Description:
            Function to count the number of leave days, full days, and half days based on monthly wage data.

        Parameters:
            month_wages (list): A list of daily wages for the month.

        Returns:
            list: A list containing three integers:
                - Number of leave days (absent days)
                - Number of full days
                - Number of half days
        
        """
        
        half_day = full_day = leaves = 0
        for day in month_wages:
            if day == 0:
                leaves += 1
            elif day == max(month_wages):
                full_day += 1
            else:
                half_day += 1
        return [leaves, full_day, half_day]
    
class EmpWageBuilder():
    def __init__(self, companies_details):
        
        """
        
        Description:
            Initialize an EmpWageBuilder object with details for multiple companies.

        Parameters:
            companies_details (list): A list of company details, where each detail is a list with parameters for CompanyEmpWages.
        
        """
        
        self.companies_details = companies_details
    
    def all_companies_wages(self):
        
        """
        
        Description:
            Function to calculate and return the monthly wages for all companies.

        Returns:
            list: A list of lists, where each sublist contains the monthly wages for one company.
        
        """

        multiple_companies_wages = {}
        for company in self.companies_details:
            # Calculate monthly wages for each company and append to the list
            company_wage = CompanyEmpWages(company[0], company[1], company[2], company[3], company[4],company[6]).company_monthly_wage()
            multiple_companies_wages[company[5]]=company_wage
        return multiple_companies_wages

    @staticmethod
    def print_wage_dict(multiple_companies_wages):
        keys = multiple_companies_wages.keys()
        for key in keys:

            total_sum =0
            print(f"{key}: ")
            emp_keys = multiple_companies_wages[key].keys()
            for emp_key in emp_keys:
                print(f"    {emp_key}: {multiple_companies_wages[key][emp_key]} ") 
                print(f"    Total Wage: {sum(multiple_companies_wages[key][emp_key])} ")
                work_details = Employee_monthly_wage.count_leave_half_full_days(multiple_companies_wages[key][emp_key])
                print(f"    Attendance:")
                print(f"        Leaves: {work_details[0]}")
                print(f"        Full Day: {work_details[1]}")
                print(f"        Half Day: {work_details[2]}")
                print(f"        Total worked hrs: {work_details[1]*8+work_details[2]*4}\n")
                
                total_sum += sum(multiple_companies_wages[key][emp_key])
            print(f"{key} total wage is {total_sum}\n\n")

class CompanyEmpWages():
    
    def __init__(self, full_day_working_hrs=8, half_day_working_hrs=4, wage_per_hr=20, total_working_days=20, total_working_hrs=100,number_of_employees =[]):
        
        """
        
        Description:
            Initialize a CompanyEmpWages object with the given parameters.

        Parameters:
            full_day_working_hrs (int): Number of hours for a full working day.
            half_day_working_hrs (int): Number of hours for a half working day.
            wage_per_hr (int): Wage per hour.
            total_working_days (int): Total number of working days in a month.
            total_working_hrs (int): Total number of working hours in a month.
            number_of_employees (int): Total number of employees.
        
        """
        self.full_day_working_hrs = full_day_working_hrs
        self.half_day_working_hrs = half_day_working_hrs
        self.wage_per_hr = wage_per_hr
        self.total_working_days = total_working_days
        self.total_working_hrs = total_working_hrs
        self.number_of_employees = number_of_employees

    def company_monthly_wage(self):
        
        """
        
        Description:
            Function to calculate the company's monthly wage by creating an Employee_monthly_wage object.

        Returns:
            list: A list containing the wages for each day of the month.
        
        """
        monthly_wage ={}
        keys = self.number_of_employees

        for key in keys:
            monthly_wage[key]=Employee_monthly_wage(self.full_day_working_hrs, self.half_day_working_hrs, self.wage_per_hr, self.total_working_days, self.total_working_hrs).montly_wage()
        return monthly_wage

def main():
    """
    Description:
        Main function to create instances of EmpWageBuilder and print monthly wages for different companies.

    """
    # Create an EmpWageBuilder object with details for three companies
        
    exit = True  # Flag to control the exit of the loop
    all_company_emp_details = {}  # Dictionary to store all company and employee details
    argument = []  # List to store company details for processing

    def unique(argument):
        """
        Function to remove duplicate company entries from the argument list.
        """
        new_argument = []  # List to store unique company entries
        for company in argument:
            if company not in new_argument:  # Check if the company is already in the new list
                new_argument.append(company)  # Add unique company entry to the new list
        return new_argument  # Return the list of unique companies

    while exit:
        try:
            # Prompt user to select an operation
            operation = int(input("\n\nEnter 1 to add Company and Employee \nEnter 2 to delete Employee or company \nEnter 3 to update Company or Employee Details \nEnter 4 to exit.\n:"))
            
            # Validate the operation input
            if operation < 1 or operation > 4:
                raise ValueError("Enter a valid number between 1 and 4.")
            
        except ValueError as ve:
            print(ve)  # Print error message if input is invalid
            continue  # Skip the rest of the loop and prompt for operation again

        if operation == 1:
            # Adding new company and employees
            company_name = input("Enter Company name: ")

            try:
                emp_per_hrs = int(input("Enter employee wages per hr: "))  # Input for employee wages per hour
            except ValueError:
                print("Enter a valid number.")  # Print error message if input is invalid
                continue  # Skip the rest of the loop and prompt for operation again

            try:
                number_of_employee = int(input("Enter number of employees: "))  # Input for number of employees
            except ValueError:
                print("Enter a valid number.")  # Print error message if input is invalid
                continue  # Skip the rest of the loop and prompt for operation again

            all_emp_details = []  # List to store employee details for the new company

            # Get existing employee names if the company already exists
            if company_name in all_company_emp_details:
                existing_employees = {emp["Name"].lower() for emp in all_company_emp_details[company_name]}
            else:
                existing_employees = set()  # Initialize as empty set if company does not exist

            for _ in range(number_of_employee):
                employee_name = input("\nEmployee Name: ").strip()

                if employee_name.lower() in existing_employees:
                    print(f"Employee name '{employee_name}' already exists in the company.")  # Print message if employee already exists
                    continue  # Skip to next iteration

                # Create a new dictionary for each employee
                emp_details = {
                    "Name": employee_name,
                    "wages_per_hrs": emp_per_hrs
                }
                all_emp_details.append(emp_details)  # Add employee details to the list
                existing_employees.add(employee_name.lower())  # Add employee name to the set (converted to lowercase for consistency)
                
                company_name_lower = company_name.lower()
                companies_name_lower = {key.lower(): key for key in all_company_emp_details.keys()}

            # Add the company's employee details to the main dictionary
            if company_name_lower in companies_name_lower:
                all_company_emp_details[company_name_lower].extend(all_emp_details)  # Extend existing list if company exists
            else:
                all_company_emp_details[company_name] = all_emp_details  # Add new entry for new company

            # Print all company and employee details
            print(json.dumps(all_company_emp_details, indent=4))

            # Update the argument list with new company data
            argument = []
            for company_name, company_employee in all_company_emp_details.items():
                each_company = [8, 4, 0, 20, 100, '', []]
                each_company[5] = company_name  # Set company name

                for employee in company_employee:
                    each_company[2] = employee["wages_per_hrs"]  # Set wages per hour
                    each_company[6].append(employee["Name"])  # Add employee name to the list
                argument.append(each_company)  # Add company details to the argument list

            argument = unique(argument)  # Remove duplicate entries from argument list
            employee_wages = EmpWageBuilder(argument).all_companies_wages()
            EmpWageBuilder.print_wage_dict(employee_wages)

        elif operation == 2:
            # Deleting company or employee
            if len(all_company_emp_details) == 0:
                print("Number of company is zero.First add new company.")
                continue
            try:
                delete = int(input("Enter 1 to delete company and 2 to delete employee: "))  # Input to choose deletion type
                company_name = input("Enter Company name to delete: ")  # Input for company name
                
                if delete == 1:
                    # Remove company and update argument
                    all_company_emp_details.pop(company_name, None)  # Remove company from dictionary
                    argument = [comp for comp in argument if comp[5] != company_name]  # Update argument list
                    print("Company removed.")  # Print confirmation message
                    
                elif delete == 2:
                    # Deleting specific employee
                    employee_name = input("Enter Employee name to delete: ")  # Input for employee name
                    
                    for company in argument:
                        if company[5] == company_name:
                            if employee_name in company[6]:
                                company[6].remove(employee_name)  # Remove employee from argument list
                                print("Employee removed.")  # Print confirmation message
                                
                                # Update the main dictionary
                                for emp in all_company_emp_details[company_name]:
                                    if emp["Name"] == employee_name:
                                        all_company_emp_details[company_name].remove(emp)  # Remove employee from company details
                                        print(json.dumps(all_company_emp_details, indent=4))
                                        employee_wages = EmpWageBuilder(argument).all_companies_wages()
                                        EmpWageBuilder.print_wage_dict(employee_wages)
                                        break
                            else:
                                print("Employee not found.")
                                continue
                        else:
                            print("Company not found")
                            continue
                else:
                    print("Enter a valid number.")  # Print message for invalid deletion type
                
                # Print updated details

            
            except Exception as e:
                print(f"Error: {e}")  # Print error message if any exception occurs

        elif operation == 3:
            # Updating company or employee details
            if len(all_company_emp_details) == 0:
                print("Number of company is zero.First add new company.")
                continue
            update = input("Enter 1 to update Company and 2 to update Employee name: ")  # Input to choose update type
            
            if update == "1":
                # Update company details
                company_name = input("Enter Company name to update: ")  # Input for company name
                
                if company_name in all_company_emp_details:
                    try:
                        emp_per_hrs = int(input("Enter new employee wages per hr: "))  # Input for new wages per hour
                        
                        # Update the wages for all employees in this company
                        for employee in all_company_emp_details[company_name]:
                            employee["wages_per_hrs"] = emp_per_hrs
                        print("Company wages updated.")  # Print confirmation message
                        
                        # Update argument list
                        for company in argument:
                            if company[5] == company_name:
                                company[2] = emp_per_hrs  # Update wages in argument list
                        argument = unique(argument)  # Remove duplicate entries
                        employee_wages = EmpWageBuilder(argument).all_companies_wages()
                        EmpWageBuilder.print_wage_dict(employee_wages)
                    except ValueError:
                        print("Enter a valid number.")  # Print message for invalid number
                else:
                    print("Company not found.")  # Print message if company is not found
            
            elif update == "2":
                # Update employee name
                company_name = input("Enter Company name to update employee: ")  # Input for company name
                
                if company_name in all_company_emp_details:
                    old_name = input("Enter current employee name: ")  # Input for current employee name
                    new_name = input("Enter new employee name: ")  # Input for new employee name
                    
                    found = False
                    for employee in all_company_emp_details[company_name]:
                        if employee["Name"] == old_name:
                            employee["Name"] = new_name  # Update employee name in the dictionary
                            found = True
                            break
                    
                    if found:
                        print("Employee name updated.")  # Print confirmation message
                        # Update argument list
                        for company in argument:
                            if company[5] == company_name:
                                try:
                                    index = company[6].index(old_name)  # Find index of old name
                                    company[6][index] = new_name  # Update name in argument list
                                except ValueError:
                                    pass
                        argument = unique(argument)  # Remove duplicate entries
                        employee_wages = EmpWageBuilder(argument).all_companies_wages()
                        EmpWageBuilder.print_wage_dict(employee_wages)
                    else:
                        print("Employee not found.")  # Print message if employee is not found
                else:
                    print("Company not found.")  # Print message if company is not found

        elif operation == 4:
            exit = False  # Set exit flag to False to terminate the loop
    
# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()