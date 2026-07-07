
Workshop prerequisites
This workshop was built on OSX (Tahoe 26.4) but should work on any current Linux distribution or Windows Powershell

The high level prerequisites are listed below:

A MongoDB Atlas cluster - an M0 (free) tier on GCP (try to use the same region that your Google Cloud organization uses)

Access to Google Cloud organization where you can either:

Use an existing project (you would need Project if necessary)




| Software | Version  | Validate |
| -------- | -------- | -------- |
| uv (Python package manager| 0.11+  | uv --version  |
| gcloud CLI   | 572.0+  | gcloud --version |
| MongoDB Compass (optional, recommended)  | 1.45+  | About (in tool) |



Enable required Google Cloud APIs

<pre>
gcloud services enable aiplatform.googleapis.com
</pre>

<!-- 2. The caution box below it (With copy button) -->
```text
ᴜsᴇ ᴄᴏᴅᴇ ᴡɪᴛʜ ᴄᴀᴜᴛɪᴏɴ.
```





