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