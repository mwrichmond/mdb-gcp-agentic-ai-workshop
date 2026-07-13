
<h2>Lab setup instructions</h2>

<div>*** <em><strong>IMPORTANT</strong></em> *** <br/>
If you have not already completed the steps in <a href="PREREQUISITES.md">PREREQUISITES.md</a> do that now before continuing here.</div>


### Create a Python virtual environment

<h4>1.&emsp;Create a Python project directory</h4>

<p>The project directory can be anywhere in your file system structure.&emsp;For simplicity's sake, you mightjust want to create this within your
users HOME directory.

Create project directory and navigate into it.&emsp;You are free to use any name you like for the project directory but all of the slides as
well as the commands in the workshop will use the name base-ai-agent-adk.</p>
```
mkdir -p base-ai-agent-adk
cd base-ai-agent-adk
```
  
<h4>2.&emsp;Create and activate a virtual Python environment</h4>

<p>This lab uses the uv package manager for Python.&emsp;If are using venv, skip the uv command and use the python command..</p>

<pre>
uv venv --python 3.12
source .venv/bin/activate
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```
<pre>
python -m venv .venv
source .venv/bin/activate
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```

</pre>
