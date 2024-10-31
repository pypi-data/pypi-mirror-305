import pprint
import time

from slurmpilot.config import Config


class SlurmSchedulerCallbackInterface:
    def on_job_scheduled_start(self, cluster: str, jobname: str):
        raise NotImplementedError()

    def on_established_connection(self, cluster: str):
        raise NotImplementedError()

    def on_sending_artifact(self, localpath: str, remotepath: str, cluster: str):
        raise NotImplementedError()

    def on_job_submitted_to_slurm(self, jobid: int, jobname: str):
        raise NotImplementedError()


class SlurmSchedulerCallback(SlurmSchedulerCallbackInterface):
    def __init__(self):
        self.format_cluster = "1;30;34"
        self.format_highlight = "1;30;34"
        self.format_jobname = "1;31;38"

    def format(self, s, format_pattern=None):
        if not format_pattern:
            format_pattern = self.format_cluster
        return f"\x1b[{format_pattern}m{s}\x1b[0m"

    def format_string_jobname(self, message: str, jobname: str) -> str:
        return f"{message} {self.format(jobname, self.format_jobname)}."

    def on_job_scheduled_start(self, cluster: str, jobname: str):
        print(
            f"Starting job {self.format(jobname, self.format_jobname)} on {self.format(cluster, self.format_cluster)}."
        )

    def on_establishing_connection(self, cluster: str):
        print(
            f"Establishing ssh connection with {self.format(cluster, self.format_cluster)}"
        )

    def on_sending_artifact(self, localpath: str, remotepath: str, cluster: str):
        print(f"Sending job data from {localpath} to {cluster}:{remotepath}")

    def on_job_submitted_to_slurm(self, jobid: int, jobname: str):
        print(
            f"Job submitted to Slurm with the following id {self.format(jobid, self.format_jobname)} saving the jobid locally."
        )

    def on_suggest_command_before_wait_completion(self, jobname: str):
        commands = [
            (
                "show the log of your job",
                f"slurmpilot --log {jobname}",
            ),
            (
                "sync the artifact of your job",
                f"slurmpilot --sync {jobname}",
            ),
            (
                "show the status of your job",
                f"slurmpilot --status {jobname}",
            ),
            (
                "stop your job",
                f"slurmpilot --stop {jobname}",
            ),
        ]
        commands_strings = []
        for description, command in commands:
            commands_strings.append(
                f"* {description}: "
                + self.format(f"`{command}`", self.format_highlight)
            )
        cmds = "\n".join(commands_strings)
        print(f"You can use the following commands in a terminal:\n" + cmds)

    def on_waiting_completion(self, jobname: str, status: str, n_seconds_wait: int):
        # TODO dependency inversion to support rich
        print(
            f"{self.format(jobname, self.format_jobname)} status {self.format(status, self.format_highlight)}, waiting {n_seconds_wait}s"
        )

    def on_config_loaded(self, config: Config):
        print(f"Cluster configurations loaded:")
        for cluster, cluster_config in config.cluster_configs.items():
            print(f"{self.format(cluster, self.format_cluster)}: {cluster_config}")


if __name__ == "__main__":

    def print_format_table():
        """
        prints table of formatted text format options
        """
        for style in range(8):
            for fg in range(30, 38):
                s1 = ""
                for bg in range(30, 48):
                    format = ";".join([str(style), str(fg), str(bg)])
                    s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
                print(s1)
            print("\n")

    print_format_table()

    print("\x1b[0;31;40m" + "Success!" + "\x1b[0m" + "yop")

    cb = SlurmSchedulerCallback()
    cluster = "bigcluster"
    jobname = "smalljob"
    cb.on_job_scheduled_start(cluster=cluster, jobname=jobname)
    cb.on_establishing_connection(cluster=cluster)
    cb.on_sending_artifact(cluster=cluster, localpath="foo/", remotepath="foo2/")
    cb.on_job_submitted_to_slurm(jobname=jobname, jobid=12)
    cb.on_suggest_command_before_wait_completion(jobname=jobname)
    # cb.on_config_loaded()
    for _ in range(4):
        cb.on_waiting_completion(jobname=jobname, status="PENDING", n_seconds_wait=1)
        time.sleep(0.2)
