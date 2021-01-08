import PIL.ImageGrab as c
import os
import getpass

a=getpass.getuser()
a1='C:\\user\\'
a2='\\Desktop'
a3=a1+a+a2
os.chdir(a3)

obj=c.grab()
obj.save("Screenshot.png","png")
obj.show()




		