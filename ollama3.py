
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os
import sys
os.environ["OPENAI_API_KEY"] = "sk-proj-bNKkiqAt6UZbYy6blzI0T3BlbkFJ5oQaLgwtGVojZ3Fxvb9x"
os.system("chcp 65001")

# Ensure the default encoding for stdout and stderr is UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
llm = ChatOpenAI(
    model = "crewai-llama3:8b",
    base_url = "http://localhost:11434/v1")

# general_agent = Agent(role = "Math Professor",
#                       goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
#                       backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
#                       allow_delegation = False,
#                       verbose = True,
#                       llm = llm)

# task = Task(description="""what is 3 + 5""",
#              agent = general_agent,
#              expected_output="A numerical answer.")

# crew = Crew(
#             agents=[general_agent],
#             tasks=[task],
#             verbose=2
#         )

# result = crew.kickoff()

# print(result)


# from crewai import Agent, Task, Crew, Process
# import os
# os.environ["OPENAI_API_KEY"]="Your Key"
    model.to()
researcher= Agent(
    role='Researcher',
    goal='Research new AI insights',
    backstory='You are an AI research assistant.',
    verbose= True,
    allow_delegation=False,
    llm=llm
    )
# writer = Agent(
#     role='Writer',
#     goal='Write compelling and engaging blog posts about AI trends and Insights',
#     backstory= 'You are an AI blog pos writer who speacializes in writing about AU tipics',
#     verbose=True,
#     allow_delegation=False
#     )
task1= Task(description='Investigate the latest AI trends', agent=researcher,expected_output="A paragraph")
# task2= Task(description='Write a compelling blog post based on latest AI trends', agent=writer)
crew= Crew(
    agents=[researcher],
    tasks=[task1],
    verbose=2
)
result=crew.kickoff()

