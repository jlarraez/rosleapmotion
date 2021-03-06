#!/usr/bin/env python
__author__ = 'flier'
import rospy
import leap_interface
from leap_motion.msg import leap2
from leap_motion.msg import leapros2

# Obviously, this method publishes the data defined in leapros.msg to /leapmotion/data
def sender():
    li = leap_interface.Runner()
    li.setDaemon(True)
    li.start()
    # pub     = rospy.Publisher('leapmotion/raw',leap)
    pub_ros   = rospy.Publisher('leapmotion/data',leapros2)
    rospy.init_node('leap_pub')

    while not rospy.is_shutdown():
        hand_direction_   = li.get_hand_direction()
        hand_normal_      = li.get_hand_normal()
        hand_palm_pos_    = li.get_hand_palmpos()
        hand_pitch_       = li.get_hand_pitch()
        hand_roll_        = li.get_hand_roll()
        hand_yaw_         = li.get_hand_yaw()
        hand_gesture_     = li.get_hand_gesture()
        hand_fingerdistance_     = li.get_fingers_distance()
        hand_fingerspos1_     = li.get_fingers_pos1()
        hand_fingerspos2_     = li.get_fingers_pos2()
	msg = leapros2()
        msg.direction.x = hand_direction_[0]
        msg.direction.y = hand_direction_[1]
        msg.direction.z = hand_direction_[2]
        msg.normal.x = hand_normal_[0]
        msg.normal.y = hand_normal_[1]
        msg.normal.z = hand_normal_[2]
        msg.palmpos.x = hand_palm_pos_[0]
        msg.palmpos.y = hand_palm_pos_[1]
        msg.palmpos.z = hand_palm_pos_[2]
        msg.ypr.x = hand_yaw_
        msg.ypr.y = hand_pitch_
        msg.type_gesture = hand_gesture_
	msg.ypr.z = hand_roll_
	msg.finger_distance=hand_fingerdistance_ 
	msg.Pos_finger1.x=hand_fingerspos1_[0] 
	msg.Pos_finger1.y=hand_fingerspos1_[1] 
	msg.Pos_finger1.z=hand_fingerspos1_[2]
	msg.Pos_finger2.x=hand_fingerspos2_[0] 
	msg.Pos_finger2.y=hand_fingerspos2_[1] 
	msg.Pos_finger2.z=hand_fingerspos2_[2]
        # We don't publish native data types, see ROS best practices
        # pub.publish(hand_direction=hand_direction_,hand_normal = hand_normal_, hand_palm_pos = hand_palm_pos_, hand_pitch = hand_pitch_, hand_roll = hand_roll_, hand_yaw = hand_yaw_)
        pub_ros.publish(msg)
        # Save some CPU time, circa 100Hz publishing.
        rospy.sleep(0.01)


if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass
