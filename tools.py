tools = [
    {
        "type": "function",
        "function": {
            "name": "set_car_motion",
            "description": "Move the robot in a specified direction.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]