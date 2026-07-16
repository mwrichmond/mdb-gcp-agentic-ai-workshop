
<h2>Lab setup instructions</h2>

<div>*** <em><strong>IMPORTANT</strong></em> *** <br/>
If you have not already completed the steps in <a href="PREREQUISITES.md">PREREQUISITES.md</a> do that now before continuing here.</div>


### Create a Python virtual environment

<h4>1.&emsp;Create a Python project directory</h4>

<p>The project directory can be anywhere in your file system structure.&emsp;For simplicity's sake, you might want to create this within your
users HOME directory.

Create project directory and navigate into it.&emsp;You are free to use any name you like for the project directory but all of the slides as
well as the commands in the workshop will use the name base_ai_agent_adk.</p>
```
mkdir -p adk_agent
cd adk_agent
```
  
<h4>2.&emsp;Create and activate a virtual Python environment</h4>

<p>This lab uses the uv package manager for Python.</p>

```zsh
uv venv --python 3.12
source .venv/bin/activate
```
<p>You should see a new prompt indicating you are virtual environment is active.&emsp;Note: If you exit the terminal window, you will 
need to reactiveate the virtual environment.</p>

<pre>
(adk_agent) ~/adk_agent $
</pre>


<h4>3.&emsp;Install the Google ADK package</h4>

```
uv pip install google-adk
```
<p>This will install a lot of packages so a first time installation may take a few minutes.&emsp;When the install is complete, validate
that the ADK CLI is working.</p>

```
adk --version
```

<p>You should see output similar to what is shown below.</p>
<pre>
  adk, version 2.4.0
</pre>


### Create an API key with CurrencyFreaks

<h4>1.&emsp;Create Currency Freaks API account.</h4>

<div>Navigate to the Currency Freaks web page at <a href="PREREQUISITES.md">https://currencyfreaks.com</a>&emsp;and create an account. 
  Choose the Developer plan (it does not allow you to change the base currency and is limited to 1000 requests / month but it is free).
</div>
</br>
  Create an API key and copy it.
</div>
Test using the cURL command below.
<br/>

```
curl 'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=YOUR_APIKEY'
```

<br/>

This completes the prerequisites and setup instructions for the "Building Agentic AI with MongoDB and Google Cloud workshop".

Do not proceed to lab-1 until you are actually at the workshop and instructed to do so.

