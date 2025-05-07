# Touchlab ROS Sensor Driver

## Dependencies:

- Touchlab python drivers:
  `pip install touchlab-comm-py`

- [touchlab_msgs](https://github.com/touchlab-avatarx/touchlab_msgs.git):
  Add this package to your workspace as a [source checkout using vcs](https://docs.ros.org/en/rolling/Installation/Maintaining-a-Source-Checkout.html#download-the-new-source-code).

## Usage

Simple usage:
```
ros2 launch touchlab_driver_ros touchlab_driver.launch.py
```
This will only publish raw sensor data at `/touchlab_driver/raw`.

With a calibration file:
```
ros2 launch touchlab_driver_ros touchlab_driver.launch.py calibration:=<PATH_TO_FILE>
```
This will only publish raw sensor data on `/touchlab_driver/raw` and calibrated data on `/touchlab_driver/calibrated`.
