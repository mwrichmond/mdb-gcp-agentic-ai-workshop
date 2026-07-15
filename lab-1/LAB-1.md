 ## Lab 1 instructions

### Create the base agent using ADK

<h4>1.&emsp;Navigate to the Python project directory</h4>

<div><p>If you followed the naming suggested in <a href="SETUP.md">SETUP.md</a> the directory should be <em>base_ai_agent_adk</em>.</p></div>

```
cd base_ai_agent_adk
```
  
<h4>2.&emsp;Create an agent named <em>basic_agent</em>.</h4>

<p>From the <em>base_ai_agent_adk</em> directory, execute the command below.</p>

```
adk create basic_agent
```

<pre>
Choose a model for the root agent:
1. gemini-3.5-flash
2. Other models (fill later)
Choose model (1, 2): 
</pre>

Type 1 and press [ENTER]

<pre>
1. Google AI
2. Vertex AI
3. Login with Google
Choose a backend: (1, 2, 3):
</pre>

Type 2 and press [ENTER]

<pre>
You need an existing Google Cloud acounts and project, check out this link for details:
https://google.github.io/adk-docs/get-started/quickstart/#gemini---google-cloud-vertex-ai

Enter Google Cloud project ID [<your-Project-ID>]
Enter Google Cloud region [us-central1]
</pre>

The values for project ID and region should be auto-filled.&emsp;If they are not add you values and press [ENTER] afer
each entry.
<br/><br/>
<pre>
Agent created in /Users/mattrichmond/base_ai_agent_adk/basic_agent:
- .env
- .gitignore
- __init__.py
- agent.py

WARNING:  Secrets (like GOOGLE_API_KEY) are stored in .env.
</pre>

Validate that all files have been created.  

```
cd basic_agent
ls -lgoa
```

You should see output similar to what is shown below.

<pre>
-rw-r--r--@  1     51 Jun 25 22:05 __init__.py
drwxr-xr-x@ 11    352 Jul  8 18:04 .
drwxr-xr-x@  7    224 Jul 13 22:22 ..
-rw-r--r--@  1    232 Jul  8 17:51 .env
-rw-r--r--@  1      5 Jul  8 17:51 .gitignore
-rw-r--r--@  1    917 Jul  1 21:14 agent.py
</pre>


<h4>3.&emsp;View the agent files</h4>

<div>Before running the agent for the first time, let's look at the <em>.env</em> file.</div>
<br/>

```
cat .env
```

<pre>
GOOGLE_GENAI_USE_ENTERPRISE=1
GOOGLE_CLOUD_PROJECT=&lt;your_project_ID&gt;
GOOGLE_CLOUD_LOCATION=&lt;your_location&gt;
</pre>

<div>
Nothing really exciting here; not yet anyway.&emsp;Just validate that your Google Cloud project and location values are what you
specified in the ADK create script.
</div>
<br/>
<div>
Let's also view the <em>agent.py</em> file.
</div>
<br/>

```
cat agent.py
```

<pre>
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge.',
)
</pre>
<br/>

<h4>4.&emsp;Run the agent with a web UI</h4>

Remember that all ADK commands need to be executed from the parent directory of the agent. &emsp;  Our file structure looks like this:
<pre>
base_ai_agent_adk
└── basic_agent
    ├── __init__.py
    ├── __pycache__
    ├── .env
    ├── .gitignore
    └── agent.py
</pre>
<br/>
<div>So we need to launch the agent from the <em>base_ai_agent_adk</em>&nbsp;directory.</div>
<br/>

```
cd ..
adk web
```

<div>
You will see some INFO messages appear as the agent launches.  After a few seconds, the message below should be displayed:
</div>
<br/>
<pre>
+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://127.0.0.1:8000.                         |
+-----------------------------------------------------------------------------+
</pre>
<div>
Open a browser window at the address above to test the agent.&emsp;IMPORTANT: do NOT close the terminal window or you will terminate the web
server.  Messages will continue to be displayed in the terminal window as you interact with the agent.  
</div>
<div>
<br/>
You should see a screen similar to the one shown below.
<br/><br/>
<img width="981" height="490" alt="image" src="https://github.com/user-attachments/assets/18952dfa-2fc9-41f3-8364-61b764653b2e" />

</div>
