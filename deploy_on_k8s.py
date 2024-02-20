import os
import subprocess

def deploy_yaml_files(yaml_dir):
    for filename in os.listdir(yaml_dir):
        if filename.endswith(".yaml"):
            filepath = os.path.join(yaml_dir, filename)
            result = subprocess.run(["kubectl", "apply", "-f", filepath], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error: Failed to deploy {filename}")
                print(result.stderr)
                return
            print(f"Deployed {filename} successfully.")

yaml_dir = "."

if not os.path.isdir(yaml_dir):
    print(f"Error: Directory {yaml_dir} does not exist.")
    exit(1)

deploy_yaml_files(yaml_dir)
