``` mermaid
graph LR;

Slicksocket --> BlackBox
BlackBox --> DeadSwitch
OGRE --> HunterShot
Prosthetic --> PanzerFist
BlackBox --> RemoteUplink
SpinalRig --> SockPuppet
SpinalRig --> SpiderMount

BlackBox["1 Black Box<br>200,000"]
click BlackBox href "../chop-shop#cyberware"
DeadSwitch["0 Dead Switch<br>5,000"]
click DeadSwitch href "../chop-shop#cyberware"
HoloProjector["1 Holo Projector<br>750"]
click HoloProjector href "../chop-shop#cyberware"
HunterShot["1 HunterShot<br>4,500"]
click HunterShot href "../chop-shop#cyberware"
Loudmouth["0 Loudmouth<br>500"]
click Loudmouth href "../chop-shop#cyberware"
OGRE["1 OGRE<br>24,000"]
click OGRE href "../chop-shop#cyberware"
PanzerFist["3 PanzerFist<br>5,000,000"]
click PanzerFist href "../chop-shop#cyberware"
Prosthetic["0 Prosthetic<br>2,000"]
click Prosthetic href "../chop-shop#cyberware"
RemoteUplink["1 Remote Uplink<br>2,000,000"]
click RemoteUplink href "../chop-shop#cyberware"
Slicksocket["1 Slicksocket<br>500"]
click Slicksocket href "../chop-shop#cyberware"
SockPuppet["1+ SockPuppet<br>1,000,000"]
click SockPuppet href "../chop-shop#cyberware"
SpiderMount["0 Spider Mount<br>250,000"]
click SpiderMount href "../chop-shop#cyberware"
SpinalRig["1 Spinal Rig<br>150,000"]
click SpinalRig href "../chop-shop#cyberware"
TerminalJack["1 Terminal Jack<br>750"]
click TerminalJack href "../chop-shop#cyberware"

Slicksocket --> EsperneticFeedbackLoop
Slicksocket & TerminalJack --> GodMode
Slicksocket & HoloProjector --> Holopet
Slicksocket --> LookyLoo
Slicksocket & BlackBox & TerminalJack --> MachineCode
Slicksocket --> SentinelSystem
Slicksocket --> Skillslick
Slicksocket --> TwitchBooster
Loudmouth --> VoxBox

EsperneticFeedbackLoop["1 Espernetic Feedback Loop<br>36,000"]
click EsperneticFeedbackLoop href "../icebox#slickware"
GodMode["1 God Mode<br>10,000"]
click GodMode href "../icebox#slickware"
Holopet["0 Holopet<br>24,000"]
click Holopet href "../icebox#slickware"
LookyLoo["0 Looky-Loo<br>550"]
click LookyLoo href "../icebox#slickware"
MachineCode["4 Machine Code<br>350,000"]
click MachineCode href "../icebox#slickware"
SentinelSystem["2 Sentinel System<br>120,000"]
click SentinelSystem href "../icebox#slickware"
Skillslick["1-3 Skillslick<br>50,000-1,000,000"]
click Skillslick href "../icebox#slickware"
TwitchBooster["1 Twitch Booster<br>4,000"]
click TwitchBooster href "../icebox#slickware"
VoxBox["1 Vox Box<br>24,000"]
click VoxBox href "../icebox#slickware"

classDef slick fill:#464,stroke:#0a0,stroke-width:2px;
classDef cyber fill:#646,stroke:#a0a,stroke-width:2px;

class BlackBox,DeadSwitch,HoloProjector,Loudmouth,HunterShot,OGRE,PanzerFist,Prosthetic,RemoteUplink,Slicksocket,SockPuppet,SpiderMount,SpinalRig,TerminalJack cyber;
class EsperneticFeedbackLoop,GodMode,Holopet,LookyLoo,MachineCode,SentinelSystem,Skillslick,TwitchBooster,VoxBox slick;
```
