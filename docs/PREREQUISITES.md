
# "Agentic AI with MongoDB and Google Cloud" workshop

## About
This workshop was built on OSX (Tahoe 26.4) but should work on any current Linux distribution or Windows Powershell.  Commands
provided in this repo will be validated to work on OSX; most will also work on major Linux distributions (Unbuntu, Fedora, Debian)
Windows syntax will not be provided.

## General Prerequisites

- A MongoDB Atlas cluster - an M0 (free) tier on GCP (try to use the same region that your Google Cloud organization uses)
- Access to Google Cloud organization where you have permissions to create a new Project
- Basic familiarity with Python
- Be comfortable using different CLIs 



| Software | Version  | Validate |
| -------- | -------- | -------- |
| uv (Python package manager) | 0.11+  | uv --version  |
| homebrew | 6.0+  | brew --version
| gcloud CLI   | 572.0+  | gcloud --version |
| MongoDB Compass (optional, recommended)  | 1.45+  | About (in tool) |

Unless you have an IDE that you can't live without, I would do one of two things:

- Simply use vi or vim built-in to OSX / Linux  (there is a learning curve, but you won't need to know it that well for this workshop)
- Install a lightweight code editor like Atom, CotEdit, Nova, CodeEdit, etc.  



### Enable required Google Cloud APIs

#### 1.  Install the Google Cloud CLI (gcloud)
If you already have this installed skip to step 2.   Otherwise, open a terminal window and execute the command below.  The brew update
may take a while to run.

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

Open a terminal window and authenticate to Google Cloud.  The command below will open a browser window and ask you to pick a Google account
to use.  When you have successfully authenticated, you can close the browser window and return to the terminal.

<pre>
gcloud auth login
</pre>

```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```






<pre>
gcloud services enable aiplatform.googleapis.com
</pre>

<!-- 2. The caution box below it (With copy button) -->
```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```





