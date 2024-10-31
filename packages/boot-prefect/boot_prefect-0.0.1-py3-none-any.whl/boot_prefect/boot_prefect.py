import subprocess
import time

import click

@click.command()
@click.option("--profile", default="local", help="The Prefect profile to use.")
@click.option("--work_pool", default="local", help="The Prefect work pool to use.")
def main(
        profile: str | None = "local",
        work_pool: str | None = "local"
    ) -> None:
    """
    Starts the Prefect server and worker for the given profile and pool_name.

    Args:
        profile (str, optional): The Prefect profile to use. Defaults to "local".
        work_pool (str, optional): The Prefect work pool to use. Defaults to "local".
    """

    # Start the Prefect server and, optionally, worker
    with start_server():
        # Set profile
        if profile:
            use_profile(profile)

        if work_pool:
            with start_work_pool(work_pool):
                print("Prefect server and work pool running. Press Ctrl+C to terminate.")

                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("Terminating Prefect server and worker...")
        else:
            print("Prefect server running. Press Ctrl+C to terminate.")

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("Terminating Prefect server...")


def use_profile(profile: str) -> None:
    """
    Issues the Prefect CLI command to set the profile.

    Args:
        profile (str): The name of the Prefect profile to set.
    """

    print(f"Setting Prefect profile to {profile}...")

    result = subprocess.run(
        args = ["prefect", "profile", "use", profile],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if "Error connecting to Prefect API URL" in result.stdout:
        raise Exception(f"Error setting Prefect profile to {profile}.")

    print(f"Prefect profile set to {profile}.")


def start_server() -> subprocess.Popen:
    """
    Issues the Prefect CLI command to start the server.
    
    Returns:
        subprocess.Popen: The server process
    """

    print("Starting Prefect server...")

    server_process = subprocess.Popen(
        args=["prefect", "server", "start"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    for line in server_process.stdout:
        if "Check out the dashboard at" in line:
            print("Prefect server started successfully.")
            break

    return server_process


def start_work_pool(work_pool: str) -> subprocess.Popen:
    """
    Issues the Prefect CLI command to start the worker.
    
    Args:
        work_pool (str): The name of the Prefect work pool to start.

    Returns:
        subprocess.Popen: The worker process
    """

    print(f"Starting Prefect work pool {work_pool}...")

    work_pool_process = subprocess.Popen(
        args=["prefect", "worker", "start", "--pool", work_pool],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    for line in work_pool_process.stdout:
        if "started!" in line:
            print("Prefect work pool started successfully.")
            break

    return work_pool_process


if __name__ == "__main__":
    main()
