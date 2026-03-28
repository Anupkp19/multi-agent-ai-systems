# ⚙️ Setup Instructions (Designed to Be Straightforward)

I’ve put together these steps to keep the setup process as smooth and predictable as possible.

## 🖥️ Choose Your Platform

- **Windows:** [Setup Guide](setup/SETUP-PC.md)  
- **Mac:** [Setup Guide](setup/SETUP-mac.md)  
- **Linux:** [Setup Guide](setup/SETUP-linux.md)  

If you run into any issues, feel free to reach out.

---

### ⚠️ Important Note for Windows Users

Before anything else, make sure you’ve completed **“Gotcha #4”** in the Windows setup guide:  
👉 Installing **Microsoft Build Tools**

If you skip this, CrewAI may fail with a confusing **Chroma-related error**.

---

## 🚀 Installing CrewAI

Run the following command in your **Cursor terminal** from the project root directory:

```bash
uv tool install crewai==0.130.0 --python 3.12