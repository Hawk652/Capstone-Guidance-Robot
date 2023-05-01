import asyncio
import websockets
import json
import sys

import time

from action_msgs.msg import GoalStatus
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose, PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from lifecycle_msgs.srv import GetState
from nav2_msgs.action import NavigateToPose

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSProfile
from rclpy.duration import Duration

from .robot_navigator import BasicNavigator

navigator = None;

async def handle_cmd(cmd, pub):
        cmd_json = json.loads(cmd);
        print(cmd_json);
        if(cmd_json["intent"]["name"] == "Turn"):
                if(cmd_json["entities"][0]["value"] == "left"):
                        vel = Twist();

                        vel.linear.x = 0.0;
                        vel.linear.y = 0.0;
                        vel.linear.z = 0.0;

                        vel.angular.x = 0.0;
                        vel.angular.y = 0.0;
                        # quarter speed
                        vel.angular.z = 0.455;

                        pub.publish(vel);
                        # Seconds for 90 degrees
                        # await asyncio.sleep(0.863076923);
                        # vel.angular.z = 0.0;
                        # pub.publish(vel);

                elif(cmd_json["entities"][0]["value"] == "right"):

                        vel = Twist();

                        vel.linear.x = 0.0;
                        vel.linear.y = 0.0;
                        vel.linear.z = 0.0;

                        vel.angular.x = 0.0;
                        vel.angular.y = 0.0;
                        # quarter speed
                        vel.angular.z = -0.455;

                        pub.publish(vel);
                        # Seconds for 90 degrees
                        # await asyncio.sleep(0.863076923);
                        # vel.angular.z = 0.0;
                        # pub.publish(vel);
        elif(cmd_json["intent"]["name"] == "Navigate"):

                # cancel previous navigation
                if(not navigator.isNavComplete()): navigator.cancelNav();

                # hardcoded poses are NOT a good way to do this, but this is just a proof of concept at this point
                if(cmd_json["entities"][0]["value"] == "room 119"):

                        goal_pose = PoseStamped();
                        goal_pose.header.frame_id = 'map';
                        goal_pose.header.stamp = navigator.get_clock().now().to_msg();
                        goal_pose.pose.position.x = 3.2576;
                        goal_pose.pose.position.y = 8.9377;
                        goal_pose.pose.orientation.z = 0.7696;
                        goal_pose.pose.orientation.w = 0.6385;
                        navigator.goToPose(goal_pose);

                elif(cmd_json["entities"][0]["value"] == "elevator"):

                        goal_pose = PoseStamped();
                        goal_pose.header.frame_id = 'map';
                        goal_pose.header.stamp = navigator.get_clock().now().to_msg();
                        goal_pose.pose.position.x = 7.9511;
                        goal_pose.pose.position.y = -26.739;
                        goal_pose.pose.orientation.z = 0.72253;
                        goal_pose.pose.orientation.w = 0.69133;
                        navigator.goToPose(goal_pose);

                elif(cmd_json["entities"][0]["value"] == "home"):
                        goal_pose = PoseStamped();
                        goal_pose.header.frame_id = 'map';
                        goal_pose.header.stamp = navigator.get_clock().now().to_msg();

                        goal_pose.pose.position.x = -1.0494;
                        goal_pose.pose.position.y = -0.00783;
                        goal_pose.pose.orientation.z = 0.09284;
                        goal_pose.pose.orientation.w = 0.99568;

                        navigator.goToPose(goal_pose);

        elif(cmd_json["intent"]["name"] == "MoveForward"):
                vel = Twist();

                vel.linear.x = 0.26;
                vel.linear.y = 0.0;
                vel.linear.z = 0.0;

                vel.angular.x = 0.0;
                vel.angular.y = 0.0;
                vel.angular.z = 0.0;

                pub.publish(vel);

        elif(cmd_json["intent"]["name"] == "Stop"):
                vel = Twist();

                vel.linear.x = 0.0;
                vel.linear.y = 0.0;
                vel.linear.z = 0.0;

                vel.angular.x = 0.0;
                vel.angular.y = 0.0;
                vel.angular.z = 0.0;

                pub.publish(vel);
        elif(cmd_json["intent"]["name"] == "March"):
                pass;

async def handle_websocket(pub):
        async with websockets.connect("ws://localhost:12101/api/events/intent") as websocket:
                print("Websocket up");
                while True:
                        cmd = await websocket.recv();
                        asyncio.create_task(handle_cmd(cmd, pub));


def main(args=None):
        global navigator;
        if args is None:
                args = sys.argv;

        rclpy.init(args=args);

        # navigator = BasicNavigator()

        # set initial pose
        # initial_pose = Pose();
        # initial_pose.position.x = -1.0494;
        # initial_pose.position.y = -0.00783;
        # initial_pose.orientation.z = 0.09284;
        # initial_pose.orientation.w = 0.99568;
        # navigator.setInitialPose(initial_pose);

        # wait until navigation is up
        # navigator.waitUntilNav2Active();

        zoomzoom = rclpy.create_node('zoomzoom');
        pub = zoomzoom.create_publisher(Twist, 'cmd_vel', 10);
        print("Publisher up!");
        asyncio.run(handle_websocket(pub));