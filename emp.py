'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Employee wages per month


'''

import random


class Employee_monthly_wage:
    def __init__(self,wage_per_hr = 20,full_day_working_hrs = 8,half_day_working_hrs=4,month =20):
        self.wage_per_hr = wage_per_hr  # Wage per hour
        self.full_day_working_hrs = full_day_working_hrs  # Working hours for a full day
        self.half_day_working_hrs = half_day_working_hrs  # Working hours for a half day
        self.month =month # Working days in month

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

    def calculate_wage_of_employee(self,attendance):

        """
        
        Description:
            Function to calculate the wage of an employee based on their attendance.
        
        Parameter:
            attendance: 0 or 1, i.e., employee present or not

        Returns:
            int: The wage of the employee based on their attendance:
                - 0 for no attendance
                - 20*8 for full-day attendance
        
        """
        
        if attendance == 0:
            return 0  # No attendance, no wage

        if attendance == 1:
            return self.full_day_working_hrs * self.wage_per_hr  # Full-day attendance, wage for 8 hours at $20/hour

    def calculate_part_time_wage_of_employee(self):
        
        """
        
        Description:
            Function to calculate the wage of an employee for part-time work.
            This assumes a fixed part-time wage for 4 hours of work.

        Returns:
            int: The total wage for part-time work, calculated as 4 hours * $20/hour.
        
        """
        
        return self.half_day_working_hrs * self.wage_per_hr  # Wage for 4 hours of work at $20 per hour

    def each_day_wage(self):
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

        # Print the calculated wage
        return wage

    def montly_wage(self):
        """
        Description:
            Function to calculate the monthly wages by collecting daily wages for each day in the month.

        Returns:
            list: A list containing the wages for each day of the month.
        """
        month_wages = []  # Initialize an empty list to store the wages for each day of the month
        
        # Iterate through each day of the month and calculate the wage for that day
        for _ in range(self.month):
            month_wages.append(self.each_day_wage())  # Append the wage of each day to the list
        
        return month_wages  # Return the list of monthly wages



def main():
    employee_wage = Employee_monthly_wage()
    print(employee_wage.montly_wage())


# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
