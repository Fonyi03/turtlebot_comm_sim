# **Turtlebot Kommunikációs Projekt**

Ez a projekt demonstrálja két robot közötti kommunikációt **ROS 2** segítségével, egy **Gazebo** szimulált világban, ahol a **RViz2** felület jeleníti meg a kommunikáció vizuális markerjeit.

---

## **Projekt célja**

A cél egy olyan ROS 2 alapú környezet létrehozása, amely:
1. Kommunikációt valósít meg két robot között.
2. Gazebo szimulációs világban szimulálja a robotokat.
3. Marker üzeneteket jelenít meg RViz2 segítségével.

---

## **Szükséges eszközök**

- **ROS 2 Humble**
- **Gazebo 11** (turtlebot3 modellek támogatásával)
- **RViz2**
- **Python 3.10**
- **Colcon** (ROS 2 build rendszer)

---

## **Telepítés**

### 1. **A repository klónozása**

```bash
git clone https://github.com/fonyi03/turtlebot_comm_ws.git
cd turtlebot_comm_ws
```

### 2. **A szükséges csomagok telepítése**
```bash
sudo apt update
sudo apt install ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-msgs ros-humble-visualization-msgs
```

### 3. A workspace építése
```bash
cd ~/turtlebot_comm_ws
colcon build
source install/setup.bash
```

## **Projekt felépítése**
1. ### **Fő könyvtárak és fájlok**
```bash
turtlebot_comm_ws/
├── src/
│   └── turtlebot_comm/
│       ├── package.xml
│       ├── setup.py
│       ├── turtlebot_comm/
│       │   ├── topic_publisher.py
│       │   ├── subscriber_node.py
│       │   └── communication_node.py
│       └── worlds/
│           └── multi_robot_with_evata.sdf
├── install/
├── build/
└── log/
```

    topic_publisher.py: Markereket publikál a /robot_burger/marker topicra.
    subscriber_node.py: Feliratkozik a /robot_burger/marker topicra és logolja a marker adatokat.
    communication_node.py: További vizuális markereket publikál a kommunikáció állapotáról.

2. Szimulációs világ (Gazebo)

A multi_robot_with_evata.sdf fájl tartalmazza a Gazebo világ beállításait:

    Egy Turtlebot3 Burger modellt.
    Egy másik Evata modellt.

## **Futtatás**

### 1. Gazebo szimuláció elindítása

```bash
gazebo --verbose src/turtlebot_comm/worlds/multi_robot_with_evata.sdf
```

### 2. A ROS 2 csomagok futtatása

#### Topic Publisher elindítása

```bash
ros2 run turtlebot_comm topic_publisher
```

#### Subscriber Node elindítása

```bash
ros2 run turtlebot_comm subscriber_node
```

#### Communication Node elindítása

```bash
ros2 run turtlebot_comm communication_node
```

### 3. RViz2 konfigurálása

Indítsd el RViz2-t:

```bash
rviz2
```

#### Fixed Frame beállítása:
Állítsd a Fixed Frame mezőt `odom` értékre.

#### Markerek hozzáadása:
Menj a Displays panelre, kattints Add.
Válaszd a By Topic fület, majd válaszd a következő topicokat:
- `/robot_burger/marker`
- `/communication_marker`

Ellenőrizd, hogy a markerek megfelelően jelennek meg.

## **A működés ellenőrzése**

- Figyeld a markerek mozgását, színét vagy pozícióját az RViz2 felületen.
- Ellenőrizd a terminálban a `subscriber_node.py` által logolt adatokat.

## **Hibaelhárítás**

- Nincs marker vizualizáció:
  - Ellenőrizd a Fixed Frame értékét (`odom`).
  - Győződj meg róla, hogy a megfelelő topicokat adtad hozzá RViz2-ben.

- Nincs adat a topicban:
  ```bash
  ros2 topic echo /robot_burger/marker
  ros2 topic echo /communication_marker
  ```

## **Verziókövetés**

A projekt aktuális állapotát, a frissítéseket és a kódot a GitHub Repository oldalon találod.

## **Szerző**

- Név: Fonyó
- Email: fonyo.nate@hallgato.sze.hu
