'''
    This is the team allocator project solution example project
'''


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = [] 

    for iter in student_list:
        if "Durban" in iter:
            dbn_students.append(iter)

    return dbn_students


def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []

    for iter in student_list:
        if "Cape Town" in iter:
            cpt_students.append(iter)

    return cpt_students


def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []

    for iter in student_list:
        if "Johannesburg" in iter:
            jhb_students.append(iter)

    return jhb_students


def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []

    for iter in student_list:
        if "Phokeng" in iter:
            nw_students.append(iter)

    return nw_students

    
def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical_students = []
    for iter in dbn_students:
        if "Durban Physical" in iter:
            dbn_physical_students.append(iter)
    return dbn_physical_students


def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    dbn_physical_teams = []
    for i in range(0, len(dbn_physical_students), 4):
        dbn_teams = dbn_physical_students[i: i + 4]
        dbn_physical_teams.append(dbn_teams)



    return dbn_physical_teams


def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    with open("virtual_teams.txt", "w") as f:
        for j in durban_physical_teams:
            f.write(j + "\n")




def cpt_physical_students(cpt_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_physical_students = []
    for iter in cpt_students:
        if "cape town physical" in iter.lower():
            cpt_physical_students.append(iter)
    
    return cpt_physical_students


def cpt_physical_teams(cpt_physical_teams):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    
    # teams = []
    cpt_phys_teams_ls = []

    for iter in range(0, len(cpt_physical_teams), 4):
        teams = cpt_physical_teams[iter: iter + 4]
        cpt_phys_teams_ls.append(teams)
        

    return cpt_phys_teams_ls


def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "w") as f:
        for i in capetown_final_teams:
            f.write(i + "\n")


def jhb_physical_students(physical_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    jhb_physical_students = []

    for iter in physical_students:
        if "Johannesburg Physical" in iter:
            jhb_physical_students.append(iter)

    return jhb_physical_students


def jhb_physical_teams(jhb_physical_teams):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    jhb_phys_teams_ls = []

    for i in range(0, len(jhb_physical_teams), 4):
        jhb_teams = jhb_physical_teams[i: i + 4]
        jhb_phys_teams_ls.append(jhb_teams)

    return jhb_phys_teams_ls

def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''


def nw_physical_students(physical_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    nw_physical_students = []
    for iter in physical_students:
        if "Phokeng Physical" in iter:
            nw_physical_students.append(iter)

    return nw_physical_students


def nw_physical_teams(nw_physical_teams):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''

    nw_phys_teams_ls = []

    for i in range(0, len(nw_physical_teams), 4):
        nw_teams = nw_physical_teams[i: i + 4]
        nw_phys_teams_ls.append(nw_teams)

    return nw_physical_teams


def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []
    for iter in student_list:
        if "Virtual" in iter:
            virtual_campus.append(iter)

    return virtual_campus


def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []
    for i in range(0, len(virtual_students_list), 4):
        virtual_teams1 = virtual_students_list[i: i + 4]
        virtual_teams.append(virtual_teams1)
    return virtual_teams


def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    stu_list = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']

    # print(dbn_campus_students(stu_list))
    #print(cpt_campus_students(stu_list))
    #print(nw_campus_students(stu_list))
    # print(jhb_physical_students(stu_list))
    #the = jhb_physical_students(stu_list)
    #print(jhb_physical_teams(the))
    #cpt_teams_file(stu_list)
    dbn_teams_file(stu_list)

