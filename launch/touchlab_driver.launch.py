#!/usr/bin/env python3

# Copyright (c) 2025 Touchlab Limited. All Rights Reserved
# Unauthorized copying or modifications of this file, via any medium is strictly prohibited.

from launch import LaunchDescription
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def launch_setup(context, *args, **kwargs):
  port = LaunchConfiguration('port', default='/dev/touchlab')
  calibration = LaunchConfiguration('calibration', default='')
  timeout = LaunchConfiguration('timeout', default=500)

  driver_node = Node(
        package='touchlab_driver_ros',
        executable='touchlab_driver',
        parameters=[
            {"port": port,
            "calibration": calibration,
            "timeout": timeout,}
        ],
        output='screen',
    )

  return [ driver_node,]

def generate_launch_description():
    return LaunchDescription([
        OpaqueFunction(function=launch_setup)
    ])
