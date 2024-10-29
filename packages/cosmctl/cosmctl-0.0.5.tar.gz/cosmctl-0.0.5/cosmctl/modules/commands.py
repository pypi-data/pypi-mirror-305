import subprocess
from datetime import datetime
from utils.Parser import Loader


class Command:
    """Base command class to define a common interface for all commands."""
    def __init__(self, env=None, versionTag=None, verboseFlag=False):
        print("Downloading scripts...")
        self.temp_dir = Loader().download_directory()
        print("Scripts load success")
        self.env = env
        self.versionTag = versionTag
        self.verboseFlag = verboseFlag
        self.naming = Loader().parse_naming(f"{self.temp_dir}/naming.json")


    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class BuildCommand(Command):
    def execute(self):
        
        print("Building container...")
        if self.env == "local":
            suffix = ".local"
        docker_build_cmd = [
            "docker", "build",
            "--label", f"project={self.naming["project_name"]}",
            "--label", f"version={self.version}",
            "--tag", f"{self.naming["project_name"]}/{self.naming["base_name"]}:{self.version}",
            "--file", f"{self.temp_dir}/Dockerfile{suffix}",
            "."
        ]
        res = subprocess.run(docker_build_cmd, check=True)
        print(res.stdout())

        # if self.verboseFlag:
        #     print(
        #         f"Build with environment '{self.env}' and version '{self.versionTag}'"
        #     )


class RunCommand(Command):
    def execute(self):
        print("Running containers...")
        # TODO run logic
        if self.verboseFlag:
            print(f"Run with environment '{self.env}'")

        project_var = self.naming["project_name"]
        base_name_var = self.naming["base_name"]
        opts_var = self.naming["opts"]
        date_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        
        subprocess.run(
            [
                "docker", "run", "-d",
                "--network", "main_bridge",
                f"--name={project_var}-{self.env}-{base_name_var}-{date_time}",
                "--label", f"project={project_var}",
                "--label", f"version={self.versionTag}",
                "--label", f"prefix={self.env}",
                "--env", f"PREFIX={self.env}",
                f"--hostname={project_var}-{self.env}-{base_name_var}",
                f"{opts_var}",
                f"{project_var}/{base_name_var}:{self.versionTag}",
            ]
        )


class BuildRunCommand(Command):
    def execute(self):
        print("Building and running container...")
        # TODO build-run logic
        if self.verboseFlag:
            print(
                f"Build-Run with environment '{self.env}' and version: '{self.versionTag}'"
            )


class StopCommand(Command):
    def execute(self):
        print("Stopping containers...")
        # TODO stop logic
        if self.verboseFlag:
            print("Verbose stop output")
