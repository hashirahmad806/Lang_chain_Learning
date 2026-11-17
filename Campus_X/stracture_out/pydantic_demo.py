from pydantic import BaseModel , field_validator ,EmailStr,Field


class Student(BaseModel):
    name : str
    age : int
    course : str
    email : EmailStr   
    cgpa : float = Field(ge=0,le=4 , description="CGPA of the student")

new_student={
    "name" : "Muneeb",
    "age" : 19,
    "course" : "AI",
    "email" : "hashir@gmail.com",
    "cgpa" : 4.0
}
 
student = Student(**new_student)
print(student)
