import docker 

client = docker.from_env()

def run_container(image="nginx",name="my_nginx",port={"80/tcp":8080},volumes=None):
    
    return client.containers.run(image=image,
                                      name=name,
                                      ports=port,
                                      volumes=volumes,
                                      detach=True)
    
def stop_container(name):
    container = client.containers.get(name)
    container.stop()
    
def list_containers():
    return [container.name for container in client.containers.list(all=True)]
    
def get_logs(name):
    container = client.containers.get(name)
    return container.logs().decode("utf-8")