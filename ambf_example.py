# Import the Client from ambf_client package
from ambf_client import Client
import time

# Create a instance of the client
_client = Client()

# Connect the client which in turn creates callable objects from ROS topics
# and initiates a shared pool of threads for bi-directional communication
_client.connect()

print('\n\n----')
input("We can see what objects the client has found. Press Enter to continue...")
# You can print the names of objects found. We should see all the links found
print(_client.get_obj_names())

# Lets get a handle to PSM and ECM, as we can see in the printed
# object names, 'ecm/baselink' and 'psm/baselink' should exist
psm_handle = _client.get_obj_handle('psm/baselink')

# Let's sleep for a very brief moment to give the internal callbacks
# to sync up new data from the running simulator
time.sleep(0.2)

print('\n\n----')
input("Let's Get Some Pose Info. Press Enter to continue...")
# Not we can print the pos and rotation of object in the World Frame
print('ECM Base Pos:')
print(psm_handle.get_pos())

print(' ')
print('PSM Base Rotation as Quaternion:')
print(psm_handle.get_rot())

print(' ')
print('MTM Wrist Fixed Rotation:')
print(psm_handle.get_rpy())

print('\n\n----')
input("Let's get Joints and Children Info. Press Enter to continue...")
# We can get the number of children and joints connected to each object as
psm_num_joints = psm_handle.get_num_joints() # Get the number of joints of this object
psm_children_names = psm_handle.get_children_names() # Get a list of children names belonging to this obj
print('Number of Joints in ECM:')
print(psm_num_joints)

print(' ')
print('Name of PSM\'s children:')
print(psm_children_names)
psm_handle.set_joint_pos(1, -0.2)

print('\n\n----')
input("Let's clean up. Press Enter to continue...")
# Lastly to cleanup
_client.clean_up()