import rospy
from std_msgs.msg import Float64
import franka_gripper.msg

from panda_gazebo.srv import (
    SetGripperWidth,
    SetGripperWidthRequest
)
class Gripper:
    def __init__(self):
        rospy.sleep(1)
        pass

        
    def grasp(self, finger1_y, finger2_y):
        rospy.wait_for_service("/panda_control_server/panda_hand/set_gripper_width")
        gripper_control=rospy.ServiceProxy('/panda_control_server/panda_hand/set_gripper_width', SetGripperWidth)

        success=gripper_control(finger1_y+finger2_y,True,5,True)

        
        
