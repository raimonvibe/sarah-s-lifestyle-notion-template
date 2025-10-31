#!/usr/bin/env python3
"""
🌌 Sarah's Notion Template Generator
Automates the creation of a comprehensive life design template in Notion.

This script creates a comprehensive life design workspace with:
- The Ultimate Habit Tracker
- The Ultimate Goal Tracker
- My Weekly Review
- Bookshelf Tracker
- Student Tracker
"""

import requests
import os
from typing import Dict, List, Any


class NotionTemplateGenerator:
    """A class to generate Notion workspace templates via the Notion API."""
    
    def __init__(self, api_key: str, parent_page_id: str):
        """
        Initialize the Notion Template Generator.
        
        Args:
            api_key: Your Notion Internal Integration Secret
            parent_page_id: The ID of the Notion page where the template will be created
        """
        self.api_key = api_key
        self.parent_page_id = parent_page_id
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
    
    def create_page(self, title: str, children: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create a new Notion page with specified title and children blocks.
        
        Args:
            title: The title of the page
            children: List of block objects to include in the page
            
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/pages"
        payload = {
            "parent": {"page_id": self.parent_page_id},
            "properties": {
                "title": {
                    "title": [{"text": {"content": title}}]
                }
            },
            "children": children
        }
        
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json() if response.status_code == 200 else response
    
    def create_heading(self, level: int, content: str) -> Dict[str, Any]:
        """Create a heading block."""
        heading_type = f"heading_{level}"
        return {
            "object": "block",
            "type": heading_type,
            heading_type: {
                "rich_text": [{"text": {"content": content}}]
            }
        }
    
    def create_todo(self, content: str, checked: bool = False) -> Dict[str, Any]:
        """Create a to-do block."""
        return {
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"text": {"content": content}}],
                "checked": checked
            }
        }
    
    def create_toggle(self, content: str, children: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a toggle block with optional children."""
        toggle = {
            "object": "block",
            "type": "toggle",
            "toggle": {
                "rich_text": [{"text": {"content": content}}]
            }
        }
        if children:
            toggle["toggle"]["children"] = children
        return toggle
    
    def create_paragraph(self, content: str) -> Dict[str, Any]:
        """Create a paragraph block."""
        return {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"text": {"content": content}}]
            }
        }
    
    def create_bulleted_list(self, items: List[str]) -> List[Dict[str, Any]]:
        """Create a list of bulleted list items."""
        return [
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"text": {"content": item}}]
                }
            }
            for item in items
        ]
    
    def create_numbered_list(self, items: List[str]) -> List[Dict[str, Any]]:
        """Create a list of numbered list items."""
        return [
            {
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [{"text": {"content": item}}]
                }
            }
            for item in items
        ]
    
    def create_dividing_line(self) -> Dict[str, Any]:
        """Create a divider block."""
        return {
            "object": "block",
            "type": "divider",
            "divider": {}
        }
    
    def build_complete_template(self) -> List[Dict[str, Any]]:
        """Build the complete Life Design workspace template structure."""
        children = []
        
        # Welcome Section
        children.append(self.create_paragraph("Welcome to your Life Design Dashboard! ✨"))
        children.append(self.create_paragraph("This template helps you track habits, set goals, plan your week, and organize your reading."))
        children.append(self.create_dividing_line())
        
        # The Ultimate Habit Tracker Section
        children.append(self.create_heading(1, "The Ultimate Habit Tracker"))
        children.append(self.create_paragraph("Track your daily habits and build consistency. Check off each habit as you complete it."))
        children.append(self.create_paragraph(""))
        
        # Daily Habits
        daily_habits = [
            "Morning routine",
            "Exercise / Physical activity",
            "Read for 30 minutes",
            "Meditation / Mindfulness",
            "Healthy meals",
            "Evening routine",
            "Journal entry",
            "Gratitude practice"
        ]
        children.append(self.create_heading(2, "Daily Habits"))
        for habit in daily_habits:
            children.append(self.create_todo(habit))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("Weekly Habits"))
        weekly_habits = [
            "Deep work session",
            "Social connection",
            "Learning / Skill development",
            "Rest day / Self-care",
            "Review and plan"
        ]
        for habit in weekly_habits:
            children.append(self.create_todo(habit))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("💡 Tip: Focus on consistency over perfection. Track what matters most to you."))
        children.append(self.create_dividing_line())
        
        # The Ultimate Goal Tracker Section
        children.append(self.create_heading(1, "The Ultimate Goal Tracker"))
        children.append(self.create_paragraph("Set meaningful goals and track your progress. Break down big goals into actionable steps."))
        children.append(self.create_paragraph(""))
        
        # Goal Categories
        children.append(self.create_heading(2, "Long-term Goals (3-12 months)"))
        children.append(self.create_paragraph("Goal: [Describe your long-term goal]"))
        children.append(self.create_paragraph("Deadline: [Set your target date]"))
        children.append(self.create_paragraph("Milestones:"))
        children.extend(self.create_bulleted_list([
            "[First milestone]",
            "[Second milestone]",
            "[Third milestone]"
        ]))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_heading(2, "Short-term Goals (1-3 months)"))
        children.append(self.create_paragraph("Goal: [Describe your short-term goal]"))
        children.append(self.create_paragraph("Actions:"))
        children.extend(self.create_bulleted_list([
            "[Action item 1]",
            "[Action item 2]",
            "[Action item 3]"
        ]))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_heading(2, "This Month's Focus"))
        children.append(self.create_todo("Priority 1: [Your main focus for this month]"))
        children.append(self.create_todo("Priority 2: [Secondary focus]"))
        children.append(self.create_todo("Priority 3: [Third focus]"))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("Progress Notes:"))
        children.append(self.create_paragraph("Track your wins, challenges, and learnings here..."))
        children.append(self.create_dividing_line())
        
        # My Weekly Review Section
        children.append(self.create_heading(1, "My Weekly Review"))
        children.append(self.create_paragraph("Use this section to reflect on your week and plan ahead."))
        children.append(self.create_paragraph(""))
        
        children.append(self.create_heading(2, "Week of [Date Range]"))
        children.append(self.create_paragraph(""))
        
        # Weekly Review Prompts
        children.append(self.create_heading(3, "Reflection"))
        reflection_questions = [
            "What were my biggest wins this week?",
            "What challenges did I face?",
            "What did I learn?",
            "What am I grateful for?",
            "How did I feel overall?"
        ]
        for question in reflection_questions:
            children.append(self.create_paragraph(question))
            children.append(self.create_paragraph(""))
        
        children.append(self.create_heading(3, "Planning"))
        children.append(self.create_paragraph("Top 3 priorities for next week:"))
        children.append(self.create_todo("Priority 1: [Your main focus]"))
        children.append(self.create_todo("Priority 2: [Secondary focus]"))
        children.append(self.create_todo("Priority 3: [Third focus]"))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("Key events & deadlines:"))
        children.append(self.create_bulleted_list([
            "[Add important dates and events]"
        ]))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("Notes for next week:"))
        children.append(self.create_paragraph("..."))
        children.append(self.create_dividing_line())
        
        # Bookshelf Tracker Section
        children.append(self.create_heading(1, "Bookshelf Tracker"))
        children.append(self.create_paragraph("Keep track of all your books in one place - what you're reading, want to read, and have completed."))
        children.append(self.create_paragraph(""))
        
        # Reading Status Sections
        children.append(self.create_heading(2, "Currently Reading"))
        children.append(self.create_toggle(
            "📖 [Book Title] by [Author]",
            [
                self.create_paragraph("Progress: [Current page/chapter]"),
                self.create_paragraph("Started: [Date]"),
                self.create_paragraph("Notes: [Your thoughts and insights]")
            ]
        ))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_heading(2, "Want to Read"))
        want_to_read = [
            "📚 [Book Title] by [Author] - [Why you want to read it]",
            "📚 [Book Title] by [Author] - [Why you want to read it]",
            "📚 [Book Title] by [Author] - [Why you want to read it]"
        ]
        children.extend(self.create_bulleted_list(want_to_read))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_heading(2, "Completed"))
        completed_books = [
            "✅ [Book Title] by [Author] - Finished: [Date]",
            "Rating: ⭐⭐⭐⭐⭐",
            "Key Takeaways: [Your main learnings]"
        ]
        for item in completed_books:
            children.append(self.create_paragraph(item))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("💡 Tip: Use this tracker to build your reading habit and remember key insights from books you've read."))
        children.append(self.create_dividing_line())
        
        # Student Tracker Section
        children.append(self.create_heading(1, "Student Tracker"))
        children.append(self.create_paragraph("Organize your academic life - track courses, assignments, deadlines, and study sessions."))
        children.append(self.create_paragraph(""))
        
        # Current Courses
        children.append(self.create_heading(2, "Current Courses"))
        children.append(self.create_toggle(
            "📚 [Course Name]",
            [
                self.create_paragraph("Instructor: [Professor Name]"),
                self.create_paragraph("Schedule: [Days/Times]"),
                self.create_paragraph("Credits: [Number]"),
                self.create_paragraph(""),
                self.create_paragraph("Assignments:"),
                self.create_todo("[Assignment 1] - Due: [Date]"),
                self.create_todo("[Assignment 2] - Due: [Date]"),
                self.create_paragraph(""),
                self.create_paragraph("Notes: [Your notes about the course]")
            ]
        ))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_heading(2, "Upcoming Deadlines"))
        upcoming_deadlines = [
            "[Assignment/Exam Name] - Due: [Date] - [Course]",
            "[Assignment/Exam Name] - Due: [Date] - [Course]",
            "[Assignment/Exam Name] - Due: [Date] - [Course]"
        ]
        children.extend(self.create_bulleted_list(upcoming_deadlines))
        
        children.append(self.create_paragraph(""))
        children.append(self.create_heading(2, "Study Sessions"))
        children.append(self.create_paragraph("Track your study time and topics:"))
        study_session = [
            "Date: [Date]",
            "Duration: [Hours]",
            "Subject/Topic: [What you studied]",
            "Notes: [Key learnings or concepts]"
        ]
        for item in study_session:
            children.append(self.create_paragraph(item))
        children.append(self.create_paragraph(""))
        
        children.append(self.create_heading(2, "Grades & Progress"))
        children.append(self.create_paragraph("Course: [Course Name]"))
        children.append(self.create_paragraph("Current Grade: [Grade/Percentage]"))
        children.append(self.create_paragraph("Target Grade: [Your goal]"))
        children.append(self.create_paragraph(""))
        children.append(self.create_paragraph("💡 Tip: Update this regularly to stay on top of your academic goals and track your progress."))
        
        return children
    
    def generate_template(self) -> bool:
        """
        Generate the complete workspace template.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            children = self.build_complete_template()
            response = self.create_page(
                "Sarah's Life Design Dashboard",
                children
            )
            
            if isinstance(response, dict) and response.get("object") == "page":
                print("✨ Sarah's Notion Template created successfully! 🎉")
                print(f"Page ID: {response.get('id', 'N/A')}")
                print(f"Page URL: {response.get('url', 'N/A')}")
                return True
            else:
                print(f"❌ Failed to create template:")
                print(f"Status: {response.get('status', 'Unknown')}")
                print(f"Error: {response.get('message', response)}")
                return False
                
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")
            return False


def main():
    """Main function to run the Notion template generator."""
    # Try to load from environment variables first
    api_key = os.getenv("NOTION_API_KEY")
    parent_page_id = os.getenv("NOTION_PARENT_PAGE_ID")
    
    # If not in environment, prompt user
    if not api_key:
        api_key = input("Enter your Notion API Key (Internal Integration Secret): ").strip()
    
    if not parent_page_id:
        parent_page_id = input("Enter your Notion Parent Page ID: ").strip()
    
    if not api_key or not parent_page_id:
        print("❌ Both API key and Parent Page ID are required.")
        print("\n📖 How to get these:")
        print("1. API Key: Go to https://www.notion.so/my-integrations")
        print("2. Page ID: Extract from your Notion page URL (the last part after the page name)")
        return
    
    # Create generator and build template
    generator = NotionTemplateGenerator(api_key, parent_page_id)
    generator.generate_template()


if __name__ == "__main__":
    main()

