import argparse
import os

from face_client import FaceClient

if __name__ == '__main__':
    face_client = FaceClient(key=os.environ['CS_FACE_API_KEY'])

    class ActionAction(argparse.Action):
        def __init__(self, option_strings, dest, nargs=None, **kw):
            if nargs is not None:
                raise ValueError("nargs not allowed")
            super(ActionAction, self).__init__(option_strings, dest, **kw)

        def __call__(self, parser, namespace, values, option_string=None):
            if parser.prog.split()[-1] == 'face':
                pass
            setattr(namespace, 'func', getattr(face_client, values))


    argparser = argparse.ArgumentParser(description="CNTK example")
    subparsers = argparser.add_subparsers(help='sub-command help')

    # ---------- EMOTION -----------------------------------------------------------------------------------------------
    parser_emotion = subparsers.add_parser('emotion', help='Emotion client')

    # ---------- COMPUTER VISION ---------------------------------------------------------------------------------------
    parser_emotion = subparsers.add_parser('cv', help='Computer vision client')

    # ---------- FACE --------------------------------------------------------------------------------------------------
    parser_face = subparsers.add_parser('face', help='Face client')
    # parser_face_list_group = parser_face.add_mutually_exclusive_group(required=True)
    parser_face.add_argument('-x', '--action', choices=['detect', 'list_face_lists'], action=ActionAction,
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
