# LLM API Integration — Receipt Extraction Endpoint

FlyRank Backend Track · Week 7 · A17

## What it does

Takes a pasted receipt (plain text) and returns structured, validated JSON —
merchant, date, total, currency, and line items — instead of a human having
to type it in by hand. See [`JOB-CARD.md`](./JOB-CARD.md) for the full spec.

## Status

- [x] Stage 0 — provider connected, key in `.env`
- [ ] Stage 1 — endpoint + input validation + output schema + stub mode
- [ ] Stage 2 — prompt as a versioned file
- [ ] Stage 3 — parse, validate, repair retry, quarantine
- [ ] Stage 4 — timeout, retry policy, cost logging, kill switch
- [ ] Stage 5 — eval set, results, published

## Provider

Using **Groq** (OpenAI-compatible, free tier, no credit card).

Env vars needed (see `.env.example`):
```
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_API_KEY=<your key>
LLM_MODEL=llama-3.1-8b-instant
```

## Run it

```
pip install -r requirements.txt   # or: pip install openai python-dotenv fastapi pydantic
cp .env.example .env              # then fill in your real key
python src/llm/hello.py           # Stage 0 checkpoint — should print "ready"
```

## Curl examples

_(added in Stage 1)_

## Eval results

_(added in Stage 5)_

## Cost per call / per 10,000 requests

_(added in Stage 5)_

## What I'd fix with another day

_(added in Stage 5)_
