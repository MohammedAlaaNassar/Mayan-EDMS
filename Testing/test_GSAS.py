
class Applicants():
    pass

class rec_letter_score():
    pass

#return -> List<Applicants>{applicant_id,name,program_id,gpa,faculty,department,university,docs}
def fetchApplicants():
    ID = Applicants()
    list_Applicant = list()
    list_Applicant.append(ID) 
    return list_Applicant

#return -> Applicants:{applicant_id,name,program_id,gpa,faculty,department,university,docs}
def fetchApplicant(applicant_id):
    ID = Applicants()
    return ID

#return -> int //score of applicantion form out of 10
def getApplicantInitialScore(applicant_id):
    return 1

#return -> int //score of applicant of all reviewers out of 10
def calcApplicantTotalScore(applicant_id):
    return 1

#return -> int //score of applicant of selected reviewer out of 10
def calcApplicantReviewerScore(applicant_id,reviewer_id):
    return 1

#return -> bool //status of submission
def submitScore(applicant_id,reviewer_id,init_score,gpa_score,rec_letter_score,resume_score):
    return True
    
##################################################################

# 1
def test_case1():
    result = fetchApplicants()
    if type(result) == list and isinstance(result[0], Applicants):
        print('test_case 1 Success')
    else:
        print('test_case 1 Fail')

# 2
def test_case2():
    applicant_id = 0
    result = fetchApplicant(applicant_id)
    if isinstance(result, Applicants):
        print('test_case 2 Success')
    else:
        print('test_case 2 Fail')

# 3
def test_case3():
    applicant_id = 0
    result = getApplicantInitialScore(applicant_id)
    if type(result) == int:
        print('test_case 3 Success')
    else:
        print('test_case 3 Fail')

# 4
def test_case4():
    applicant_id = 0
    result = calcApplicantTotalScore(applicant_id)
    if type(result) == int:
        print('test_case 4 Success')
    else:
        print('test_case 4 Fail')

# 5
def test_case5():
    applicant_id = 0
    reviewer_id = 0
    result = calcApplicantReviewerScore(applicant_id,reviewer_id)
    if type(result) == int:
        print('test_case 5 Success')
    else:
        print('test_case 5 Fail')

# 6
def test_case6():
    applicant_id = 0
    reviewer_id = 0
    init_score = 0
    gpa_score = 4.0
    resume_score = 0

    result = submitScore(applicant_id,reviewer_id,init_score,gpa_score,rec_letter_score,resume_score)
    if type(result) == bool:
        print('test_case 6 Success')
    else:
        print('test_case 6 Fail')


def test_gsas():

    print('Testing GSAS Project...')
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()
    return

test_gsas()