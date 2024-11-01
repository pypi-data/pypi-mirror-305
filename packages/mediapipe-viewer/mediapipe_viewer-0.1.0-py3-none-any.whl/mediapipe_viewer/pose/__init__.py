from .mediapipe_pose import ANGLE_DEFINES
from .mediapipe_pose_config import MediapipePoseConfig
from .mediapipe_pose_config import MediapipePoseVideoConfig
from .mediapipe_pose_video import MediapipePoseVideo
from .mediapipe_pose_video_base import MediapipePoseVideoBase
from .mediapipe_pose_video_data import MediapipePoseVideoData
from .mediapipe_pose_video_viewer import show


# 入口
def main(pose: MediapipePoseConfig):
    if pose is not None:
        mv1 = get_mediapipe_pose_video(pose.video1)
        mv2 = get_mediapipe_pose_video(pose.video2)
        show(mv1, mv2)


def get_mediapipe_pose_video(video: MediapipePoseVideoConfig):
    if (video is not None
            and video.model_path is not None
            and video.video_path is not None):
        return MediapipePoseVideoBase(
            video.model_path,
            video.video_path,
            ANGLE_DEFINES)

    if (video is not None
            and video.video_data_path is not None):
        return MediapipePoseVideoData(
            video.video_data_path,
            ANGLE_DEFINES)

    return None
