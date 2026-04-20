# 📋 COM 103 Midterm: Group Project Task Tracker

---

## 📖 Overview

A command-line task monitoring tool built to solve the classic group project problem: **"Sino ang gagawa nito, at done na ba?"**

Instead of guessing who is doing what, this program acts as a lightweight digital task board. It allows a group to assign specific project phases to members and track their status. 

* **Logic:** It automatically calculates a weighted progress score based on completion.
* **Result:** It outputs a clean, formatted dashboard that instantly tells the team if they are **PROJECT READY!** or **NEEDS MORE WORK!**.

---

## ✨ Core Features

* **Dynamic Assignments:** Assign tasks with skip functionality for flexibility.
* **Weighted Points:** Automatically assigns points based on task status.
* **Progress Tracking:** Real-time percentage calculation.
* **Dashboard View:** Clean, terminal-based output for quick status checks.

---

## 🚀 How to Run

### Prerequisites
* Python 3.x installed on your machine.

### Execution Steps
1.  **Open Terminal:** Launch your command prompt (Git Bash, CMD, etc.).
2.  **Navigate to Folder:** ```bash
    cd com103-midterm-exam
    ```
3.  **Run Script:**
    ```bash
    python midterm_solution.py
    ```
4.  **Interact:** Follow the prompts to input project details and assign tasks.

---

## 📊 Scoring System

### Point Distribution
* ✅ **Done Task:** 2 Points
* ⏳ **Pending Task:** 1 Point

### Project Status Thresholds
* 🏆 **Progress ≥ 75%:** PROJECT READY!
* 📈 **Progress ≥ 50%:** ON TRACK.
* ⚠️ **Progress < 50%:** NEEDS MORE WORK!
