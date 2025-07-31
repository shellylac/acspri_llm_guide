---
---

# 🛠️ Troubleshooting API Errors – Gemini, OpenAI, Hugging Face

This module catalogs **common issues** encountered when running inference across Gemini, OpenAI, and Hugging Face APIs. It includes **error types**, **diagnostic strategies**, and **practical fixes** that apply in both notebook and production environments.

---

## 📦 Error Categories

We break down issues into the following categories:

| Category           | Description                                                                 |
|--------------------|------------------------------------------------------------------------------|
| 🔐 Authentication   | Missing, invalid, or misconfigured API key                                  |
| 🔤 Model Access      | Model unavailable, private, or requires approval                           |
| 🔁 Rate Limiting     | Sending too many requests in a short time window                           |
| 💡 Misconfiguration | Invalid parameters, mismatched models, or incorrect prompt structure        |
| 💥 Output Errors     | Truncated, empty, or nonsensical outputs                                   |
| 🔌 Network Issues    | Timeouts, SSL errors, DNS failures                                         |

---

## 🔐 Authentication Errors

### ❌ Error: `401 Unauthorized` or `Invalid API Key`

**Occurs When:**
- API key is missing or malformed
- Wrong key used for provider (e.g., OpenAI key in Gemini)

**How to Fix:**
- Confirm correct API key from dashboard
- Avoid wrapping keys in quotes twice (e.g., `""sk-...""` = bad)
- In Python, ensure key is passed securely (e.g., via `os.environ["API_KEY"]`)

---

## 🔤 Model Access Errors

### ❌ Error: `403 Forbidden`, `Model Not Found`, or `Join the Waitlist`

**Occurs When:**
- Using a model that is gated (e.g., GPT-4, LLaMA-2)
- Using HF model that is not publicly hosted

**Fix:**
- Switch to open model (`gpt-3.5-turbo`, `gemini-1.5-flash`)
- Accept model terms on Hugging Face model card
- Use platform-provided base models

---

## 🔁 Rate Limiting

### ❌ Error: `429 Too Many Requests` or `Quota Exceeded`

**Occurs When:**
- Sending requests too frequently
- Free tier quota exhausted

**Fix:**
- Add `time.sleep(1)` between calls in test loops
- Use exponential backoff strategy
- Consider upgrading to paid tier or requesting quota bump

---

## 💡 Misconfiguration Errors

### ❌ Error: `InvalidArgument`, `BadRequest`, or `Missing required field`

**Occurs When:**
- Malformed prompt object (e.g., missing `messages` list in OpenAI)
- Model name or parameters misconfigured

**Fix:**
- Validate required fields for each provider:
  - OpenAI needs `messages=[{"role": "user", ...}]`
  - Gemini needs string or list of ContentBlocks
- Avoid typos in model names (`gpt-3.5-turbo` not `gpt_3.5_turbo`)

---

## 💥 Output-Related Errors

### ❌ Problem: Output is empty, clipped, or nonsensical

**Causes:**
- `max_tokens` is too small
- Prompt is malformed or lacks clarity
- Completion cut off by stop sequence or input formatting

**Fix:**
- Set `max_tokens=500+` when unsure
- Use delimiters to separate instructions and data
- Add `"stop"` parameter only when needed

---

## 🔌 Network / Transport Errors

### ❌ Error: `Timeout`, `SSL handshake failed`, `ConnectionError`

**Occurs When:**
- Internet connectivity issues
- Cold-start latency on server
- Client config not compatible with TLS/SSL version

**Fix:**
- Retry with backoff
- Try another network (VPN, tethering)
- Ensure requests lib is up to date (`pip install -U requests`)

---

## 🧰 Debugging Workflow

1. **Print full response or traceback**  
   Don't just print `response.text` — look at headers and `.status_code`.

2. **Test known good example**  
   Use working prompt from docs or quickstart to eliminate logic errors.

3. **Switch platform temporarily**  
   Try Gemini vs OpenAI — helps isolate SDK vs logic issue.

4. **Log full payloads** (use `print(json.dumps(payload, indent=2))`)

5. **Use curl or Postman**  
   Helps rule out local Python issues.

---

## 🔗 Related Modules

| File                                | Purpose                                         |
|-------------------------------------|-------------------------------------------------|
| `api_key_setup.md`                  | Covers key management and security              |
| `api_inference_quickstart.md`       | Examples of good payloads                       |
| `openai_api_basic_call.md`          | OpenAI wrapper with error handling              |
| `gemini_api_basic_call.md`          | Gemini wrapper including exception handling     |
| `hf_inference_api_call.md`          | Hugging Face API call + response parsing        |

---
