#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

disToObstacle = 0.8

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "Distance to obstacle - %s", msg.ranges[300])

    if msg.ranges[300] > disToObstacle:
        print("In")
        move.linear.x = 0.5
        move.angular.z = 0

    if msg.ranges[300] <= disToObstacle:
        print("Out")
        move.linear.x = 0
        move.angular.z = 0.4

    pub.publish(move)


rospy.init_node('sub_node')
sub = rospy.Subscriber('/scan', LaserScan, callback)    
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(5)
move = Twist()
rospy.spin()