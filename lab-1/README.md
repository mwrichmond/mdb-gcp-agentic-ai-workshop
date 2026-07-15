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



Agent created in /Users/mattrichmond/base_ai_agent_adk/basic_agent:
- .env
- .gitignore
- __init__.py
- agent.py

WARNING:  Secrets (like GOOGLE_API_KEY) are stored in .env.
</pre>
