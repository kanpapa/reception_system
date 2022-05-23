# reception_system

# 使い方

1. docker コンテナの起動

   ```
   git clone https://github.com/sibafb/akiemon_dockerfiles.git
   cd ./dockerfiles/noetic-create-raspi
   ./build_docker_image.bash
   ./run-docker_container.bash
   ```

1. 受付システムのRasberryPiで本リポジトリをクローン

   ```
   git clone https://github.com/sibafb/reception_system.git --recursive
   ```

1. Catkin make する

   ```
   catkin_make 
   ```

1. IPアドレスを編集する


   ```
   ac_and_sub_topics.html
   const ros_server = 'ws://192.168.0.XXX:9090';　// Roomba側のIPアドレス
   ```

1. roslaunchを起動

   ```
   roslaunch reception_main reception_system.launch
   ```

1. ブラウザを開き、下記にアクセス

   http://localhost:8085/ros_bridge_sandbox/ac_and_sub_topics.html

1. Roomba側のrosbridgeを起動

   ```
   roslaunch rosbridge_server rosbridge_websocket.launch
   ```


# pin assign

|  Sensor  |  GPIO  |
| ---- | ---- |
|  human_sensor  |  22  |
|  push_button  |  23  |
|  push_button_led  |  25  |

```
pi@raspberrypi:~ $ pinout
,--------------------------------.
| oooooooooooooooooooo J8   +======
| 1ooooooooooooooooooo  PoE |   Net
|  Wi                    1o +======
|  Fi  Pi Model 4B  V1.2 oo      |
|        ,----. +---+         +====
| |D|    |SoC | |RAM|         |USB3
| |S|    |    | |   |         +====
| |I|    `----' +---+            |
|                   |C|       +====
|                   |S|       |USB2
| pwr   |hd|   |hd| |I||A|    +====
`-| |---|m0|---|m1|----|V|-------'

Revision           : c03112
SoC                : BCM2711
RAM                : 4GB
Storage            : MicroSD
USB ports          : 4 (of which 2 USB3)
Ethernet ports     : 1 (1000Mbps max. speed)
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 1
Display ports (DSI): 1

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

POE:
TR01 (1) (2) TR00
TR03 (3) (4) TR02
```
