course = "Python for beginners"

course_modified = course.replace("for","4")

mail = '''
This is a
multiline
string
'''

print(course)
print(course_modified)
print(mail)

print('List of course, first character: ', course[0])
print('List of course, last character: ', course[-1])
print('List of course, multiple character: ', course[0:6])
print('List of course, remove first character: ', course[1:])
print('List of course, display all: ', course[:])

## exercice
name = 'Jeoffrey'
# we exclude the first and last character of the variable name
print(name[1:-1])

