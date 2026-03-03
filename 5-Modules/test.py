# when developing project we call this in test.py file

# go to 5-Modules folder == cd 5-Modules
# then run PS D:\python-for-dsa\5-Modules> python test.py

from package.maths import *

print(addition(2,3))
print(sub(3,2))


# 

from package.subpackage.multi import multiply
print(multiply(3,4))