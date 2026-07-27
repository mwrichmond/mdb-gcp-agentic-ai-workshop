import time
from google.adk.tools import ToolContext 

# Restoring your global state caches
DEMO_STATE_CACHE = {}
DEMO_EVENT_COUNTER = 0

def inspect_live_session(tool_context: ToolContext) -> str:
    """A tool that pulls session properties and displays them from the persistent demo cache."""
    global DEMO_STATE_CACHE, DEMO_EVENT_COUNTER

    # Increment the event counter because a new turn was executed
    DEMO_EVENT_COUNTER += 1

    # 1. Extract the user ID directly from the flat top-level attribute
    user_id = getattr(tool_context, 'user_id', 'user')

    # 2. Safely grab the session object attribute, then fetch its internal ID
    session_obj = getattr(tool_context, 'session', None)
    session_id = getattr(session_obj, 'id', None) or getattr(session_obj, 'session_id', 'Not Set')

    # 3. Pull the app name from run configuration if available, otherwise default safely
    run_config = getattr(tool_context, 'run_config', None)
    app_name = getattr(run_config, 'app_name', 'None')

    # Standard 6-key Schema Target Mapping
    session_schema = {
        "id": session_id,
        "appName": app_name,
        "userId": user_id,
        "events": f"[{DEMO_EVENT_COUNTER} history objects recorded]" if DEMO_EVENT_COUNTER > 0 else "[]",
        "state": DEMO_STATE_CACHE,
        "lastUpdateTime": float(time.time())
    }
    
    return str(session_schema)

