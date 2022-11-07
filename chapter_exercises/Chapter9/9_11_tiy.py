#9-11 import privileges module and call a method to ensure it is working correctly. 
from Ch9_TIY import User
from Ch9_TIY import Admin
from Ch9_TIY import Privileges

admin_privileges = Admin('cody', 'baggins', 'cbaggins','admin', '1')
admin_privileges.privileges.show_privileges()