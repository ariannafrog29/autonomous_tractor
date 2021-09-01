import rospy
from geometry_msgs.msg import PoseStamped

rospy.init_node('GoalPublisher', anonymous=True)

sendGoal = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)


def movebase():

    goal = PoseStamped()
    goal.header.frame_id = "odom"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 3.0
    goal.pose.position.y = 0.0
    goal.pose.orientation.w = 1.0
    rate = rospy.Rate(2.0)
    
    while not rospy.is_shutdown():
     sendGoal.publish(goal)
     rate.sleep()



if __name__ == '__main__':
    try:
        movebase()
    except rospy.ROSInterruptException:
        pass