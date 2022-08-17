class Task:
    def find_pairs(self, students):
        self.solution = {}
        map = list(set([i[0] for i in students]))
        for i in range(len(map)):
            left = set(c[1] for c in students if c[0]==map[i])
            for j in range(i+1, len(map)):
                right = set(c[1] for c in students if c[0]==map[j])
                self.solution.__setitem__(map[i]+','+map[j], list(left.intersection(right)))
    def display(self):
        for key,value in self.solution.items(): print(key,":",value)
        print()

if __name__ == "__main__":
    enrollments1 = [
        ["58", "Linear Algebra"],
        ["94", "Art History"],
        ["94", "Operating Systems"],
        ["17", "Software Design"],
        ["58", "Mechanics"],
        ["58", "Economics"],
        ["17", "Linear Algebra"],
        ["17", "Political Science"],
        ["94", "Economics"],
        ["25", "Economics"],
        ["58", "Software Design"],
    ]
    enrollments2 = [
        ["0", "Advanced Mechanics"],
        ["0", "Art History"],
        ["1", "Course 1"],
        ["1", "Course 2"],
        ["2", "Computer Architecture"],
        ["3", "Course 1"],
        ["3", "Course 2"],
        ["4", "Algorithms"]
    ]

    enrollments3 =  [
        ["23", "Software Design"],
        ["3", "Advanced Mechanics"],
        ["2", "Art History"],
        ["33", "Another"],
    ]
    obj = Task()
    obj.find_pairs(enrollments1)
    obj.display()
    obj.find_pairs(enrollments2)
    obj.display()
    obj.find_pairs(enrollments3)
    obj.display()
    
    
    
'''
Output : 
--------
17,94 : []
17,25 : []
17,58 : ['Software Design', 'Linear Algebra']
94,25 : ['Economics']
94,58 : ['Economics']
25,58 : ['Economics']

4,0 : []
4,3 : []
4,2 : []
4,1 : []
0,3 : []
0,2 : []
0,1 : []
3,2 : []
3,1 : ['Course 2', 'Course 1']
2,1 : []

23,2 : []
23,3 : []
23,33 : []
2,3 : []
2,33 : []
3,33 : []

'''
