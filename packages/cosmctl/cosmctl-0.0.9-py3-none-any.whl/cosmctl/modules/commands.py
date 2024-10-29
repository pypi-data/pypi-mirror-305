import subprocess
import time
from cosmctl.utils.loader import Loader


class Command:
    """Base command class to define a common interface for all commands."""
    def __init__(self, env=None, versionTag=None, verboseFlag=False):
        print("Downloading scripts...")
        self.temp_dir = Loader().download_directory("Crossroads")
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
            "--label", f"version={self.versionTag}",
            "--tag", f"{self.naming["project_name"]}/{self.naming["base_name"]}:{self.versionTag}",
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

        project_var = self.naming["project_name"]
        base_name_var = self.naming["base_name"]
        opts_var = self.naming["opts"]
        date_time = int(time.time())
        
        docker_run_cmd = [
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
        print("     ".join(docker_run_cmd))
        res = subprocess.run(docker_run_cmd, text=True, check=True)
        print(res.stdout)

        # if self.verboseFlag:
        #     print(f"Run with environment '{self.env}'")



class BuildRunCommand(Command):
    def execute(self):
        print("Building and running container...")
        BuildCommand(self.env, self.versionTag, self.verboseFlag).execute()
        RunCommand(self.env, None, self.verboseFlag).execute()

        # if self.verboseFlag:
        #     print(
        #         f"Build-Run with environment '{self.env}' and version: '{self.versionTag}'"
        #     )


class StopCommand(Command):
    def execute(self):
        print("Stopping containers...")

        project_var = self.naming["project_name"]
        base_name_var = self.naming["base_name"]
        docker_container_hash_cmd = [
            "docker", "ps", "-a", "-q",
            "--filter", f"label=project={project_var}",
            "--filter", f"label=prefix={self.env}",
            "--filter", f"name={project_var}-{self.env}-{base_name_var}"
        ]
        res = subprocess.run(docker_container_hash_cmd, stdout=subprocess.PIPE, text=True, check=True)
        containers_hash = res.stdout.strip().replace("\n", " ")
        if not containers_hash:
            print("No running containers found \nnothing to stop and kill")
            return        
        print(f"Containers to delete: {containers_hash}")

        # stop
        docker_stop_cmd = [
            "docker", "stop", containers_hash,
        ]
        res = subprocess.run(docker_stop_cmd, text=True, check=True)
        print(res.stdout)

        # remove
        docker_rm_cmd = [
            "docker", "rm", containers_hash,
        ]
        res = subprocess.run(docker_rm_cmd, text=True, check=True)
        print(res.stdout)

        # if self.verboseFlag:
        #     print("Verbose stop output")
