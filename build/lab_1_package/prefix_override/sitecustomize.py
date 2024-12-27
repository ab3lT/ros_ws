import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abel/CODE/AAiT/AI/ros_ws/install/lab_1_package'
