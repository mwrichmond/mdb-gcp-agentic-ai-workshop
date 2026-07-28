i## Lab 2 instructions

### Create the base agent using ADK

<h4>1.&emsp;If you are not already there, navigate to the <i>basic_agent</i> directory</h4>

```
cd basic_agent
```

<h4>2.&emsp;Edit the <i>.env</i> file</h4>

Add your Currency Freaks API key

```
CF_API_KEY=<YOUR_CURRENCY_FREAKS_API_KEY>
```

<h4>3.&emsp;Copy the <i>custom_functions.py</i> file into the <i>basic_agent</i> directory</h4>

<p>Navigate to <a href="../src/adk_agents/basic_agent/custom_functions.py"><i>custom_functions.py</i></a> in the <i>src</i> directory.
</p>
Click the Raw button at the top right of the code view to open the plain text version.  







<div>From the <em>adk_agents</em> directory, execute the command below.&emsp;The command script will create a sub-directory ( <em>basic_agent</em> ) and
create several files within in.</div>
<br/>

```
adk create basic_agent
```

<pre>
Choose a model for the root agent:
1. gemini-3.5-flash
2. Other models (fill later)
Choose model (1, 2): 
</pre>
