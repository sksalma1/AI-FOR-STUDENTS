import tkinter as tk
from tkinter import messagebox
import webbrowser

# Create main window
root = tk.Tk()
root.title("Exam Chatbot")

# Set background color
root.configure(bg='#fffff0')

# Add a heading for all the buttons
heading_label = tk.Label(root, text="Select Your Competitive Exam", font=("Helvetica", 14, "bold"), bg='#f0f0f0')
heading_label.pack(pady=10, anchor='w')

# Function to handle button clicks
def button_click(topic):
    hide_buttons()
    if topic == "GRE":
        show_gre_options()
    elif topic == "TOEFL":
        show_tofel_options()
    elif topic == "IELTS":
        show_ielts_options()
    elif topic == "GATE":
        show_gate_options()
    elif topic == "JEE MAINS":
        show_jeemains_options()
    elif topic == "NEET":
        show_neet_options()
    elif topic == "SSC":
        show_ssc_options()
    elif topic == "EAMCET":
        show_eamcet_options()
    else:
        messagebox.showinfo("Chatbot", f"You clicked {topic}.")

# Function to show GRE specific options
def show_gre_options():
    gre_buttons_frame.pack()

# Function to show TOEFL specific options
def show_tofel_options():
    tofel_buttons_frame.pack()

# Function to show IELTS specific options
def show_ielts_options():
    ielts_buttons_frame.pack()

# Function to show GATE specific options
def show_gate_options():
    gate_buttons_frame.pack()

# Function to show JEE MAINS specific options
def show_jeemains_options():
    jeemains_buttons_frame.pack()

# Function to show NEET specific options
def show_neet_options():
    neet_buttons_frame.pack()

# Function to show SSC specific options
def show_ssc_options():
    ssc_buttons_frame.pack()

# Function to show EAMCET specific options
def show_eamcet_options():
    eamcet_buttons_frame.pack()

# Function to hide all buttons
def hide_buttons():
    gre_buttons_frame.pack_forget()
    tofel_buttons_frame.pack_forget()
    ielts_buttons_frame.pack_forget()
    gate_buttons_frame.pack_forget()
    jeemains_buttons_frame.pack_forget()
    neet_buttons_frame.pack_forget()
    ssc_buttons_frame.pack_forget()
    eamcet_buttons_frame.pack_forget()

# Function to handle GRE specific button clicks
def gre_button_click(option):
    if option == "Books":
        webbrowser.open("https://www.upgradabroad.com/ebooks/gre-guide-7")
    elif option == "Mock Tests":
        webbrowser.open("https://www.studies-overseas.com/test-prep/gre-coaching?utm_source=google-ads&utm_medium=search-ads&utm_campaign=GRE-Online-Batch-Search&utm_id=GRE-Online-Batch-Search&matchtype=b&device=c&devicemodel=&keyword=gre%20course&campaignid=20451972859&adgroupid=152691098095&extensionid=&network=g&gad_source=1&gclid=CjwKCAiA8sauBhB3EiwAruTRJmGCqzqP1yQlubI25bmOsAJcDEqdC7C3ocyh1M4RBbdirJyCmhzHDRoCwYIQAvD_BwE")
    elif option == "Previous Year Papers":
        webbrowser.open("https://www.shiksha.com/studyabroad/exams/gre/sample-papers")

# Function to handle TOEFL specific button clicks
def tofel_button_click(option):
    if option == "Books":
        webbrowser.open("https://www.upgradabroad.com/ebooks/toefl-guide-17")
    elif option == "Mock Tests":
        webbrowser.open("https://www.bestmytest.com/toefl/practice-test")
    elif option == "Previous Year Papers":
        webbrowser.open("https://entrance-exam.net/toefl-papers/")

# Function to handle IELTS specific button clicks
def ielts_button_click(option):
    if option == "Books":
        webbrowser.open("https://www.ieltsforfree.com/download-your-ielts-ebooks/")
    elif option == "Mock Tests":
        webbrowser.open("https://www.bestmytest.com/ielts/test?gad_source=1&gclid=CjwKCAiA8sauBhB3EiwAruTRJkox71Sbb9t0BO8D8j62qPrAdGnUGjKpogqhgtrUH1_0Dg8rcBO-7xoCdZ0QAvD_BwE")
    elif option == "Previous Year Papers":
        webbrowser.open("https://www.shiksha.com/studyabroad/exams/ielts/sample-papers")

# Function to handle GATE specific button clicks
def gate_button_click(option):
    if option == "Books":
        webbrowser.open("https://www.gatexplore.com/study-material/")
    elif option == "Mock Tests":
        webbrowser.open("https://oswaalbooks.com/pages/gate-mock-test-sample-paper")
    elif option == "Previous Year Papers":
        webbrowser.open("https://byjus.com/gate/previous-year-question-papers/")

# Function to handle JEE MAINS specific button clicks
def jee_button_click(option):
    if option == "Books":
        webbrowser.open("https://unacademy.com/content/jee/notification/jee-preparation-books/")
    elif option == "Mock Tests":
        webbrowser.open("https://nta.ac.in/Student")
    elif option == "Previous Year Papers":
        webbrowser.open("https://www.shiksha.com/engineering/jee-main-exam-question-papers")

# Function to handle NEET specific button clicks
def neet_button_click(option):
    if option == "Books":
        webbrowser.open("https://www.neetprep.com/ncert-book-pdf")
    elif option == "Mock Tests":
        webbrowser.open("https://www.neetprep.com/papers-test-series")
    elif option == "Previous Year Papers":
        webbrowser.open("https://byjus.com/neet/neet-question-papers/")

# Function to handle EAMCET specific button clicks
def eamcet_button_click(option):
    if option == "Books":
        webbrowser.open("https://engineering.careers360.com/download/ap-eamcet-ebooks")
    elif option == "Mock Tests":
        webbrowser.open("https://www.manabadi.co.in/entrance-Exams/eamcet-mock-test-free-online-eamcet-mock-tests-for-courses-in-engineering-and-agriculture.asp")
    elif option == "Previous Year Papers":
        webbrowser.open("https://www.embibe.com/exams/ap-eamcet-previous-year-papers/")

# Function to handle SSC specific button clicks
def ssc_button_click(option):
    if option == "Books":
        webbrowser.open("https://www.apteacher.net/10thclass-textbooks/10thclass-textbooks-2022-ap-scert-download-pdf")
    elif option == "Previous Year Papers":
        webbrowser.open("https://byjus.com/ap-board/ap-ssc-previous-question-papers/")

# Create buttons for various exam topics
topics = ["JEE MAINS", "NEET", "GRE", "TOEFL", "IELTS", "SSC", "GATE", "EAMCET"]
buttons = []
for topic in topics:
    button = tk.Button(root, text=topic, command=lambda t=topic: button_click(t), bg='#ffffff')
    button.pack(pady=5, anchor='w', padx=10)
    buttons.append(button)

# Frame to hold GRE specific options
gre_buttons_frame = tk.Frame(root, bg='#f0f0f0')

# GRE specific buttons
gre_books_button = tk.Button(gre_buttons_frame, text="Books", command=lambda: gre_button_click("Books"), bg='#ffffff')
gre_books_button.pack(pady=5, anchor='w', padx=10)

gre_mock_tests_button = tk.Button(gre_buttons_frame, text="Mock Tests", command=lambda: gre_button_click("Mock Tests"), bg='#ffffff')
gre_mock_tests_button.pack(pady=5, anchor='w', padx=10)

gre_prev_year_papers_button = tk.Button(gre_buttons_frame, text="Previous Year Papers", command=lambda: gre_button_click("Previous Year Papers"), bg='#ffffff')
gre_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold TOEFL specific options
tofel_buttons_frame = tk.Frame(root, bg='#f0f0f0')

# TOEFL specific buttons
tofel_books_button = tk.Button(tofel_buttons_frame, text="Books", command=lambda: tofel_button_click("Books"), bg='#ffffff')
tofel_books_button.pack(pady=5, anchor='w', padx=10)

tofel_mock_tests_button = tk.Button(tofel_buttons_frame, text="Mock Tests", command=lambda: tofel_button_click("Mock Tests"), bg='#ffffff')
tofel_mock_tests_button.pack(pady=5, anchor='w', padx=10)

tofel_prev_year_papers_button = tk.Button(tofel_buttons_frame, text="Previous Year Papers", command=lambda: tofel_button_click("Previous Year Papers"), bg='#ffffff')
tofel_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold IELTS specific options
ielts_buttons_frame = tk.Frame(root, bg='#f0f0f0')

# IELTS specific buttons
ielts_books_button = tk.Button(ielts_buttons_frame, text="Books", command=lambda: ielts_button_click("Books"), bg='#ffffff')
ielts_books_button.pack(pady=5, anchor='w', padx=10)

ielts_mock_tests_button = tk.Button(ielts_buttons_frame, text="Mock Tests", command=lambda: ielts_button_click("Mock Tests"), bg='#ffffff')
ielts_mock_tests_button.pack(pady=5, anchor='w', padx=10)

ielts_prev_year_papers_button = tk.Button(ielts_buttons_frame, text="Previous Year Papers", command=lambda: ielts_button_click("Previous Year Papers"), bg='#ffffff')
ielts_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold GATE specific options
gate_buttons_frame = tk.Frame(root, bg='#f0f0f0')

# GATE specific buttons
gate_books_button = tk.Button(gate_buttons_frame, text="Books", command=lambda: gate_button_click("Books"), bg='#ffffff')
gate_books_button.pack(pady=5, anchor='w', padx=10)

gate_mock_tests_button = tk.Button(gate_buttons_frame, text="Mock Tests", command=lambda: gate_button_click("Mock Tests"), bg='#ffffff')
gate_mock_tests_button.pack(pady=5, anchor='w', padx=10)

gate_prev_year_papers_button = tk.Button(gate_buttons_frame, text="Previous Year Papers", command=lambda: gate_button_click("Previous Year Papers"), bg='#ffffff')
gate_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold JEE MAINS specific options
jeemains_buttons_frame = tk.Frame(root, bg='#f0f0f0')

jee_books_button = tk.Button(jeemains_buttons_frame, text="Books", command=lambda: jee_button_click("Books"), bg='#ffffff')
jee_books_button.pack(pady=5, anchor='w', padx=10)

jee_mock_tests_button = tk.Button(jeemains_buttons_frame, text="Mock Tests", command=lambda: jee_button_click("Mock Tests"), bg='#ffffff')
jee_mock_tests_button.pack(pady=5, anchor='w', padx=10)

jee_prev_year_papers_button = tk.Button(jeemains_buttons_frame, text="Previous Year Papers", command=lambda: jee_button_click("Previous Year Papers"), bg='#ffffff')
jee_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold NEET specific options
neet_buttons_frame = tk.Frame(root, bg='#f0f0f0')

neet_books_button = tk.Button(neet_buttons_frame, text="Books", command=lambda: neet_button_click("Books"), bg='#ffffff')
neet_books_button.pack(pady=5, anchor='w', padx=10)

neet_mock_tests_button = tk.Button(neet_buttons_frame, text="Mock Tests", command=lambda: neet_button_click("Mock Tests"), bg='#ffffff')
neet_mock_tests_button.pack(pady=5, anchor='w', padx=10)

neet_prev_year_papers_button = tk.Button(neet_buttons_frame, text="Previous Year Papers", command=lambda: neet_button_click("Previous Year Papers"), bg='#ffffff')
neet_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold SSC specific options
ssc_buttons_frame = tk.Frame(root, bg='#f0f0f0')

ssc_books_button = tk.Button(ssc_buttons_frame, text="Books", command=lambda: ssc_button_click("Books"), bg='#ffffff')
ssc_books_button.pack(pady=5, anchor='w', padx=10)

ssc_prev_year_papers_button = tk.Button(ssc_buttons_frame, text="Previous Year Papers", command=lambda: ssc_button_click("Previous Year Papers"), bg='#ffffff')
ssc_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Frame to hold EAMCET specific options
eamcet_buttons_frame = tk.Frame(root, bg='#f0f0f0')

eamcet_books_button = tk.Button(eamcet_buttons_frame, text="Books", command=lambda: eamcet_button_click("Books"), bg='#ffffff')
eamcet_books_button.pack(pady=5, anchor='w', padx=10)

eamcet_mock_tests_button = tk.Button(eamcet_buttons_frame, text="Mock Tests", command=lambda: eamcet_button_click("Mock Tests"), bg='#ffffff')
eamcet_mock_tests_button.pack(pady=5, anchor='w', padx=10)

eamcet_prev_year_papers_button = tk.Button(eamcet_buttons_frame, text="Previous Year Papers", command=lambda: eamcet_button_click("Previous Year Papers"), bg='#ffffff')
eamcet_prev_year_papers_button.pack(pady=5, anchor='w', padx=10)

# Function to handle closing the window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Hide all specific options initially
hide_buttons()

# Start the main loop
root.mainloop()