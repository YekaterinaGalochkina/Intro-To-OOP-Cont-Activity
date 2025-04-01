from school_schedule.student import Student

def test_attributes_of_class_of_student():
    #Arrange
    name = "Alice"
    grade = "junior"
    classes = ["Math", "Science"]
    
    #Act
    student = Student(
        name,
        grade,
        classes
    )
    # assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes
    
def test_add_class_if_class_name_is_empty():
    #Arrange
    name = "Alice"
    grade = "junior"
    classes = ["Math", "Science"]
    class_name = None
    
    student = Student(
        name,
        grade,
        classes
    )
    #Act
    
    new_classes = student.add_class(class_name)
    
    #Assert
    assert new_classes == classes
    
def test_get_num_classes_length():
    #Arrange
    name = "Alice"
    grade = "junior"
    classes = ["Math", "Science"]
    
    student = Student(
        name,
        grade,
        classes
    ) 
    #Act
    length_of_classes = student.get_num_classes()
    
    #Assert
    assert length_of_classes == 2