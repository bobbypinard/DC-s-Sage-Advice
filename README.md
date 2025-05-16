# DC-s-Sage-Advice

# V1.0.1 Release notes
- Changed name to David as to not have confusion between DC CyberSec and DC's sage advice
- Give proper credit to myself
- Lowered insult severity
- Increased frequency penalty
- Increased presence penalty
-- Added modularity in the code base
-- Added logging for research purposes

## Usage
Create a .env file with your Discord API, and OpenAI API keys.
```
DISCORD_TOKEN=""
OPENAI_API_KEY=""
```

Source the virtual environment with uv
```
source .venv/bin/activate
```

Install all the requirements with uv
```
uv pip install -r requirements.txt
```

Start the server
```
python bot.py
```