import time
from datetime import datetime

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

# STUDENTS' DATABASE
students = {
    "2023-001": {"name": "Mendez, Acee Zai L.", "parent_number": "09171255567"},
    "2023-002": {"name": "Esta, Divina May L.", "parent_number": "09981234777"},
    "2023-003": {"name": "Mendez, Zoe L.", "parent_number": "09976301546"}
}

def header():
    print(CYAN + "     PUP STUDENT ATTENDANCE SYSTEM        " + RESET)

def loading(text):
    print(YELLOW + text + RESET, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()

def save_log(student_num, name, status, time_now):
    date_today = datetime.now().strftime("%Y-%m-%d")
    with open("attendance_log.txt", "a") as file:
        file.write(f"{date_today} | {time_now} | {student_num} | {name} | {status.upper()}\n")

def send_sms(name, number, time_now, status):
    print(GREEN + f"\nMessage sent to {number}:" + RESET)
    print(
        f"Your son/daughter, {name}, {status} Polytechnic University of the Philippines at exactly {time_now}."
    )

def attendance(status):
    header()
    student_num = input(YELLOW + "Enter Student Number: " + RESET)

    if student_num in students:
        name = students[student_num]["name"]
        number = students[student_num]["parent_number"]
        time_now = datetime.now().strftime("%I:%M %p")

        loading("Recording attendance")
        print(GREEN + f"\n✓ {status.upper()} recorded for {name}!" + RESET)

        loading("Sending message to parent")
        send_sms(name, number, time_now, status)

        save_log(student_num, name, status, time_now)

    else:
        print(RED + "\n× Student Number not found!" + RESET)

def view_logs():
    header()
    print(MAGENTA + "Attendance Logs:\n" + RESET)

    try:
        with open("attendance_log.txt", "r") as file:
            logs = file.readlines()

            if len(logs) == 0:
                print(YELLOW + "No logs yet." + RESET)
                return

            print(CYAN + "DATE       | TIME     | STUDENT NO. | NAME                     | STATUS" + RESET)
            print(CYAN + "-" * 78 + RESET)

            for log in logs:
                print(log.rstrip())

    except FileNotFoundError:
        print(YELLOW + "No logs found." + RESET)

while True:
    header()
    print(YELLOW + "[1] Student Time IN")
    print("[2] Student Time OUT")
    print("[3] View Attendance Logs")
    print("[4] Exit" + RESET)

    choice = input(CYAN + "\nSelect an option: " + RESET)

    if choice == "1":
        attendance("entered")
    elif choice == "2":
        attendance("exited")
    elif choice == "3":
        view_logs()
    elif choice == "4":
        print(GREEN + "\nThank you for using the system!" + RESET)
        break
    else:
        print(RED + "\nInvalid choice! Please try again." + RESET)

    input(YELLOW + "\nPress Enter to return to menu..." + RESET)
    