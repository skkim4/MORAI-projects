# 2. pub_camera
이 코드는 ROS의 cv_bridge 를 이용하여 Morai 시뮬레이션의 camera 토픽을 openCV에서 취할 수 있는 이미지 변환(gray scale image & rgb_image)를 취하고 ros image 형태로 publish하는 코드이다. 

**1. init**
```python
    rospy.init_node('camera', anonymous=True)
    self.bridge=CvBridge()
```
