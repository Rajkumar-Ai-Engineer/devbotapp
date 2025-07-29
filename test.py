import os

paths = ["./.env", "./.gitignore", "./phi.yml", "./main.py", "./README.md", "./requirements.txt", 
         "./agents/devops_agent.py", "./chains/command_chain.py", "./tools/docker_tools.py", "./terminal/devbotops_app.py"]

for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(os.path.dirname(path))
    if not os.path.exists(path):
        open(path, 'a').close()

print("Execution finished...")
