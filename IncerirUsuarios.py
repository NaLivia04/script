import subprocess

new_user_name = "Ana"
new_user_pass = "1234"
# cria usuario no sistema

subprocess.run(["sudo","useradd",new_user_name])
subprocess.run(["sudo","passwd",new_user_name], input=f"{new_user_pass}\n{new_user_pass}\n".encode())