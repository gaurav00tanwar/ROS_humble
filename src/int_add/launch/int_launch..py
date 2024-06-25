from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    pub_node = Node(
        package = "int_add",
        executable = "pub_add",
    )

    sub_node = Node(
        package = "int_add",
        executable = "sub_add",
    )
    
    ld.add_action(pub_node)
    ld.add_action(sub_node)
    return ld