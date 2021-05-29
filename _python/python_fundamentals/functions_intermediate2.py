x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
# print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
# print(students)
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
# print(sports_directory)
# Change the value 20 in z to 30
z[0]['y']=30
# print(z)

def iterateDictionary(list):
    for dict in list:
        output = ""
        for key, value in dict.items():
            output += key + ' - ' + value + ', '
        output = output[:-2]
        print(output)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key, list):
    for dict in list:    
        print(dict[key])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key, value in dict.items():
        print('There are ' + str(len(value)) + ' ' + str(key))
        print(*value, sep = "\n")
        print("\n")

printInfo(dojo)