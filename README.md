This is a ROS wrapper for the [Touchlab Driver for Python](https://touchlab-avatarx.github.io/touchlab_driver_py). We provide [ROS1](https://github.com/touchlab-avatarx/touchlab_driver_ros/tree/ros1) and [ROS2](https://github.com/touchlab-avatarx/touchlab_driver_ros) support. This driver is ideal for quickly starting to TOuchlab sensors in ROS.

## Dependencies:

- Touchlab python drivers via [rosdep](https://wiki.ros.org/rosdep).

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
