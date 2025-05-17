Interact with a robot with voice.

- The voice is converted to text.
- The text is sent to an LLM.
- The LLM decides whether to respond normally or do function calling.
  - In case of normal response, the text is converted to sound (the robot responded with something).
  - In case of function calling, the LLM makes the robot act in some way.