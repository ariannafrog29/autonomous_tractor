import rospy
from sensor_msgs.msg import NavSatFix

rospy.init_node('GpsTargetPublisher', anonymous=True)
gps = rospy.Publisher('/gps_target', NavSatFix, queue_size=10)
 

def got_position():
 
    fix=NavSatFix()
    fix.header.frame_id="gps_target"
    fix.status.status=0
    fix.status.service=1

    fix.latitude=40.79882399539434
    fix.longitude=16.92312700802616
    rate = rospy.Rate(2.0)

    while not rospy.is_shutdown():
     gps.publish(fix)
     rate.sleep()

if __name__ == '__main__':
    try:
        got_position()
    except rospy.ROSInterruptException:
        pass
