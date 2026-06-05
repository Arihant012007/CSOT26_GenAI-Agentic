# Week 1 Learnings: Agentic LLM Foundations

## 1. LLM API Fundamentals
* **The API is Stateless:** Models like DeepSeek or Llama have zero memory. Every single API call is a blank slate.
* **State Management:** Built conversational memory by creating a "rolling buffer" that stores user and assistant messages, resending the entire history on every request.
* **Prompt Engineering:** Enforced AI behavior by keeping a `system` prompt isolated at the very front of the payload so it never gets deleted.

## 2. Environment & Debugging Mastery
* **Virtual Environments:** Resolved `ModuleNotFoundError` by correctly aligning the VS Code integrated terminal with the active Python interpreter.
* **Dependency Management:** Managed force-upgrades for modern SDKs (`openai >= 1.0.0`) and graceful downgrades for specific networking libraries (`urllib3<2`) to bypass macOS LibreSSL compatibility errors.

## 3. AI Infrastructure & Routing
* **Understanding Endpoints:** Learned what an API endpoint is and why `404 - No endpoints found` occurs when free-tier servers hit capacity and drop connections.
* **Model Routing:** Utilized `openrouter/free` to automatically hunt for live servers rather than hardcoding fragile ones.
* **Provider Swapping:** Leveraged the standard OpenAI SDK to switch from OpenRouter to Groq instantly by changing the `base_url` and API key, without rewriting core logic.

## 4. Security & Deployment
* **Key Hygiene:** Secured API keys in a `.env` file via `python-dotenv` and added it to `.gitignore` before making any commits.
* **GitHub Workflow:** Executed an open-source submission workflow: forking a repository, cloning locally, isolating files, verifying the `.env` did not leak, and pushing the final commit to a public repo.
