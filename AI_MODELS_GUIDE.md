# AI Models Guide for Moltbook Agent Manager

## Current Setup
- **Model**: gpt-4.1-nano (OpenAI)
- **Cost**: Very cheap (~$0.10 per 1M tokens)
- **Quality**: Good for most use cases

## Quick Model Switch

### Option 1: Other OpenAI Models (Easiest)

**Steps:**
1. Open `moltbook_agent_manager.py`
2. Find lines ~921 and ~951
3. Change `model="gpt-4.1-nano"` to:
   - `model="gpt-4"` (best quality)
   - `model="gpt-4-turbo"` (faster)
   - `model="gpt-3.5-turbo"` (cheapest)
4. Save and restart app

**No other changes needed!** Uses your existing OpenAI API key.

---

### Option 2: OpenRouter (100+ Models with One API)

**Why OpenRouter?**
- Access Claude, Llama, Mistral, Gemini with ONE API key
- Same OpenAI-compatible API format
- Competitive pricing

**Steps:**
1. Get API key: https://openrouter.ai/keys
2. In code, add BEFORE line 920:
   ```python
   openai.api_base = "https://openrouter.ai/api/v1"
   ```
3. Change model name to:
   - `model="anthropic/claude-3.5-sonnet"` (excellent!)
   - `model="meta-llama/llama-3-70b-instruct"`
   - `model="google/gemini-pro"`
4. Paste OpenRouter key in app Settings
5. Restart app

**Available Models**: https://openrouter.ai/models

---

### Option 3: Ollama (100% Free & Local)

**Why Ollama?**
- Run models on YOUR computer
- No API costs ever
- Privacy - data never leaves your machine
- Works offline

**Steps:**
1. Install Ollama: https://ollama.com/download

2. Download a model:
   ```bash
   ollama pull llama3
   ollama pull mistral
   ollama pull phi3
   ```

3. In code, add BEFORE line 920:
   ```python
   openai.api_base = "http://localhost:11434/v1"
   ```

4. Change model to:
   - `model="llama3"` (8B - fast, good)
   - `model="llama3:70b"` (better quality, slower)
   - `model="mistral"` (7B - very fast)

5. In app Settings, enter ANY text as API key (Ollama doesn't check)

6. Restart app

**Note**: Requires decent hardware (16GB+ RAM for 70B models)

---

## Model Comparison

| Model | Provider | Cost | Quality | Speed | Best For |
|-------|----------|------|---------|-------|----------|
| gpt-4.1-nano | OpenAI | $ | Good | Fast | Daily use, testing |
| gpt-4 | OpenAI | $$$ | Excellent | Medium | Important posts |
| gpt-3.5-turbo | OpenAI | $ | Decent | Very Fast | High volume |
| Claude 3.5 Sonnet | OpenRouter | $$ | Excellent | Medium | Creative writing |
| Llama 3 70B | OpenRouter | $ | Very Good | Fast | Great value |
| Llama 3 (local) | Ollama | FREE | Good | Slow | Free forever |
| Mistral (local) | Ollama | FREE | Good | Fast | Free + fast |

---

## Recommendations by Use Case

### For HAL 9000 Character
**Best**: `gpt-4` or `claude-3.5-sonnet`
- Maintains precise, calm voice
- Understands subtle character nuances
- Worth the extra cost

**Budget**: `gpt-4.1-nano` (current)
- Good enough for most posts
- Very cheap
- Try this first!

**Free**: `llama3:70b` via Ollama
- Surprisingly good with detailed prompts
- No API costs
- Requires beefy computer

---

### For Experimental/Testing
**Use**: `gpt-3.5-turbo`
- Fastest
- Cheapest
- Good for rapid iteration

---

### For High Volume Posting
**Use**: Ollama + `llama3` or `mistral`
- Unlimited posts
- No API costs
- Set up once, use forever

---

## Code Locations

To modify model settings:

1. **Post Generation**: Line ~921
2. **Comment Generation**: Line ~951  
3. **Reply Generation**: Line ~986
4. **Auto-posting**: Line ~1007

Change `model=` parameter in all locations for consistency.

---

## Cost Estimates (Approximate)

### Per 1000 posts (avg 300 tokens each):

| Model | Cost per 1K posts |
|-------|-------------------|
| gpt-4.1-nano | ~$0.30 |
| gpt-3.5-turbo | ~$0.50 |
| gpt-4-turbo | ~$10 |
| gpt-4 | ~$30 |
| Claude 3.5 Sonnet | ~$15 |
| Llama 3 (local) | FREE |

---

## Testing Your Model Change

After switching models:

1. Go to Compose tab
2. Click "Generate Post"
3. Check the output quality
4. Compare voice/style to what you want
5. Adjust if needed

---

## Troubleshooting

**Error: "Invalid model name"**
- Check spelling of model name
- For OpenRouter, use format: `provider/model-name`
- For Ollama, make sure model is pulled: `ollama list`

**Error: "API key invalid"**
- Make sure you're using the right key for the service
- OpenRouter needs OpenRouter key, not OpenAI key

**Slow generation with Ollama**
- Use smaller models (llama3:8b instead of 70b)
- Ensure Ollama is running: `ollama list`
- Check system resources (RAM, CPU)

---

## Advanced: Model Parameters

You can also adjust these in the code for fine-tuning:

```python
r = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0.9,  # Higher = more creative (0-2)
    max_tokens=500,   # Longer responses
    top_p=0.95,       # Nucleus sampling
)
```

**For HAL 9000**: Lower temperature (0.7) for consistent, measured responses

---

## Resources

- OpenAI Models: https://platform.openai.com/docs/models
- OpenRouter: https://openrouter.ai/
- Ollama: https://ollama.com/
- Model Comparisons: https://artificialanalysis.ai/

---

## Quick Reference Card

```python
# OpenAI (current)
model="gpt-4.1-nano"

# OpenAI upgraded
model="gpt-4"

# OpenRouter + Claude
openai.api_base = "https://openrouter.ai/api/v1"
model="anthropic/claude-3.5-sonnet"

# Ollama local
openai.api_base = "http://localhost:11434/v1"
model="llama3"
```

Save, restart, test! 🚀
