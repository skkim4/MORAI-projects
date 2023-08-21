# LAKS 방법
sliding_window로 부터 얻어진 좌우 차선의 가운데 지점에서 좌우로 치우처진 정도의 0번째 index ~ 4번째 index 값에
각각 가중치를 적용하여 저장한 후 이를 전부 더하고 스케일링 하여 Steering 값에 대한 제어량으로 계산합니다.
cmd_vel topic의 data에 linear.x 값은 0.6 으로 지정하고
위에서 나온 steering에 대한 제어량을 angular.z 값에 넣어줍니다.
그 후에 cmd_vel 토픽을 publish 합니다.

<p align="center">
<img src ="https://github.com/skkim4/MORAI-projects/assets/128979311/a239fa4a-12a0-41e7-b2b3-25588e45e2db" width="300" height="250" >
</p>
