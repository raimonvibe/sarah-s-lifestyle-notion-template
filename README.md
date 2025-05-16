# 🌌 Automating Notion Templates with Python: A Developer’s Guide  

A workspace should be more than just a collection of notes—it should evolve with you.  
If you’ve ever wanted to create a **smart, adaptable Notion template** that does more than just hold text, this guide is for you.  

I’ll walk you through how to use the **Notion API** to generate fully functional, customizable templates with Python.  
You'll also learn how we **overcame troubleshooting issues** like permissions, missing integrations, and formatting problems.  

By the end, you’ll have a **fully automated Notion template** that dynamically creates sections for:  
✅ **Task Management**  
📔 **Journaling with Prompts**  
📆 **Habit Tracking**  
🎯 **Goal Setting**  
📚 **Knowledge Hub**  
🌺 **Mood & Motivation Check-Ins**  

---

## **🚀 Why Code Your Notion Templates?**  

Before diving into the technical steps, let's talk about **why this is worth your time**:  

- ✅ **No More Manual Copy-Pasting** – Automate your workflow.  
- ✅ **Scalability** – Generate multiple pages dynamically.  
- ✅ **Adaptability** – Modify templates dynamically via API.  
- ✅ **AI and External Integrations** – Extend Notion’s power with APIs.  

Instead of **spending time recreating templates**, imagine **running a single command** and having an entire **structured workspace ready**.  

---  

## **1️⃣ Setting Up the Notion API**  

### **Step 1: Create a Notion Integration**  
To use the API, you need to **create an internal integration** in Notion.  

- Go to the **[Notion My Integrations Page](https://www.notion.so/my-integrations)**.  
- Click **"New Integration"** and give it a name (e.g., `"Template Generator"`).  
- Copy the **Internal Integration Secret**—this is your API key.  

### **Step 2: Ensure the Template is in the Same Workspace**  
We ran into issues when creating a new Notion template that **wasn't in the same workspace as the API integration**.  
- Click the **Notion logo (top-left corner)** and select **the same environment where you created the integration**.  
- Create a **new page** under this workspace before running your API script.  

If you don’t do this, your API might return a `404 object_not_found` error because it doesn’t have access to pages outside its workspace.  

### **Step 3: Assign the API Connection in Notion**  
We had to manually select the API **from a dropdown menu in Notion** before it could modify pages. You can do this in **two places**:  

1️⃣ **Share Button (Top Right Corner)**  
   - Click **"Share"** in the top-right corner of your Notion page.  
   - If your integration is visible, select it here.  
   - If it’s not listed, it might be restricted due to **Teamspace permissions**.  

2️⃣ **Three Dots (`⋮`) Menu (Top Right Corner)**  
   - Click the **three dots (`⋮`)** at the top right of the Notion page.  
   - Scroll down to **"Connections"**.  
   - Select your **API integration** from the dropdown.  
   - This ensures the API has the correct **access to modify pages**.  

### **Step 4: Share the Page with the Integration**  
- Open the Notion page where you want to **generate your template**.  
- Click **Share → Invite** and **add your integration** (if needed).  
- This **grants API permission** to modify that page.  

### **Step 5: Install Dependencies**  
Run this in your terminal:  

```bash
pip install requests
```  

This installs the `requests` library, which we’ll use to **send API requests**.  

---  

## **2️⃣ Understanding Notion Page ID Formatting**  

There was some **confusion about Notion’s Page ID format**. Here’s the **correct way to get it**:  

1️⃣ Open your **target Notion page** in your browser.  
2️⃣ Copy the **URL** from the address bar.  
   Example:  
   ```
   https://www.notion.so/yourworkspace/Page-Name-1856236383b680ee877de0b6ee27ythu
   ```  
3️⃣ The **Page ID** is the last part:  
   ```
   1856236383b680ee877de0b6ee27ythu
   ```  

⚠️ **Important:** You don’t need to manually add dashes! When copied from the browser, the format is already correct for use in API requests.  

---  

## **3️⃣ Writing Your First Notion Template with Python**  

Now, let’s **write the script** to generate a structured Notion workspace.  

### **🚧 API Setup: Connecting to Notion**  
We start by defining our **API key** and **Notion Page ID**:  

```python
import requests

NOTION_API_KEY = "your_internal_integration_secret"
PARENT_PAGE_ID = "your_page_id"

url = "https://api.notion.com/v1/pages"
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}
```  

This is the **foundation** of every API request.  

---  

## **4️⃣ Structuring the Template**  

Let’s create a **structured workspace** that includes:  

✅ **A Dynamic Task Manager**  
📔 **A Daily Journal with Prompts**  
📆 **A Habit Tracker**  
🎯 **A Weekly Goal Tracker**  
📚 **A Knowledge Hub**  
🌺 **A Mood & Motivation Tracker**  

```python
payload = {
    "parent": {"page_id": PARENT_PAGE_ID},
    "properties": {
        "title": {
            "title": [{"text": {"content": "🌌 Versatile Calm & Intelligent Workspace"}}]
        }
    },
    "children": [
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"text": {"content": "🛠️ Task Manager"}}]}},
        {"object": "block", "type": "toggle", "toggle": {"rich_text": [{"text": {"content": "🎯 View or hide tasks"}}], "children": [
            {"object": "block", "type": "to_do", "to_do": {"rich_text": [{"text": {"content": "🌿 Plan my day"}}]}},
            {"object": "block", "type": "to_do", "to_do": {"rich_text": [{"text": {"content": "🔍 Research a topic"}}]}},
            {"object": "block", "type": "to_do", "to_do": {"rich_text": [{"text": {"content": "✍️ Journal entry"}}]}},
        ]}},
    ]
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("🌌 Notion template created successfully! 🎉")
else:
    print(f"Failed to create template: {response.text}")
```  

---  

## **🏆 Final Thoughts**  

By coding Notion templates, you’re **not just creating pages**—you’re **building a system that grows with you**.  

Now, it’s your turn. 🚀 What kind of **automated Notion setup** will you build?  
