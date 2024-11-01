# operation_selection_few_shot.py

operation_few_shot_examples = [
    {
        "user": "What’s my current balance across all my accounts?",
        "connector": "plaid",
        "assistant": {
            "operation": "get_account_balance"
        }
    },
    {
        "user": "Schedule a call with my manager tomorrow at 3 PM.",
        "connector": "google_calendar",
        "assistant": {
            "operation": "create_event"
        }
    },
    {
        "user": "Send the monthly financial report to the team.",
        "connector": "gmail",
        "assistant": {
            "operation": "send_email"
        }
    },
    {
        "user": "Pull up the latest engagement metrics from last week.",
        "connector": "google_analytics",
        "assistant": {
            "operation": "get_engagement_metrics"
        }
    },
    {
        "user": "Find nearby restaurants open for dinner tonight.",
        "connector": "yelp",
        "assistant": {
            "operation": "search_nearby_restaurants"
        }
    }
]
