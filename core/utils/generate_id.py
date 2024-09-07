import uuid

def GenerateApplicationId():
    primary_id = str(uuid.uuid4().int)[:10]
    student_id = 'ST' + primary_id
    return student_id