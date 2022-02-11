students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def Update():
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

    x[1][0] = 15
    students[0]['last_name'] = "Bryant"
    sports_directory['soccer'][0] = 'Andres'
    z[0]['y'] = 30
    print(x)
    print(students)
    print(sports_directory)
    print(z)

def iterateDictionary(list):
    x = len(list)
    for i in range(x):
        full_name = f"first_name - {list[i]['first_name']}, last_name - {list[i]['last_name']}"
        print(full_name)

def iterateDictionary2(key_name, list):
    x = len(list)
    for i in range(x):
        name = list[i][key_name]
        print(name)

def printInfo(dict):
    list1 = dict.get('locations')
    list2 = dict.get('instructors')
    list1_num = len(list1)
    list2_num = len(list2)
    
    print(f"{list1_num} Locations")
    for i in range(list1_num):
        print(list1[i])
    print(f"\n{list2_num} Instructors")
    for i in range(list2_num):
        print(list2[i])



Update()
iterateDictionary(students) 
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
printInfo(dojo)