# Write your code here
def average(list):
    return round(sum(list) / len(list))
def format_grades(grades):
    return "\n".join(f"{key}: {average(grades)}" for key, grades in grades.items())
