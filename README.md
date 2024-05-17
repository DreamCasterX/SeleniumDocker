## Selenium Docker Test Config

#### [SOP]

##### 1).  Install Docker

##### 2).  Install docker images
+  [Test a single browser at one time]
    + docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-firefox
    + docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome
    + docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-edge

+  [Test multiple browsers at the same time]
    + docker pull selenium/hub
    + docker pull selenium/node-chrome
    + docker pull selenium/node-firefox
    + docker pull selenium/node-edge
    + docker compose up

##### 3).  Open the browser
+ localhost:4444 (Selenium Grid)
+ localhost:7900 (noVNC) 

##### 4).  Run python test scripts 
---
#### [Note]
- Default hub password is `secret`, if you want to change it, set the env variable in docker-compose.yml
    - `SE_VNC_PASSWORD=xxx` = Set your own password
    - `SE_VNC_NO_PASSWORD=1` = Don't prompt for password 
