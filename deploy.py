import argparse
import subprocess
import docker
from getpass import getpass

def main():
    parser = argparse.ArgumentParser(description="Deploy microservices with versions and parameters")
    parser.add_argument("--version_service1", help="Version of service 1")
    parser.add_argument("--version_service2", help="Version of service 2")
    parser.add_argument("--additional_param_1", type=int, help="Additional parameter for service 1")
    args = parser.parse_args()
  

        # Docker Hub credentials (store securely, preferably not in the script)
    username = input("Enter your Docker Hub username: ")
    password = getpass("Enter your Docker Hub password: ")

    # Login to Docker Hub
    client = docker.from_env()
    try:
        client.login(username=username, password=password)
    except docker.errors.AuthenticationError:
        print("Invalid credentials. Please try again.")
        exit(1)

    services = {
        "matealipovac/image1": {
            "version": args.version_service1,
            "additional_params": ["-p", f"{args.additional_param_1}"] if args.additional_param_1 else [],
        },
        "matealipovac/image2": {"version": args.version_service2},
    }

    for name, config in services.items():
        version = config["version"]
        image = f"{name}:{version}"
        if args.additional_param_1:
            params = ["docker", "run", "-d"] + config["additional_params"] + [image]
        else:
            params = ["docker", "run", "-d"] + [image]

        subprocess.run(params, check=True)

    print("Microservices deployed successfully!")

if __name__ == "__main__":
  main()
