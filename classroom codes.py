def attendance_tracking():
    numlst = input("Enter the following(single line only): class, \nnumber of absentees on monday, \nnumber absentees on tuesday, \nnumber absentees on wednesday, \
\nnumber absentees on thursday, \nnumber of absentees on friday.")
    lst = numlst.split(", ")
    opstring = "Total number of absentees on Monday: {0} \nTotal number of absentees on Tuesday: {1} \nTotal number of students on Wednesday: {2} \nTotal number of students on Thursday: {3} \nTotal number of students on Friday: {4}:".format(lst[1], lst[2], lst[3], lst[4], lst[5])
    
    print(opstring)
