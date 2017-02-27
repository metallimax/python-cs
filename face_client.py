from project_oxford import ProjectOxfordApi


class FaceClient(ProjectOxfordApi):
    """
    Face Client
    """

    API = {
        'facelists': 'facelists',
        'detect': 'detect',
    }

    def __init__(self, key):
        super(self.__class__, self).__init__(key=key)
        endpoint = "/face/v1.0"
        self.endpoint = "%s/%s" % (self.base_url, endpoint,)
        self.key = key

    def list_face_lists(self, **kw):
        """
        .Net ListFaceListsAsync equivalent
        :return:
        """

        json = {
        }
        data = None
        params = None
        api_url = "%s/%s" % (self.endpoint, self.API['facelists'],)

        return self.request(method='get', endpoint=api_url, json=json, data=data, params=params)

    def detect(self, image_url, return_face_id=True, return_face_landmarks=True, return_face_attributes=None, **kw):
        """
        .Net DetectAsync equivalent
        :return:
        """

        if return_face_attributes is None:
            return_face_attributes = ['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', ]

        json = {'url': image_url}
        data = None
        params = {
            'returnFaceId': return_face_id,
            'returnFaceLandmarks': return_face_landmarks,
            'returnFaceAttributes': ','.join(return_face_attributes),
        }
        # json = {
        # }
        # data = None
        # params = None
        api_url = "%s/%s" % (self.endpoint, self.API['detect'],)

        return self.request(method='post', endpoint=api_url, json=json, data=data, params=params)

