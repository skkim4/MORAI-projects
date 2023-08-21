### mapping in MORAI-simulation
- mapping 기본 세팅
  MORAI 키코 sensor 및 네트워크 설정
	- sensor 는 llidar 만
  - lidar 의  frame_id lidar로 설정 ( 배치는 x:0.25, y:0.0, z: 0.15)
	- 네트워크 세팅은( tf 끄고, cmd_vel, scout_status 는 켜고)
 ``` Linux
$ roslaunch rosbridge_server rosbridge_websocket.launch
$ roslaunch pointcloud_to_laserscan sample_node.launch
$ roslaunch wego tf_setting.launch
$ roslaunch wego gmapping.launch
맵 다 그린 후
$ rosrun map_server map_saver
$ roslaunch wego navigation.launch
```
  
<p align="center">
<img src ="https://github.com/skkim4/MORAI-projects/assets/128979311/c98ccd26-d902-4262-81a3-1cca6eaee6d0" width="300" height="250" >
</p>

```Linux
$ roslaunch rosbridge_server rosbridge_websocket.launch
$ roslaunch pointcloud_to_laserscan sample_node.launch
$ roslaunch kw_tf tf_setting.launch
$ roslaunch gmapping slam_gmapping_pr2.launch
```
<p align="center">
<img src ="https://github.com/skkim4/MORAI-projects/assets/128979311/c98ccd26-d902-4262-81a3-1cca6eaee6d0" width="300" height="250" >
</p>

<p align="center">
<img src ="https://github.com/skkim4/MORAI-projects/assets/128979311/a8992895-9331-44eb-847a-90b5ffcbee23" width="300" height="250" >
</p>

