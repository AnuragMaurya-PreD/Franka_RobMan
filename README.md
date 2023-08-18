# ReadME

### Steps for pick and place task

**To spawn the robot in the prorobman world:**

```bash
roslaunch pick_and_place spawn_sample.launch
```

**To broadcast cube pose as parameters**

```bash
rosrun pick_and_place cube_param.py
```

********To perform pick and place task********

```bash
rosrun pick_and_place pick_box.py
```

### For modifying scripts according to your task

### Demo Script

```python
import rospy
from pick_and_place_module.pick_and_place import PickAndPlace

pick_and_place = PickAndPlace(0.05, 0.5) # gripper_offset, intermediate_z_stop
pick_position=[1,2,3]
pick_orientation=[1.57,3.14,0] # Euler values 

place_position=[2,3,4]
place_orientation=[1.57,3.14,0]
    
pick_and_place.setPickPose(*pick_position,*pick_orientation) #setting the pick pose
pick_and_place.setDropPose(*place_position,*place_orientation) #setting the place pose
pick_and_place.setGripperPose(0.02, 0.02) # gripper finger1 movemen, gripper finger 2 movement 

pick_and_place.execute_pick_and_place() # pick and place in joint space
pick_and_place.execute_cartesian_pick_and_place() # pick and place in cartesian space
```

For modifying the package to your task, make changes to the **generate_waypoints** function in the **pick_and_place.py** script

### Acknowledgments

- Staa, R., & Pan, W. rickstaa/panda-gazebo [Computer software]. [https://github.com/rickstaa/stable-gym](https://github.com/rickstaa/stable-gym)
- [https://github.com/iROSA-lab/ProRobMan](https://github.com/iROSA-lab/ProRobMan)
