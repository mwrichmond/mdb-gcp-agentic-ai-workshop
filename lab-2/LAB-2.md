## Lab 2 instructions

### Create a custom Python function to call an external API


<h4>1.&emsp;If you are not already there, navigate to the <i>basic_agent</i> directory</h4>

```
cd basic_agent
```

<h4>2.&emsp;Edit the <i>.env</i> file; adding the line below:

```
CF_API_KEY=9371a7239bbe4164bcac58df4b0867e5
```

<h4>3.&emsp;Copy the <i>custom_functions.py</i> file from the Github repository into the <i>basic_agent</i> directory</h4>

```
curl -O https://raw.githubusercontent.com/mwrichmond/mdb-gcp-agentic-ai-workshop/refs/heads/main/src/adk_agents/basic_agent/custom_functions.py
```
<br/>

<pre>
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   679  100   679    0     0   7780      0 --:--:-- --:--:-- --:--:--  7804
</pre>

<p>
Verify the new files in the directory.
</p>

```
ls -lgoa
```

<pre>
total 36
-rw-r--r--@  1    20 Jul 27 15:14 __init__.py
drwxr-xr-x@  4   128 Jul 27 15:20 __pycache__/
drwxr-xr-x@  9   288 Jul 28 15:23 ./
drwxr-xr-x@ 12   384 Jul 28 10:35 ../
-rw-r--r--@  1   143 Jul 28 12:20 .env
-rw-r--r--@  1   252 Jul 27 15:20 agent.py
-rw-r--r--@  1   679 Jul 28 12:02 custom_functions.py
</pre>

<h4>4.&emsp;Replace the existing <i>agent.py</i> with the one from the lab-2/src folder in the Github repository </h4>
<br/>

```
curl -O https://raw.githubusercontent.com/mwrichmond/mdb-gcp-agentic-ai-workshop/refs/heads/main/lab-2/src/adk_agents/basic_agent/agent.py
```
<br/>

<pre>
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   374  100   374    0     0   3221      0 --:--:-- --:--:-- --:--:--  3224
</pre>

<p>
Verify the new files in the directory.
</p>

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
-rw-r--r--@  1   374 Jul 28 16:12 agent.py
-rw-r--r--@  1   679 Jul 28 12:02 custom_functions.py
</pre>

<h4>5.&emsp;Test the updated agent</h4>
<br/>
<p>Navigate one level up to the parent directory - <i>adk_agents</i> - and start the ADK web UI</p>

```
cd ..
adk web
```

<p>Open a browser window to <a href="127.0.0.1:8000"></a> and test the agent.></p>   <a href="SETUP.md">SETUP.md</a> 
