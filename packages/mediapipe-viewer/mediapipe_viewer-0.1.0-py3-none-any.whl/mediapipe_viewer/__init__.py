import getopt
import sys

from mediapipe_viewer.config import read_config
from mediapipe_viewer.pose import main as pose_main


# 全局入口
def main() -> int:
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hc:",
            ["help", "config="])

    except getopt.GetoptError:
        print("usage: mediapipe-viewer -h")
        sys.exit(2)

    config_filename = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("mediapipe-viewer -c <config-filename>")
            sys.exit()
        elif opt in ("-c", "--config"):
            config_filename = arg

    config_object = read_config(config_filename)
    if config_object.pose is not None:
        pose_main(config_object.pose)

    return 0


# 测试
if __name__ == '__main__':
    print("Testing...")
    main()
