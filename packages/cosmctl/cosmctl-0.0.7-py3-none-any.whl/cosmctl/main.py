from cosmctl.modules.argsparser import checkEnv, defineArgs, getParsedArgs
from cosmctl.modules.commands import *


def main():
    args = defineArgs()
    environment, verboseFlag, versionTag, command = getParsedArgs(args)

    print(environment, verboseFlag, versionTag, command)

    if not checkEnv(environment):
        print(
            "Invalid environment argument. Type cosmctl --help to see argument description"
        )

    command_map = {
        "build": BuildCommand(environment, versionTag, verboseFlag),
        "run": RunCommand(environment, None, verboseFlag),
        "build-run": BuildRunCommand(environment, versionTag, verboseFlag),
        "stop": StopCommand(None, None, verboseFlag),
    }

    if command in command_map:
        command_map[command].execute()
    else:
        print("Invalid command. Type cosmctl --help to see commands")


if __name__ == "__main__":
    main()
