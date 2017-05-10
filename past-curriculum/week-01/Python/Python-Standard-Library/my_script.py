def send_greating(student_name):
    """"This function greats the student to the dsi course."""
    print "Hello {} and welcome to DSI 5!".format(student_name)
    
        
def celebrate_birthday(student_name):
    """"This function sends a birthday wish"""
    print "Happy birthday {}, and have a great year!".format(student_name)   
    
    
if __name__ == '__main__':
    
    
    student_name = raw_input("Enter your name: ")
    
    send_greating(student_name)