#!/usr/bin/env python3

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

rospy.init_node('application', anonymous=True)
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id="map"
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = 1.0
goal.target_pose.pose.orientation.w = 1.0


client.send_goal(goal)
wait = client.wait_for_result()

goal.target_pose.header.frame_id="map"
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = -1.3237
goal.target_pose.pose.position.y = 14.935

goal.target_pose.pose.orientation.z = -0.99
goal.target_pose.pose.orientation.w = 0.09

client.send_goal(goal)
wait = client.wait_for_result()