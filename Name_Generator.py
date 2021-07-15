import random
#************************************Data************************************

Name_inputs = ["ramesh","mukesh","hannu","pawan","gopal","Sunita","Kamlesh"
,"Aashish","madhu","priya","madhav","Kamlesh","Bobby","Sunny","priya"]

#***********************************Functions*******************************

def Take_first_3_letters(string):
    return string[0:3]

def Generate_names(input_data):
    a = Take_first_3_letters(input_data[random.randint(0,len(input_data)-1)])
    b = input_data[random.randint(0,len(input_data)-1)][3:]
    if (a+b) in Name_inputs:
        Generate_names(Name_inputs) 
    return a + b

#**********************************Main Code********************************

final_output = Generate_names(Name_inputs)
if final_output in Name_inputs:
    final_output = Generate_names(Name_inputs)
print(final_output)
