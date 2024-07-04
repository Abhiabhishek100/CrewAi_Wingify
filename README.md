# CrewAi_Wingify
Abstract:- 
        In my recent assignment, I was tasked with developing a health recommendation system based on blood test reports. The code was written in Python. However, I encountered issues with setting up my local GPU, which prevented me from obtaining the desired output. The GPU functions correctly on native Windows with Python 3.9, but CrewAI requires Python 3.10 or higher. This discrepancy caused a conflict, making it impossible to utilize the GPU for this project.

Code Explanation:-
          First we imported the important crewai libraries like Agent, Task, Crew etc. Than other libraries like langchain,  os, sys. Then we have set the environment with OpenAI. For getting output we have chosen LLM model llama3:8b.  I downloaded it locally and then ran. For that I have to make two other files. One llama3.sh and llama3ModelFile. These are the steps to set the environment. You should have these files in the same folder and the llama3 installed in your pc in the same environment with command “ollama run llama3”.
           Next step is to come up with the main code. First we have made a fake report text to use it further. In the crewai, the first step is to make agents. We have made 3 agents- analysis_agent, article_agent, recommendation_agent. These three have their own works. First one is to analyse the given text data and summarise it in a human readable manner. Arctilcal_agent sees the web to get the relevant article. Recommandation agent, recommends based on these outputs.
          Now it’s time to define the tasks. We have defined the analysis, article and recommendation task and have given the work to the respective agent. 
     At the end we came to the crew which gave us the final result.


