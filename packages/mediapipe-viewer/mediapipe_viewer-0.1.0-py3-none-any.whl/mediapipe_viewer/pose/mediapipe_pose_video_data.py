from .mediapipe_pose_video import MediapipePoseVideo
from .mediapipe_pose_video import VideoData
from .mediapipe_pose_video import VideoFrame
from .mediapipe_pose_video import VideoProp


# 视频数据
class MediapipePoseVideoData(MediapipePoseVideo):

    def __init__(self, video_data_path: str, angles: list):
        self.video_data_path = video_data_path
        self.angles = angles

        with open(video_data_path, "r") as file:
            content = file.read()
            self.video_data = VideoData.model_validate_json(content)
            self.video_prop = self.video_data.video_prop
            self.video_frames = self.video_data.video_frames

            # 帧数据
            self.index = 0
            self.video_frame = None
            self.video_frame_image = None

    def read(self) -> bool:
        if self.index < len(self.video_frames):
            self.video_frame = self.video_frames[self.index]
            self.index += 1
            return True

        return False

    def get_angles(self) -> list:
        return self.angles

    def get_video_prop(self) -> VideoProp:
        return self.video_prop

    def get_video_frame(self) -> VideoFrame:
        return self.video_frame

    def get_video_frame_image(self):
        return self.video_frame_image
