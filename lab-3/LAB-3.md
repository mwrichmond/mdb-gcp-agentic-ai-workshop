## Lab 3 instructions

### Create an "inline" MongoDB MCP Server as an MCPTool for the agent

This Lab will involve creating a 3rd agent tool - a MongoDB MCP server - where the code for the tool is not configured
in a separate file; rather it is embedded "inline" into the <i>agent.py</i> file.  

<p>How does this work?&nbsp;&nbsp;Let's take a look.&nbsp;&nbsp;The lab-3 <i>agent.py</i> code is shown below:</p>
<br/>
<div>
<img width="820" height="717" alt="image" src="https://github.com/user-attachments/assets/dcf6225d-6509-4640-af1c-1216922bda9d" />
</div>
<br/>
<p>OK.&nbsp;&nbsp;Other than some new required imports on lines 5-8; the real code starts at line 17.</p>

<p>Without going too deep into the weeds here; what we are doing is spawning a nodejs sub-process (the MongoDB MCP Server) on localhost
when the ADK agent starts up (i.e. a user executes the "adk web" command).  
 
The easy way to think about this is that on agent startup after lines 17 - 31 execute; there will be a running nodejs process on your 
localhost.  At this point the MongoDB MCP Server has successfully authenticated to an Atlas cluster and all of the available MongoDB commands
have been registered as tools with the LLM.

The process sits idle until it is actually invoked by the LLM.  It is a stateful session if you will so it remains available for use at any 
turn in the agent:user interaction cycle.

When the adk web process terminates (usually via a CTRL-C) the ADK backend will gracefully terminate the node process on localhost.

1.&emsp;If you are not already there, navigate to the** `basic_agent` directory.

```
cd basic_agent
```

**2.&emsp;Replace the current** <i>`custom_agents.py`</i> **file**

```
curl -O https://raw.githubusercontent.com/mwrichmond/mdb-gcp-agentic-ai-workshop/refs/heads/main/lab-3/src/adk_agents/basic_agent/custom_agents.py
```


<h4>2.&emsp;Copy the <i>agents.py</i> file from the Github repository into the <i>basic_agent</i> directory</h4>

```

```
<br/>

<pre>
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                Dload  Upload   Total   Spent    Left  Speed
100   415  100   415    0     0   4897      0 --:--:-- --:--:-- --:--:--  4940
</pre>

Verify the new files in the directory.

```
ls -lgoa
````

<pre>
total 32
-rw-r--r--@  1    20 Jul 27 15:14 __init__.py
drwxr-xr-x@  5   160 Jul 28 16:20 __pycache__/
drwxr-xr-x@  9   288 Jul 28 18:09 ./
drwxr-xr-x@ 12   384 Jul 28 10:35 ../
-rw-r--r--@  1   143 Jul 28 12:20 .env
-rw-r--r--@  1   374 Jul 28 16:12 agent.py
-rw-r--r--@  1   415 Jul 28 18:09 custom_agents.py
-rw-r--r--@  1   679 Jul 28 12:02 custom_functions.py

 <h4>3.&emsp;Test the updated agent</h4>

Navigate one level up to the parent directory `adk_agents` and start the ADK web UI

```
cd ..
adk web
```

Open a browser window to&nbsp;<a href=127.0.0.1:8000>http://127.0.0.1:8000</a>&nbsp;and test the agent.
