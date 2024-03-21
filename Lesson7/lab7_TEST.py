import paramiko
import time
import re

host = "10.31.70.209"
log = "restapi"
pas = "j0sg1280-7@"

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh_connection.connect(host,
                       username=log,
                       password=pas,
                       look_for_keys=False,
                       allow_agent=False)

# session = ssh_connection.invoke_shell()
stdin, stdout, stderr = ssh_connection.exec_command(command="show interfaces\n", bufsize=65536, get_pty=True)

# for i in stdout:
#     print(i)

#print(stdout.readlines())


for current_line in stdout:
    # print(current_line)
    if m := re.match("^([A-Z].+?) is", current_line):
        print("Interface " + m.group(1))
    if m := re.match("^.+?([0-9]+) packets input, ([0-9]+) bytes", current_line):
        print("Packets/bytes input: ", m.group(1), "/", m.group(2))

    if m := re.match("^.+?([0-9]+) packets output, ([0-9]+) bytes", current_line):
        print("Packets/bytes output: ", m.group(1), "/", m.group(2))


ssh_connection.close()