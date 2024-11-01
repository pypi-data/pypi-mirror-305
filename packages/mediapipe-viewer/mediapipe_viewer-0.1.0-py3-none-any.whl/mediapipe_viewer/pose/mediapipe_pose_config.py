from pydantic import BaseModel


# 视频配置
class MediapipePoseVideoConfig(BaseModel):
    model_path: str | None = None
    video_path: str | None = None
    video_data_path: str | None = None


# 姿态配置
class MediapipePoseConfig(BaseModel):
    video1: MediapipePoseVideoConfig | None = None
    video2: MediapipePoseVideoConfig | None = None
