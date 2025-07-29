from agents.devops_agent import agent

def handle_user_input(user_input:str):
    return agent.invoke(input={"input":user_input})

