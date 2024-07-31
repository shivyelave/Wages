'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Employee wages per month


'''

import random

wage_per_hr = 20  # Wage per hour
full_day_working_hrs = 8  # Working hours for a full day
half_day_working_hrs = 4  # Working hours for a half day

def employee_attendance():

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

def calculate_wage_of_employee(attendance):

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
        return full_day_working_hrs * wage_per_hr  # Full-day attendance, wage for 8 hours at $20/hour

def calculate_part_time_wage_of_employee():
    
    """
    
    Description:
        Function to calculate the wage of an employee for part-time work.
        This assumes a fixed part-time wage for 4 hours of work.

    Returns:
        int: The total wage for part-time work, calculated as 4 hours * $20/hour.
    
    """
    
    return half_day_working_hrs * wage_per_hr  # Wage for 4 hours of work at $20 per hour

def main():
    
    # Get attendance status from employee_attendance function
    attendance = employee_attendance()
    
    # Calculate wage based on attendance status using pattern matching
    match attendance:
        case 0:
            wage = calculate_wage_of_employee(attendance)  # No attendance
        case 1:
            wage = calculate_wage_of_employee(attendance)  # Full-day attendance
        case 2:
            wage = calculate_part_time_wage_of_employee()  # Half-day attendance

    # Print the calculated wage
    print(wage)

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
