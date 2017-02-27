import argparse
import os

from computer_vision_client import ComputerVisionClient
from emotion_client import EmotionClient
from face_client import FaceClient

if __name__ == '__main__':
    face_client = FaceClient(key=os.environ['CS_FACE_API_KEY'])
    emotion_client = EmotionClient(key=os.environ['CS_EMOTION_API_KEY'])
    computer_vision_client = ComputerVisionClient(key=os.environ['CS_COMPUTER_VISION_API_KEY'])


    class ActionAction(argparse.Action):
        def __init__(self, option_strings, dest, nargs=None, **kw):
            if nargs is not None:
                raise ValueError("nargs not allowed")
            super(ActionAction, self).__init__(option_strings, dest, **kw)

        def __call__(self, parser, namespace, values, option_string=None):
            if parser.prog.split()[-1] == 'face':
                pass
            setattr(namespace, 'func', getattr(face_client, values))


    argparser = argparse.ArgumentParser(description="Project Oxford Cognitive Services")
    subparsers = argparser.add_subparsers(help='sub-command help')

    # ---------- EMOTION -----------------------------------------------------------------------------------------------
    parser_emotion = subparsers.add_parser('emotion', help='Emotion client')
    parser_emotion.add_argument('-x', '--action', choices=['recognize', 'recognizeinvideo', 'operations', ],
                                action=ActionAction, help="Action")

    # ---------- COMPUTER VISION ---------------------------------------------------------------------------------------
    parser_cv = subparsers.add_parser('cv', help='Computer vision client')
    parser_cv.add_argument('-x', '--action', choices=['analyze', ], action=ActionAction,
                           help="Action")

    # ---------- FACE --------------------------------------------------------------------------------------------------
    parser_face = subparsers.add_parser('face', help='Face client')
    parser_face.add_argument('-x', '--action', choices=['detect', 'list_face_lists', ], action=ActionAction,
                             help="Action")
    parser_face.add_argument('-i', '--image_url', help="Image URL")
    parser_face.add_argument('-l', '--face_list_id', help="Face list ID")

    args, unknown = argparser.parse_known_args()
    kwargs = vars(args)
    try:
        if args.func is not None:
            json_result = args.func(**kwargs)
            print json_result
    except Exception, e:
        args.output.write(e.message)
