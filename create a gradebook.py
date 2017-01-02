#create a gradebook for all of your students.

"""
Create three dictionaries: lloyd, alice, and tyler.
Give each dictionary the keys "name", "homework", "quizzes", and "tests".
Have the "name" key be the name of the student (that is, lloyd's name should be "Lloyd")
and the other keys should be an empty list. (We'll fill in these lists soon!)
"""

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


#Below your code, create a list called students that contains lloyd, alice, and tyler.
students=[lloyd,alice,tyler]
#Print a hard copy for yourself. for each student in your students list, print out that student's data.
print "Hi Professor Mark. Here is your printed copy of each students results:"
print
for student in students:
    print student ["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]
    print
    print

# Write a function average that takes a list of numbers and returns the average.
"""
1. Define a function called average that has one argument, numbers.
2. Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a
variable called total.
3. Like the example above, use float() to convert total and store the result in total.
4. Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
5. Return that result.
"""
# Add your function below!
def average(numbers):
    total = sum(numbers)
    avg=float(total)/len(numbers)
    return avg
# Great now we need to compute a student's avrage using weighted averages.
"""
Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as
input and returns his/her weighted average.

1. Define a function called get_average that takes one argument called student.
2. Make a variable homework that stores the average() of student["homework"].
3. Repeat step 2 for "quizzes" and "tests".
4. Multiply the 3 averages by their weights and return the sum of those three.
Homework is 10%, quizzes are 30% and tests are 60%.
"""
def get_average(student):
    homework=average(student["homework"]) *.10
    quizzes=average(student["quizzes"]) * .30
    tests=average(student["tests"]) * .60
    return homework + quizzes + tests
#Now let's write a get_letter_grade function that takes a number score as input
# and returns a string with the letter grade that that student should receive.
"""
1. Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.
2. Inside your function, test score using a chain of if: / elif: / else: statements, like so:

If score is 90 or above: return "A"
Else if score is 80 or above: return "B"
Else if score is 70 or above: return "C"
Else if score is 60 or above: return "D"
Otherwise: return "F"

3. Finally, test your function! Call your get_letter_grade function with the result of get_average(lloyd).
Print the resulting letter grade.
"""
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Good! Now let's calculate the class average. You need to get the average for each student.
# Then calculate the average of those averages.
"""
1. Define a function called get_class_average that has one argument students.
You can expect students to be a list containing your three students.
2. First, make an empty list called results.
3. For each student item in the class list, calculate get_average(student)
and then call results.append() with that result.
4. Finally, return the result of calling average() with results.
"""
def get_class_average(students):
    results=[]
    for student in students:
        results.append(get_average(student))
    return average(results)
"""
Finally, print out the result of calling get_class_average with your students list.
Your students should be [lloyd, alice, tyler].
Then, print the result of get_letter_grade for the class's average.
"""
print get_class_average(students)
print get_letter_grade(get_class_average(students))