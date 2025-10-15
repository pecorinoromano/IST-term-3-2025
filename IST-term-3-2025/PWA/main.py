from flask import Flask, jsonify, render_template, request, redirect, url_for
import database_manager as dbHandler
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# HOME PAGE (My Day)
# -----------------------------
@app.route("/")
@app.route("/index.html")
def index():
    try:
        reminders = dbHandler.listReminders()
        print(f"[DEBUG] Loaded {len(reminders)} reminders for homepage")
    except Exception as e:
        print("[ERROR] Could not load reminders:", e)
        reminders = []
    return render_template("index.html", reminders=reminders)


# -----------------------------
# TASKS PAGE
# -----------------------------
@app.route("/tasks.html", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        due_date = request.form["due_date"]
        dbHandler.addReminder(title, description, due_date)
        return redirect(url_for("tasks"))

    reminders = dbHandler.listReminders()
    return render_template("tasks.html", reminders=reminders)


# -----------------------------
# LISTS PAGE
# -----------------------------
@app.route("/lists", methods=["GET", "POST"])
def lists():
    if request.method == "POST":
        list_name = request.form["list_name"]
        dbHandler.addList(list_name)
        return redirect(url_for("lists"))

    all_lists = dbHandler.listLists()
    return render_template("lists.html", lists=all_lists)


# -----------------------------
# DELETE LIST
# -----------------------------
@app.route("/delete_list/<int:list_id>", methods=["POST"])
def delete_list(list_id):
    try:
        dbHandler.deleteList(list_id)  # we will add this function in database_manager.py
        return jsonify({"success": True})
    except Exception as e:
        print("Error deleting list:", e)
        return jsonify({"success": False, "error": str(e)})


# -----------------------------
# CALENDAR PAGE
# -----------------------------
@app.route("/calendar.html")
def calendar():
    reminders = dbHandler.listReminders()
    return render_template("calendar.html", reminders=reminders)


# -----------------------------
# COMPLETE REMINDER
# -----------------------------
@app.route("/complete/<int:reminder_id>", methods=["POST"])
def complete(reminder_id):
    dbHandler.completeReminder(reminder_id)
    return jsonify({"success": True})


# -----------------------------
# DELETE REMINDER
# -----------------------------
@app.route("/delete/<int:reminder_id>", methods=["POST"])
def delete(reminder_id):
    try:
        dbHandler.deleteReminder(reminder_id)
        return jsonify({"success": True})
    except Exception as e:
        print("Error deleting reminder:", e)
        return jsonify({"success": False, "error": str(e)})


# -----------------------------
# MAIN ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
