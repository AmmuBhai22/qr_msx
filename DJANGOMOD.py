import os
#os.chdir('/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.11/site-packages/django/contrib/admin/templates/admin')
#f=open("base.html","r")
#print(f.read())
data=open("admin.py","r").read()
os.chdir('/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.11/site-packages/django/contrib/admin')
f=open("sites.py","r")
print(f.read())
f.close()