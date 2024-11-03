import subprocess


def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error occurred in {script_name}:")
        print(result.stderr)
        exit(result.returncode)


run_script("generate_csv.py")
run_script("categorise_data.py")
run_script("convert_to_lowercase.py")
run_script("generate_corrections.py")

print("Pipeline completed successfully.")