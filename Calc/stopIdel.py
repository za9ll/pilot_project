import os

find_container = 'docker ps -a | grep \'calc\''
stop_container = 'docker stop \'calc\''
find_image = 'docker images | grep \'web_calc\''
del_image = 'docker rmi \'web_calc\''

if os.system (find_container) == 0:
    os.system (stop_container)
else:
    print ('container not found \n')

if os.system (find_image) == 0:
    os.system (del_image)
else:
    print ('image not found \n')
