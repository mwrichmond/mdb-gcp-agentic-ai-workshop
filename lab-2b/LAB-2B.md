## Lab 2B instructions

### Create a Python wrapper function to call native Google Search

**1.&emsp;If you are not already there, navigate to the** `basic_agent` **directory.**

```
cd basic_agent
```

**2.&emsp;Replace the current** <i>`custom_agents.py`</i> **file**

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
</pre>



<h4>3.&emsp;Replace the existing <i>agent.py</i> with the one from the lab-2b/src folder in the Github repository</h4>

```
curl -O https://raw.githubusercontent.com/mwrichmond/mdb-gcp-agentic-ai-workshop/refs/heads/main/lab-2b/src/adk_agents/basic_agent/agent.py
```

 <pre>
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                  Dload  Upload   Total   Spent    Left  Speed
100   374  100   374    0     0   3221      0 --:--:-- --:--:-- --:--:--  3224 
 </pre>

Verify the new files in the directory.

```
ls -lgoa
```

<pre>
total 32
-rw-r--r--@  1    20 Jul 27 15:14 __init__.py
drwxr-xr-x@  4   128 Jul 27 15:20 __pycache__/
drwxr-xr-x@  7   224 Jul 28 16:16 ./
drwxr-xr-x@ 12   384 Jul 28 10:35 ../
-rw-r--r--@  1   143 Jul 28 12:20 .env
-rw-r--r--@  1   415 Jul 28 16:12 agent.py
-rw-r--r--@  1   679 Jul 28 12:02 custom_functions.py
</pre>

<h4>4.&emsp;Test the updated agent</h4>
<br/>
<p>Navigate one level up to the parent directory - <i>adk_agents</i> - and start the ADK web UI</p>

```
cd ..
adk web
```

Open a browser window to&nbsp;<a href=127.0.0.1:8000>http://127.0.0.1:8000</a>&nbsp;and test the agent.
