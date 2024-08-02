'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 01-08-24
    @Title: Employee wages per month


'''

import random
from abc import abstractmethod ,ABC

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
        while day < self.total_working_days and hrs < self.total_working_hrs:  # Continue until either the number of days reaches 'total_working_days' or total hours reach 'total_working_hrs'
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
            print(f"{key}: ")
            emp_keys = multiple_companies_wages[key].keys()
            for emp_key in emp_keys:
                print(f"    {emp_key}: {multiple_companies_wages[key][emp_key]} ")              

class CompanyEmpWages():
    
    def __init__(self, full_day_working_hrs=8, half_day_working_hrs=4, wage_per_hr=20, total_working_days=20, total_working_hrs=100,number_of_employees =1):
        
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
        keys = []
        # Calculate the monthly wages by using Employee_monthly_wage
        for i in range(self.number_of_employees):
            i = str(i+1)
            keys.append("Employee "+i)
        for key in keys:
            monthly_wage[key]=Employee_monthly_wage(self.full_day_working_hrs, self.half_day_working_hrs, self.wage_per_hr, self.total_working_days, self.total_working_hrs).montly_wage()
        return monthly_wage

def main():
    """
    Description:
        Main function to create instances of EmpWageBuilder and print monthly wages for different companies.

    """
    # Create an EmpWageBuilder object with details for three companies
    emplpoyee_wages = EmpWageBuilder([[8, 4, 20, 10, 50,"Apple",4], [8, 4, 20, 20, 100,"Amazon",5], [8, 4, 20, 15, 75,"Google",4]]).all_companies_wages()

    EmpWageBuilder.print_wage_dict(emplpoyee_wages)

    
# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
