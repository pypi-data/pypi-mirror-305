# Simplified, stringified task_few_shot_examples for plan_tasks
import json
task_few_shot_examples = [
    {
        "user": json.dumps({"user_input": "What's the current price of Bitcoin?"}),
        "assistant": json.dumps({"tasks": [{"connector": "coindesk", "operation": "get_current_bitcoin_price", "params": {}}]})
    },
    {
        "user": json.dumps({"user_input": "Check my bank account balance at Plaid."}),
        "assistant": json.dumps({"tasks": [{"connector": "plaid", "operation": "get_balance", "params": {"client_id": "your-client-id", "secret": "your-secret", "access_token": "user-access-token"}}]})
    },
    {
        "user": json.dumps({"user_input": "Schedule a Zoom meeting for next Tuesday with the marketing team."}),
        "assistant": json.dumps({"tasks": [{"connector": "zoom", "operation": "schedule_meeting", "params": {"topic": "Marketing Team Meeting", "start_time": "2023-10-10T10:00:00Z", "duration": 60}}]})
    },
    {
        "user": json.dumps({"user_input": "Send an email to the finance team with the weekly report."}),
        "assistant": json.dumps({"tasks": [{"connector": "gmail", "operation": "send_email", "params": {"to": "finance@company.com", "subject": "Weekly Financial Report", "body": "Please find attached the weekly financial report."}}]})
    },
    {
        "user": json.dumps({"user_input": "Find a list of properties for sale under $500,000 in Zillow."}),
        "assistant": json.dumps({"tasks": [{"connector": "zillow", "operation": "search_properties", "params": {"max_price": 500000, "location": "San Francisco, CA"}}]})
    }
]
