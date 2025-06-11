import os


command = 'curl http://localhost:11434/api/generate -d \'{"model": "tinyllama_1b_prompt", "prompt": "what are your tasks?", "stream": false}\''

out = os.system(command)
print('----------------------')
print('out:')
print(out)
print('----------------------')
