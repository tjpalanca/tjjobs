import subprocess


def main():
    try:
        workspace = "tjjobs/workspace.yaml"
        daemon = subprocess.Popen(["dagster-daemon", "run", "-w", workspace])
        subprocess.run(["dagit", "-w", workspace])
    finally:
        daemon.kill()


if __name__ == "__main__":
    main()
