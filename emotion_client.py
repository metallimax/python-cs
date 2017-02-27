from project_oxford import ProjectOxfordApi


class EmotionClient(ProjectOxfordApi):
    """
    Emotion Client
    """

    def __init__(self, key):
        super(self.__class__, self).__init__(key=key)
        endpoint = "/emotion/v1.0"
        self.endpoint = "%s/%s" % (self.base_url, endpoint,)
        self.key = key

    # TODO emotion_recognition
    # TODO emotion_recognition_in_video
    # TODO emotion_recognition_with_face_rectangles
    # TODO get_recognition_in_video_operation_result
