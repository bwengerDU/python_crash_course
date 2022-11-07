# 9-12 
from mod_9_12_2 import User
from mod_9_12_3 import Privileges
from mod_9_12_3 import Admin

admin_privileges = Admin('cody', 'baggins', 'baggins','admin', '1')
admin_privileges.privileges.show_privileges()