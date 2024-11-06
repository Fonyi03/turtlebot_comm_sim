# Több Robot Kommunikációja és Navigációja - ROS2 Projekt

## Projekt Áttekintés
Ez a projekt a ROS2 (Robot Operating System 2) keretrendszert használja két szimulált Turtlebot robot közötti kommunikáció és együttműködés bemutatására egy Gazebo szimulációs környezetben. A robotok képesek megosztani a pozíciójukat és együttesen navigálni, miközben egy adott cél elérésén dolgoznak.

A projekt célja, hogy szemléltesse a több robot közötti adatmegosztást és valós idejű interakciókat egy szimulált környezetben, hardver hozzáférés nélkül.

## Fő Jellemzők
- **Több robot szimulációja**: Két Turtlebot robotot helyezünk el a Gazebo környezetben.
- **Kommunikáció és koordináció**: A robotok valós időben megosztják egymással a pozíciójukat és célpontjaikat.
- **3D vizualizáció**: A projekt az rviz2-ben jeleníti meg a robotok helyzetét, mozgását és célpontjait, 3D környezetben.

## Használt Eszközök és Követelmények
- **ROS2 Foxy**
- **Gazebo** - A 3D szimulációs környezet a robotok mozgásának és interakcióinak szimulálásához.
- **rviz2** - A robotok és a környezet valós idejű vizualizálásához.
- **Turtlebot3 csomagok** - A robotmodellek és alapértelmezett beállítások eléréséhez.

### Követelmények Telepítése
Telepítsd a szükséges ROS2 csomagokat:
```bash
sudo apt install ros-foxy-gazebo-ros-pkgs ros-foxy-turtlebot3*
```

## A Projekt Felépítése
- **Launch Fájlok**: A `multi_robot_launch.py` fájl két robotot indít el a Gazebo szimulációban, valamint elindítja az rviz2 alkalmazást.
- **Kommunikációs Csomópontok**: A `multi_robot_comm.py` csomópont kezeli a robotok közötti kommunikációt, és megosztja a pozíciójukat a szimuláció során.

## A Projekt Futtatása
Hozd létre a workspace-t, majd építsd fel a kódot:
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
```
Indítsd el a szimulációt és a 3D vizualizációt a következő paranccsal:
```bash
ros2 launch your_package_name multi_robot_launch.py
```

## A Projekt Részletei
- **Pozíciómegosztás**: Az egyik robot pozícióját átadjuk a másik robotnak, így képesek koordinálni egymás mozgását.
- **Célmeghatározás**: A robotok célpontokat határoznak meg a kommunikáció során, amelyeket valós időben követhetnek.

A `multi_robot_comm.py` csomópont egy ROS2 Pose üzenetet használ, hogy a robotok a pozíciójukat megosszák egymással. Az egyik robot célpontként követi a másik pozícióját, és valós időben reagál rá.

## A Kód Fájlstruktúrája
```plaintext
ros2_ws/
└── src/
    └── your_package_name/
        ├── launch/
        │   └── multi_robot_launch.py
        ├── scripts/
        │   └── multi_robot_comm.py
        └── rviz/
            └── multi_robot.rviz
```

## További Fejlesztési Lehetőségek
- **Több robot hozzáadása**: A projekt könnyen kiterjeszthető további robotok hozzáadásával és kommunikációs protokolljuk fejlesztésével.
- **Haladó kommunikáció**: További szenzoradatok megosztása (például lézeres távolságmérő adatai) a robotok jobb együttműködéséhez.
- **Interaktív HUD vagy irányító felület**: Opcionálisan hozzáadhatsz egy olyan kezelőfelületet, amely mutatja a robotok állapotát és pozícióját, vagy ahol beállítható a célpontjuk.

## Szerző és Karbantartás
Készítette: [A neved]  
GitHub: [GitHub repository link]  
Licenc: MIT