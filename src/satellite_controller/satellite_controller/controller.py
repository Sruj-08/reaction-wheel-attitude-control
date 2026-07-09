import rclpy
from rclpy.node import Node

class SatelliteController(Node):
    def __init__(self):
        super().__init__('satellite_controller')
        self.get_logger().info("Satellite Controller Started!")

def main(args=None):
    rclpy.init(args=args)

    node = SatelliteController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
