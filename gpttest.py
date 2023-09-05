import paramiko

# create a new SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server
client.connect('hostname', username='username', password='password')

# execute a command on the remote server
stdin, stdout, stderr = client.exec_command('ls /')

# print the output of the command
print(stdout.read().decode())

# close the connection
client.close()
