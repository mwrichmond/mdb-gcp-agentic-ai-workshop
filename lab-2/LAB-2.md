## Lab 2 instructions

### Create a custom Python function to call an external API

<h4>1.&emsp;If you are not already there, navigate to the <i>basic_agent</i> directory</h4>

```
cd basic_agent
```

<h4>2.&emsp;Edit the <i>.env</i> file</h4>

<p>Add your Currency Freaks API key to the file and save it.</p>

```
CF_API_KEY=<YOUR_CURRENCY_FREAKS_API_KEY>
```

</p> When completed your file should resemble the one below (the API key will be different)</p>

<pre>
GOOGLE_GENAI_USE_ENTERPRISE=1
GOOGLE_CLOUD_PROJECT=matt-richmond
GOOGLE_CLOUD_LOCATION=us-central1
CF_API_KEY=9371a7239bbe4164bcac58df4b0867e9
</pre>

<h4>3.&emsp;Copy the <i>custom_functions.py</i> file from the Github repository into the <i>basic_agent</i> directory</h4>
<br/>

```
curl -O https://raw.githubusercontent.com/mwrichmond/mdb-gcp-agentic-ai-workshop/refs/heads/main/src/adk_agents/basic_agent/custom_functions.py
```
<br/><br/>

```
adk create basic_agent
```

