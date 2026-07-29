## Lab 3 instructions

### Create an "inline" MongoDB MCP Server as an MCPTool for the agent

This Lab will involve creating a 3rd agent tool - a MongoDB MCP server - where the code for the tool is not configured
in a separate file; rather it is embedded "inline" into the <i>agent.py</i> file.  

How does this work?  Let's take a look.  The code is shown below:

```{.r filename="/lab-3/src/adk_agents/basic_agent/agent.py" startFrom=1}
```


<h4>1.&emsp;If you are not already there, navigate to the <i>basic_agent</i> directory</h4>

```
cd basic_agent
```

<h4>2.&emsp;Copy the <i>agents.py</i> file from the Github repository into the <i>basic_agent</i> directory</h4>

```
curl -O https://raw.githubusercontent.com/mwrichmond/mdb-gcp-agentic-ai-workshop/refs/heads/main/lab-2b/src/adk_agents/basic_agent/custom_agents.py
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
