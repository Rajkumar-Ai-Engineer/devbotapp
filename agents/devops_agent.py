from tools import docker_tools
from langchain.agents import Tool,initialize_agent
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os 
load_dotenv()

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

llm = ChatGroq(
    model=os.getenv("model_id")
)

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}"),
])

chain = LLMChain(llm=llm,prompt=template)

tools = [
    Tool(
        name="RunDockerContainer",
        func=lambda x:docker_tools.run_container(name=x),
        description="Use this tool to run a docker container. Input should be the name of the container."
    ),
    Tool(
        name="StopDockerContainer",
        func=lambda x:docker_tools.stop_container(name=x),
        description = "Use this tool to Stop the docker container. Input should be the name of the container."
    ),
    Tool(
        name="ListDockerContainers",
        func=lambda x:docker_tools.list_containers(),
        description = "Use this tool to list all the docker containers."
    ),
    Tool(
        name="LogsDockerContainer",
        func=lambda x:docker_tools.logs_container(name=x),
        description = "Use this tool to get the logs of the docker container. Input should be the name of the container."
    ),
]

agent = initialize_agent(
    tools,
    chain,
    agent="chat-zero-shot-react-description",
    verbose=True
)


