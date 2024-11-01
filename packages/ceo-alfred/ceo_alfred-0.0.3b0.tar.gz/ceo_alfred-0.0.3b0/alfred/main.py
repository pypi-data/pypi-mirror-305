import sys

from process_manager.agent import process_manager
from alfred.action import find_information_about_the_assistant

process_manager.grant_ability(find_information_about_the_assistant)


def main():
    if len(sys.argv) > 1:
        process_manager.assign(sys.argv[1])
    try:
        process_manager.just_do_it()
    except KeyboardInterrupt:
        pass
    exit(0)


if __name__ == "__main__":
    main()
