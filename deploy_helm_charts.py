import subprocess

def helm_deploy(chart_path, release_name):
    # Check if release already exists
    check_cmd = ["helm", "get", "manifest", release_name]
    result = subprocess.run(check_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        # Release exists, perform upgrade
        print(f"Release '{release_name}' already exists. Upgrading...")
        upgrade_cmd = ["helm", "upgrade", release_name, chart_path]
        subprocess.run(upgrade_cmd, check=True)
        print(f"Release '{release_name}' upgraded successfully.")
    else:
        # Release does not exist, perform install
        print(f"Release '{release_name}' does not exist. Installing...")
        install_cmd = ["helm", "install", release_name, chart_path]
        subprocess.run(install_cmd, check=True)
        print(f"Release '{release_name}' installed successfully.")


chart_paths = ["./service1-chart", "./service2-chart"] 
release_names = ["service1-chart", "service2-chart"]  
for chart_path, release_name in zip(chart_paths, release_names):
    helm_deploy(chart_path, release_name)
