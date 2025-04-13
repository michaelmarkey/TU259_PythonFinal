import os
import json
import csv
import fitz
from dotenv import load_dotenv
from openai import OpenAI
from docx import Document
from odf.opendocument import OpenDocumentText
from odf.text import P

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- File Readers ----------
def read_txt_file(filepath):
    content = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content.extend(file.readlines())
    except Exception as e:
        content.append(f"Error reading .txt file: {e}\n")
    return content

def read_docx_file(filepath):
    content = []
    try:
        doc = Document(filepath)
        for para in doc.paragraphs:
            content.append(para.text + "\n")
    except Exception as e:
        content.append(f"Error reading .docx file: {e}\n")
    return content

def read_odt_file(filepath):
    content = []
    try:
        textdoc = OpenDocumentText(filepath)
        for element in textdoc.text.childNodes:
            if isinstance(element, P) and element.firstChild:
                content.append(element.firstChild.data + "\n")
    except Exception as e:
        content.append(f"Error reading .odt file: {e}\n")
    return content

def read_pdf_file(filepath):
    content = []
    try:
        doc = fitz.open(filepath)
        for page in doc:
            content.append(page.get_text() + "\n")
    except Exception as e:
        content.append(f"Error reading .pdf file: {e}\n")
    return content

# ---------- ChatGPT Parser ----------
def chatgpt_parse_job_profile(raw_text):
    prompt = f"""
You will be given a job description. Extract the following fields:
- Job Title
- Department
- Location
- Experience
- Skills (as a list)
- Responsibilities (as a list)
- Education (if mentioned)
- Languages (if mentioned)
- Certifications (if mentioned)
- Additional Requirements (anything not listed above)

Return ONLY the result as raw JSON, with no explanation, no markdown, and no formatting.

Job Description:
{raw_text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured data from job descriptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

# ---------- JobProfile Class ----------
class JobProfile:
    def __init__(self, data: dict):
        self.title = data.get("Job Title")
        self.department = data.get("Department")
        self.location = data.get("Location")
        self.experience = data.get("Experience")
        self.skills = data.get("Skills", [])
        self.responsibilities = data.get("Responsibilities", [])
        self.education = data.get("Education")
        self.languages = data.get("Languages")
        self.certifications = data.get("Certifications")
        self.additional_requirements = data.get("Additional Requirements")

    def display_summary(self):
        print(f"\n📌 Job Title: {self.title}")
        print(f"🏢 Department: {self.department}")
        print(f"📍 Location: {self.location}")
        print(f"🧑‍💼 Experience: {self.experience}")

        print("\n🛠️ Skills:")
        if isinstance(self.skills, list):
            for skill in self.skills:
                print(f"  • {skill}")
        else:
            print(f"  {self.skills}")

        print("\n📋 Responsibilities:")
        if isinstance(self.responsibilities, list):
            for r in self.responsibilities:
                print(f"  • {r}")
        else:
            print(f"  {self.responsibilities}")

        print(f"\n🎓 Education: {self.education}")
        print(f"🗣️ Languages: {self.languages}")
        print(f"📜 Certifications: {self.certifications}")
        print(f"➕ Additional Requirements: {self.additional_requirements}")

    def to_dict(self):
        return {
            "Job Title": self.title,
            "Department": self.department,
            "Location": self.location,
            "Experience": self.experience,
            "Skills": self.skills,
            "Responsibilities": self.responsibilities,
            "Education": self.education,
            "Languages": self.languages,
            "Certifications": self.certifications,
            "Additional Requirements": self.additional_requirements
        }

    def to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        print(f"✅ Saved to JSON: {filename}")

    def to_csv(self, filename):
        data = self.to_dict()
        for key in data:
            if isinstance(data[key], list):
                data[key] = ", ".join(data[key])
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print(f"✅ Saved to CSV: {filename}")

# ---------- MAIN ----------
if __name__ == "__main__":
    print("Choose the file type to open:")
    print("1 - TXT\n2 - DOCX\n3 - ODT\n4 - PDF")
    choice = input("Enter a number (1-4): ").strip()

    file_base = input("Enter the base file name (without extension): ").strip()
    extension_map = {"1": ".txt", "2": ".docx", "3": ".odt", "4": ".pdf"}
    extension = extension_map.get(choice)

    if not extension:
        print("❌ Invalid choice.")
        exit()

    file_path = os.path.abspath(file_base + extension)
    print(f"\n🔎 Looking for file: {file_path}")

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        exit()
    else:
        print(f"📂 File found: {file_path}")

    # Read file content
    if choice == "1":
        full_content = read_txt_file(file_path)
    elif choice == "2":
        full_content = read_docx_file(file_path)
    elif choice == "3":
        full_content = read_odt_file(file_path)
    elif choice == "4":
        full_content = read_pdf_file(file_path)

    raw_text = "".join(full_content)

    # Send to ChatGPT
    print("\n🧠 Sending job profile to ChatGPT for parsing...")
    parsed_json = chatgpt_parse_job_profile(raw_text)

    # Save raw response (for debugging)
    with open("job_profile_parsed.json", "w", encoding="utf-8") as f:
        f.write(parsed_json)

    parsed_json = parsed_json.strip()

    if not parsed_json:
        print("❌ No response received from ChatGPT.")
        exit()

    try:
        parsed_data = json.loads(parsed_json)
    except json.JSONDecodeError as e:
        print("❌ Failed to parse JSON response.")
        print("Error:", e)
        print("Raw response was:\n", parsed_json)
        exit()

    # Create JobProfile
    job = JobProfile(parsed_data)

    # Auto-save to JSON and CSV
    job.to_json("job_profile_output.json")
    job.to_csv("job_profile_output.csv")

    # Ask user if they want to display the summary
    show = input("\n👀 Do you want to display the summary on screen? (y/n): ").strip().lower()
    if show == "y":
        job.display_summary()
    else:
        print("✅ Done. Output saved to CSV and JSON.")
