from project_oxford import ProjectOxfordApi


class ComputerVisionClient(ProjectOxfordApi):
    """
    Computer Vision Client
    """

    def __init__(self, key):
        super(self.__class__, self).__init__(key=key)
        endpoint = "/vision/v1.0"
        self.endpoint = "%s/%s" % (self.base_url, endpoint,)
        self.key = key

    # TODO analyze_image
    # TODO describe_image
    # TODO get_thumbnail
    # TODO list_domain_specific_models
    # TODO ocr
    # TODO recognize_domain_specific_content
    # TODO tag_image
