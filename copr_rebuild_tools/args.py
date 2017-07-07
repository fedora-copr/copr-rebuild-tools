import argparse


parser = argparse.ArgumentParser(prog="copr-rebuild")
parser.add_argument("--debug", action="store_true", help="Enable debug output")
parser.add_argument("-c", "--config", help="Path to a configuration file")
parser.add_argument("backend")
subparsers = parser.add_subparsers(title="actions")


parser_base = argparse.ArgumentParser(add_help=False)
parser_base.add_argument("--previous", help="")
parser_base.add_argument("--limit", type=int, help="")
parser_base.add_argument("--new-packages", action="store_true", help="")
parser_base.add_argument("--new-versions", action="store_true", help="")


parser_submit = subparsers.add_parser("submit", parents=[parser_base], help="")
parser_submit.set_defaults(func="action_submit")

parser_print = subparsers.add_parser("print", parents=[parser_base], help="")
parser_print.set_defaults(func="action_print")


parser_successful = subparsers.add_parser("successful", help="")
parser_successful.set_defaults(func="action_successful")

parser_stats = subparsers.add_parser("stats", help="")
parser_stats.set_defaults(func="action_stats")
