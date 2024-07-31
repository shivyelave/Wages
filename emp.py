'''


    @Author: Shivraj Yelave
    @Date: 31-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Employee Attendance


'''

import random

def employee_attendance():

    """

    Description:
        Function to randomly determine an employee's attendance status.
        0: Absent
        1: Present

    Returns:
        int: A random choice representing attendance status (0, 1).
    
    """

    # Randomly choose an attendance status from [0, 1]
    attendance = random.choice([0, 1])
    
    # Return the corresponding attendance status
    if attendance == 0:
        return 0  # Absent
    if attendance == 1:
        return 1  # Present
    

def calculate_wage_of_employee():
    
    """

    Description:
        Function to calculate the wage of an employee based on their attendance.

    Returns:
        int: The wage of the employee based on their attendance:
            - 0 for no attendance
            - 20*8 for full day attendance

    
    """
    
    attendance = employee_attendance()  # Get attendance status from employee_attendance function

    if attendance == 0:
        return 0  # No attendance, no wage

    if attendance == 1:
        return 20 * 8  # Full-day attendance, wage for 8 hours at $20/hour


def calculate_part_time_wage_of_employee():

    """

    Description:
        Function to calculate the wage of an employee for part-time work.
        This assumes a fixed part-time wage for 4 hours of work.

    Returns:
        int: The total wage for part-time work, calculated as 4 hours * $20/hour.
    
    """
    
    return 4 * 20  # Wage for 4 hours of work at $20 per hour

def main():
    print(calculate_part_time_wage_of_employee())  # Print the calculated part-time wage

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()
