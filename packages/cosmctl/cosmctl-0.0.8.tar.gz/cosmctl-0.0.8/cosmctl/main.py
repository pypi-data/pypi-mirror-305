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
        return

    if command == "build":
        command_instance = BuildCommand(environment, versionTag, verboseFlag)
    elif command == "run":
        command_instance = RunCommand(environment, None, verboseFlag)
    elif command == "build-run":
        command_instance = BuildRunCommand(environment, versionTag, verboseFlag)
    elif command == "stop":
        command_instance = StopCommand(None, None, verboseFlag)
    else:
        print("Invalid command. Type cosmctl --help to see commands")
        return

    command_instance.execute()


if __name__ == "__main__":
    main()
