
# "Agentic AI with MongoDB and Google Cloud" workshop

## About
<p>This workshop was built to provide a 150 level of knowledge and hands on experience for anyone wanting to build Agents using Google ADK,
MongoDB Atlas and Mongo MCP Server.&ensp;&ensp;It is a mixture of content (slides) and hands on exercises (labs).&ensp;&ensp;Upon completion 
of this, users should have a good working knowledge of - and hands on experience with - building a single agent prototype that utilizes a 
public API, Google Search and a MongoDB Atlas database as its tools.</p>

NOTE:&nbsp;&nbsp;The commands in this repo are OSX (Tahoe 26.4) but should work on any current Linux distribution (Unbuntu, Fedora, Debian) or 
Windows Powershell.  Windows syntax will not be provided

## Prerequsites
### General

- A MongoDB Atlas cluster - an M0 (free) tier on GCP (try to use the same region that your Google Cloud organization uses)
- Access to Google Cloud organization where you have permissions to create a new Project
- Basic familiarity with Python
- Be comfortable using a CLI
- A source code text editor.&ensp;&ensp;Use vi or vim (built-in to OSX / Linux), a code editor like Atom, Nova, CodeEdit) or your
  favorite IDE.

<h2>
  Software
</h2>

| Software | Version  | Validate |
| -------- | -------- | -------- |
| <p>homebrew&nbsp;&nbsp;(highly recommended)</p> | 6.0+  | brew --version |
| <p>uv&nbsp;&nbsp;(optional)</p>| 0.11+  | uv --version  |
| gcloud CLI    | 572.0+  | gcloud --version |
| <p>MongoDB Compass&nbsp;&nbsp;(optional, recommended)</p>  | 1.45+  | About (in tool) |

### Installing required software

<h4>1.&emsp;Install Homebrew</h4>
Open a terminal window on OSX and execute the command below:
<pre>
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```
<p>This may take a few minutes to install.&emsp;When complete, run the command below to validate the install.</p>
<pre>
brew --version
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```

<h4>2.&emsp;Install uv (Python package manager)</h4>
    If you have already install this or prefer to use pip/pip3 then skip to step 2.&emsp;Otherwise, open a terminal window and execute the commands below.
<pre>
brew update
brew install uv
uv --version
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```

<h4>3.&emsp;Install the Google Cloud CLI (gcloud)</h4>
If you already have this installed skip to step 2.   Otherwise, open a terminal window and execute the command below.  The brew update
may take a while to run.  If you executed brew update from the previous step, skip it here.

<pre>
brew update
brew install --cask gcloud-cli
</pre>
```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```

Validate the gcloud CLI is successfully installed.

<pre>
gcloud -- version
</pre>
```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```
You should see output similar to what is shown below.
<pre>
Google Cloud SDK 575.0.1
bq 2.1.33
bundled-python3-unix 3.14.5
core 2026.07.07
gcloud-crc32x 1.0.0
gsutil 5.37
</pre>

### Enable required Google Cloud APIs
<h4>1.&emsp;Authenticate to Google Cloud</h4> 
<p>
Open a terminal window and authenticate to Google Cloud.&emsp;The command below will open a browser window and ask you to pick a Google account
to use.&emsp;When you have successfully authenticated, you can close the browser window and return to the terminal.
</p>
<pre>
gcloud auth login
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```
If you receive this message after successfully authenticating:
<pre>
Your current project is [None].  You can change this settings by running:
gcloud config set project PROJECT_ID
</pre>

Follow the gcloud command syntax above to set the PROJECT_ID before continuing.

<h4>2.&nbsp;Enable the required APIs</h4>
<p>
All of the Google Cloud APIs that we need can be enabled with one command.j
</p>
<pre>
gcloud services enable aiplatform.googleapis.com
</pre>

<!-- 2. The caution box below it (With copy button) -->
```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```
It may take a few minutes to enable all the APIs (there are 30+) 









