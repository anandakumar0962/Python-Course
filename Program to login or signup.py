class User:
    
    user_data = [{'anand0962@gmail.com':'anand0962'},{'vignesh2706@gmail.com':'vignesh2706'}]
    def __init__(self,email_id,password,user_data):
        self.email_id = email_id
        self.password = password
        self.user_data = user_data

    def login():
        
        user_data = [{'anand0962@gmail.com':'anand0962'},{'vignesh2706@gmail.com':'vignesh2706'}]
        print("Login to experience our service")
        mailid = input("Enter your email\n")
        passcode = input ("Enter your password\n")
        data = {mailid : passcode}
    
        for i in user_data:
            if data in user_data:
                print("login successfully")
                break
            else:
                print("Does not exist")                
                break
    def signup():
        print("Welcome to Signup page")  
        email = input("Enter your Email\n ")
        password = input("Enter a New Password\n")
        confirmpassword = input("Re enter to confirm password\n")
        while password == confirmpassword:
            new_id = {email : confirmpassword}
            user_data.append(new_id)
        
        print("Password does not match")
            

        
        
print("Welcome to Home Service Solution ")
User.login()
User.signup()
    
