import os
import sys
import argparse
import shutil

from alo.__version__ import __version__


def __run(args):
    from alo.alo import Alo
    from alo.model import settings, Git
    if args.name:
        settings.name = args.name
    if args.config:
        settings.config = args.config
    if args.system:
        settings.system = args.system
    if args.computing:
        settings.computing = args.computing
    settings.mode = None if args.mode == 'all' else args.mode
    if args.loop:
        settings.computing = 'daemon'
    if getattr(args, "git.url"):
        settings.git = Git(url=getattr(args, 'git.url'),
                           branch=getattr(args, 'git.branch') if getattr(args, 'git.branch') else 'main')
    alo = Alo()
    alo.reload()
    alo.run()


def __template(args):
    src = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'template')
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(os.getcwd(), item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    print("A Titanic template file has been created in the current path.")
    print("Run alo : $ alo")


def __history(args):
    from alo.alo import Alo
    from alo.model import settings
    if args.config:
        settings.config = args.config
    alo = Alo()
    alo.history(type=args.mode, show_table=True, head=args.head, tail=args.tail)


def __register(args):
    from alo.solution_register import SolutionRegister
    solution_register = SolutionRegister(args.id, args.password)
    solution_register.register()


def __update(args):
    from alo.solution_register import SolutionRegister
    solution_register = SolutionRegister(args.id, args.password)
    solution_register.update()


def __delete(args):
    from alo.solution_register import SolutionRegister
    solution_register = SolutionRegister(args.id, args.password)
    solution_register.delete(args.name)


def main():
    if len(sys.argv) > 1:
        if sys.argv[-1] in ['-v', '--version']:
            print(__version__)
            return
        if sys.argv[1] in ['-h', '--help']:
            pass
        elif sys.argv[1] not in ['run', 'history', 'register', 'update', 'delete', 'template']:  # v1 호환
            sys.argv.insert(1, 'run')
    else:
        sys.argv.insert(1, 'run')

    parser = argparse.ArgumentParser('alo', description='ALO(AI Learning Organizer)')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    subparsers = parser.add_subparsers(dest='command')

    cmd_exec = subparsers.add_parser('run', description='Run alo')
    cmd_exec.add_argument('--name', type=str, help='name of solution')
    cmd_exec.add_argument('--mode', type=str, default='all', choices=['train', 'inference', 'all'], help='ALO mode: train, inference, all')
    cmd_exec.add_argument("--loop", dest='loop', action='store_true', help="On/off infinite loop: True, False")
    cmd_exec.add_argument("--computing", type=str, default="local", choices=['local', 'daemon'], help="training resource: local, ...")
    cmd_exec.add_argument('--config', type=str, help='path of experimental_plan.yaml')
    cmd_exec.add_argument('--system', type=str, help='path of solution_metadata.yaml')
    cmd_exec.add_argument('--git.url', type=str, help='url of git repository')
    cmd_exec.add_argument('--git.branch', type=str, help='branch name of git repository')
    cmd_exec.add_argument('--log_level', type=str, default="DEBUG", choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR'], help='log level')

    cmd_history = subparsers.add_parser('history', description='Run history')
    cmd_history.add_argument('--config', type=str, help='path of experimental_plan.yaml')
    cmd_history.add_argument('--mode', default=['train', 'inference'], choices=['train', 'inference'], nargs='+', help='train, inference')
    cmd_history.add_argument("--head", type=int, default=None, help="output the last part of history")
    cmd_history.add_argument("--tail", type=int, default=None, help="output the first part of history")

    cmd_template = subparsers.add_parser('template', description='Create titanic template')

    cmd_register = subparsers.add_parser('register', description='Create new solution')
    cmd_register.add_argument('--id', required=True, help='user id of AI conductor')
    cmd_register.add_argument('--password', required=True, help='user password of AI conductor')
    cmd_register.add_argument('--description', default=None, help='description')

    cmd_update = subparsers.add_parser('update', description='Update a solution')
    cmd_update.add_argument('--id', required=True, help='user id of AI conductor')
    cmd_update.add_argument('--password', required=True, help='user password of AI conductor')

    cmd_delete = subparsers.add_parser('delete', description='Delete a solution')
    cmd_delete.add_argument('--name', required=True, help='name of stream')
    cmd_delete.add_argument('--id', required=True, help='user id of AI conductor')
    cmd_delete.add_argument('--password', required=True, help='user password of AI conductor')

    args = parser.parse_args()

    commands = {'run': __run,
                'template': __template,
                'history': __history,
                'register': __register,
                'update': __update,
                'delete': __delete,
                }
    commands[args.command](args)
