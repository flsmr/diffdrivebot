# diffdrivebot
mobile robot with gripper, cam, and lidar

## USB Motor Connection
Install pyserial for communication with Arduino via USB
```
pip3 install pyserial
```
If usb port does not get shown using
```
sudo dmesg | grep tty
```
Try to deactivate braile reader, which was grabbing the port on my machine via
```
sudo apt remove brltty
```
Unplug and plugin USB device after this command.
(see https://askubuntu.com/questions/786367/setting-up-arduino-uno-ide-on-ubuntu)

To grant access to the usb port, also add user to dialout group
```
sudo usermod -a -G dialout $USER
```
Logout and login after this statement.
(see https://askubuntu.com/questions/133235/how-do-i-allow-non-root-access-to-ttyusb0)

## IMU Wiring and Calibration
For calibration the following tool is helpful:
https://github.com/adafruit/Adafruit_CircuitPython_BNO055

Enable I2C and set permissions:
https://roboticsbackend.com/raspberry-pi-hardware-permissions/#Enable_UART

Wiring diagram
https://robofoundry.medium.com/using-bmi160-imu-with-ros2-ecb550851efa
