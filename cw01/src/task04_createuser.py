import os

for index in range (1,101):
    command = "adduser student{}".format(index)
    os.system(command)
    command = "yes student{} | passwd student{}".format(index, index)
    os.system(command)
    command = "chage -d 0 student{}".format(index)
    os.system(command)


