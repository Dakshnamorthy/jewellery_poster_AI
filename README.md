# Jewellery Poster AI  
### Agentic AI System for Automated Jewellery Social Media Posters

---

## Project Overview

**Jewellery Poster AI** is an end-to-end **Agentic AI-based automation tool** designed to help jewellery shops generate **professional social media posters** automatically based on **live gold and silver price trends**.

The system runs **three times a day** (morning, afternoon, evening), analyzes price movements, decides marketing strategy, designs posters, generates captions, and presents them to the shop owner through a **human-in-the-loop approval dashboard** before posting.

This project demonstrates how **Agentic AI**, automation, and human control can be combined to solve a real-world business problem.

---

## Problem Statement

Jewellery businesses post daily gold and silver prices on social media to attract customers.  
Currently, this process is:

- Manual
- Time-consuming
- Inconsistent in design
- Dependent on human availability

**Goal:**  
Automate the poster creation process while still allowing the business owner to **approve or reject** content before posting.

---

## Key Features

-  **Automated Execution (3× Daily)**
  - Morning (10:00 AM)
  - Afternoon (3:00 PM)
  - Evening (7:00 PM)

-  **Agentic AI Pipeline**
  - Price Trend Analysis
  - Strategy Decision
  - Design Decision
  - Caption Generation

-  **Automatic Poster Generation**
  - Dynamic layouts
  - Multiple fonts
  - Product & background images

-  **Human-in-the-Loop Approval**
  - Approve or reject posters via web dashboard
  - Instant regeneration on rejection

-  **Ready-to-Post Output**
  - Poster image
  - Caption text
  - Hashtags
  - No paid tools required

-  **Completely Free & Local**
  - No paid APIs
  - No cloud dependency

---

##  Agentic AI Architecture

The system is built using **multiple specialized agents**, each responsible for a specific decision.

### Agents Used

| Agent | Responsibility |
|------|---------------|
| Price Trend Agent | Analyzes gold price movement |
| Strategy Agent | Decides marketing tone (offer, announcement, calm) |
| Design Agent | Selects poster layout & style |
| Caption Agent | Generates caption & hashtags |
| Approval Agent | Handles human approval & regeneration logic |

This modular design makes the system **explainable, scalable, and controllable**.

---

##  System Workflow

Scheduled Time Trigger
↓
Fetch Gold & Silver Prices
↓
Agentic AI Decision Pipeline
↓
Poster + Caption Generated
↓
Approval Dashboard (Flask)
↓
Approve → Ready to Post
Reject → Regenerate Poster


---

##  Technology Stack

- **Programming Language:** Python 3.12
- **Web Framework:** Flask
- **Image Processing:** Pillow (PIL)
- **Automation:** Windows Task Scheduler
- **Architecture:** Agentic AI + Human-in-the-loop
- **Frontend:** HTML & CSS (No frameworks)

---

---

##  Automation Setup

The system uses **Windows Task Scheduler** to run automatically:

| Time | Command |
|----|----|
| 10:00 AM | `python run_slot.py morning` |
| 3:00 PM | `python run_slot.py afternoon` |
| 7:00 PM | `python run_slot.py evening` |

Each run generates a fresh poster and updates the approval dashboard.

---

## Approval Dashboard

- Built using Flask
- Displays the latest generated poster
- Two actions:
  - ✅ **Approve** – Poster is finalized for posting
  - ❌ **Reject** – New poster is generated instantly
- No page redirection (smooth UX)

---

## Social Media Posting Strategy

This project follows a **manual-posting-ready** approach:

- After approval, poster & caption are saved in `ready_to_post/`
- Jewellery owner uploads content to Instagram / Facebook manually

> This approach is safe, realistic, and widely used by businesses.

(Automatic posting using platform APIs can be added in future versions.)

---

## Academic Value

This project demonstrates:

- Agentic AI concepts
- Multi-agent coordination
- Human-in-the-loop systems
- Automation & scheduling
- Real-world business application
- Ethical AI control

---

## Future Enhancements

- Automatic Instagram & Facebook posting (Meta Graph API)
- Multiple shop profiles
- Analytics dashboard
- Mobile-friendly UI
- Cloud deployment

---

## Conclusion

**Jewellery Poster AI** is a complete, practical example of how **Agentic AI** can be applied to solve real-world business problems with automation and human control.

This project goes beyond simple AI generation by incorporating:
- Decision-making agents
- Feedback loops
- Safety mechanisms
- Professional workflow design

---



