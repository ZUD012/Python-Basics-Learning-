class Student :
    def __init__ (self , Full_name ) :
        self.name = Full_name
       
    
    def marks_Input(self):
        arr = []
        sum  = 0
        a = int(input("Enter the Marks scored in Maths"))
        arr.append(a)
        b = int(input("Enter The marks Scored in Biology"))
        arr.append(b)
        c = int(input("Enter the marks scored in Computer"))
        arr.append(c)
        for i in arr :
            sum += i 
        print("Hello" ,self.name , "your Average Score is  " , sum/3 )

s1 = Student("ZUDO")
s1.marks_Input()

        
        
        