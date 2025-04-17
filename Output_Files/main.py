import os
import json
import csv
import fitz
from dotenv import load_dotenv
from openai import OpenAI
from docx import Document
from odf.opendocument import load
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
        textdoc = load(filepath)
        paragraphs = textdoc.getElementsByType(P)
        for para in paragraphs:
            text_nodes = para.childNodes
            for node in text_nodes:
                if node.nodeType == node.TEXT_NODE:
                    content.append(node.data + "\n")
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

# ---------- ChatGPT Parsers ----------
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


def chatgpt_parse_cv(cv_text):
    prompt = f"""
You will be given a candidate's CV in plain text. Extract the following fields:
- Name (if available)
- Contact Information (if available)
- Work Experience (as a list of roles with title, company, duration)
- Education (as a list with degree, institution, year)
- Skills (as a list)
- Certifications (if mentioned)
- Languages (if mentioned)
- Summary or Objective (if available)

Return ONLY the result as raw JSON, with no explanation or formatting.

CV:
{cv_text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You extract structured data from CVs."},
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
        for skill in self.skills:
            print(f"  • {skill}")
        print("\n📋 Responsibilities:")
        for r in self.responsibilities:
            print(f"  • {r}")
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
        print(f"✅ Saved job profile to JSON: {filename}")

    def to_csv(self, filename):
        data = self.to_dict()
        for key in data:
            if isinstance(data[key], list):
                data[key] = ", ".join(data[key])
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print(f"✅ Saved job profile to CSV: {filename}")

# ---------- CandidateProfile Class ----------
class CandidateProfile:
    def __init__(self, data: dict):
        self.name = data.get("Name")
        self.contact = data.get("Contact Information")
        self.summary = data.get("Summary or Objective")
        self.skills = data.get("Skills", [])
        self.experience = data.get("Work Experience", [])
        self.education = data.get("Education", [])
        self.languages = data.get("Languages")
        self.certifications = data.get("Certifications")

    def display_summary(self):
        print(f"\n🙋 Candidate Name: {self.name}")
        print(f"📞 Contact Info: {self.contact}")
        print(f"\n🧠 Summary:\n{self.summary}")
        print("\n🛠️ Skills:")
        for skill in self.skills:
            print(f"  • {skill}")
        print("\n📋 Work Experience:")
        for exp in self.experience:
            print(f"  • {exp}")
        print("\n🎓 Education:")
        for edu in self.education:
            print(f"  • {edu}")
        print(f"\n📜 Certifications: {self.certifications}")
        print(f"🗣️ Languages: {self.languages}")

    def to_dict(self):
        return {
            "Name": self.name,
            "Contact Information": self.contact,
            "Summary or Objective": self.summary,
            "Skills": self.skills,
            "Work Experience": self.experience,
            "Education": self.education,
            "Languages": self.languages,
            "Certifications": self.certifications
        }

    def to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        print(f"✅ Saved CV to JSON: {filename}")

# ---------- Comparison Function ----------
def compare_profiles(job_profile, candidate_profile):
    total_score = 0
    max_score = 5
    explanations = []

    # Compare Skills
    if job_profile.skills:
        common_skills = set(job_profile.skills).intersection(candidate_profile.skills)
        skill_fit_percentage = (len(common_skills) / len(job_profile.skills)) * 100 if job_profile.skills else 0
        total_score += skill_fit_percentage
        explanations.append(f"🛠️ Skills Fit: The candidate possesses {len(common_skills)} of the required skills. Fit: {skill_fit_percentage:.2f}%")
    else:
        explanations.append("🛠️ Skills Fit: No specific skills required by the job.")

    # Compare Experience
    relevant_experience = 0
    for exp in candidate_profile.experience:
        if isinstance(exp, dict):  # If experience is in dictionary format (e.g., with 'title')
            title = exp.get('title', '').lower()
            if job_profile.title.lower() in title:
                relevant_experience = 1
                break
        elif isinstance(exp, str):  # If experience is a string (just the role name)
            if job_profile.title.lower() in exp.lower():
                relevant_experience = 1
                break
    experience_fit_percentage = relevant_experience * 100
    total_score += experience_fit_percentage
    explanations.append(f"💼 Experience Fit: The candidate has relevant experience. Fit: {experience_fit_percentage}%")

    # Compare Education
    education_fit_percentage = 0
    matching_educations = []
    if job_profile.education and candidate_profile.education:
        matching_educations = []
        for edu in candidate_profile.education:
            if isinstance(edu, dict):
                degree = edu.get('degree', '').lower()
                institution = edu.get('institution', '').lower()
                # Match by degree or institution with job profile education requirements
                for job_edu in job_profile.education:
                    if isinstance(job_edu, str):  # If job profile education is a string (e.g., "Bachelor's in Computer Science")
                        if job_edu.lower() in degree or job_edu.lower() in institution:
                            matching_educations.append(edu)
                            break
                    elif isinstance(job_edu, dict):  # If job profile education is a dictionary (with degree, institution, etc.)
                        job_degree = job_edu.get('degree', '').lower()
                        job_institution = job_edu.get('institution', '').lower()
                        if job_degree in degree or job_institution in institution:
                            matching_educations.append(edu)
                            break
        education_fit_percentage = (len(matching_educations) / len(job_profile.education)) * 100
    total_score += education_fit_percentage
    explanations.append(f"🎓 Education Fit: The candidate has {len(matching_educations)} matching educational qualifications. Fit: {education_fit_percentage:.2f}%")

    # Compare Certifications
    certification_fit_percentage = 0
    matching_certs = []
    if job_profile.certifications:
        matching_certs = [cert for cert in candidate_profile.certifications if cert in job_profile.certifications]
        certification_fit_percentage = (len(matching_certs) / len(job_profile.certifications)) * 100
    total_score += certification_fit_percentage
    explanations.append(f"📜 Certifications Fit: The candidate holds {len(matching_certs)} of the required certifications. Fit: {certification_fit_percentage:.2f}%")

    # Compare Languages
    language_fit_percentage = 0
    matching_languages = []
    if job_profile.languages:
        matching_languages = [lang for lang in candidate_profile.languages if lang in job_profile.languages]
        language_fit_percentage = (len(matching_languages) / len(job_profile.languages)) * 100
    total_score += language_fit_percentage
    explanations.append(f"🗣️ Language Fit: The candidate speaks {len(matching_languages)} of the required languages. Fit: {language_fit_percentage:.2f}%")

    overall_fit_percentage = (total_score / (max_score * 100)) * 100

    # Debug prints to check if the function is returning values
    print(f"Total Fit Score: {overall_fit_percentage}")
    print(f"Explanations: {explanations}")

    if overall_fit_percentage >= 80:
        summary_comment = "The candidate is a strong fit for the job based on the key criteria."
    elif overall_fit_percentage >= 50:
        summary_comment = "The candidate has potential, but there are areas for improvement."
    else:
        summary_comment = "The candidate may need further development or experience in several key areas."

    # Debug print to confirm function is returning a value
    print(f"Summary Comment: {summary_comment}")

    return overall_fit_percentage, explanations, summary_comment



# ---------- MAIN ----------
if __name__ == "__main__":
    input_folder = "/home/michael/Documents/TU259/OOSD/Python_Project_TU259/Output_Files"

    print("🔹 First, load the job profile.")
    print("Choose the file type:\n1 - TXT\n2 - DOCX\n3 - ODT\n4 - PDF")
    job_choice = input("Enter a number (1-4): ").strip()
    job_file = input("Enter the base file name for the job description (without extension): ").strip()
    ext_map = {"1": ".txt", "2": ".docx", "3": ".odt", "4": ".pdf"}
    job_path = os.path.join(input_folder, job_file + ext_map.get(job_choice, ""))

    if not os.path.exists(job_path):
        print("❌ Job description file not found.")
        exit()

    if job_choice == "1":
        job_text = read_txt_file(job_path)
    elif job_choice == "2":
        job_text = read_docx_file(job_path)
    elif job_choice == "3":
        job_text = read_odt_file(job_path)
    elif job_choice == "4":
        job_text = read_pdf_file(job_path)

    job_text = "".join(job_text)
    print("\n🧠 Sending job profile to ChatGPT...")
    job_json = chatgpt_parse_job_profile(job_text)

    try:
        job_data = json.loads(job_json)
        job = JobProfile(job_data)
        job.to_json("job_profile_output.json")
        job.to_csv("job_profile_output.csv")
    except Exception as e:
        print("❌ Failed to parse job profile JSON.", e)
        exit()

    print("\n✅ Job profile parsed successfully.")
    if input("👀 Display job profile? (y/n): ").lower() == "y":
        job.display_summary()

    # ---- Candidate Section ----
    print("\n🔹 Now, load the candidate's CV.")
    print("Choose the file type:\n1 - TXT\n2 - DOCX\n3 - ODT\n4 - PDF")
    cv_choice = input("Enter a number (1-4): ").strip()
    cv_file = input("Enter the base file name for the candidate CV (without extension): ").strip()
    cv_path = os.path.join(input_folder, cv_file + ext_map.get(cv_choice, ""))

    if not os.path.exists(cv_path):
        print("❌ CV file not found.")
        exit()

    if cv_choice == "1":
        cv_text = read_txt_file(cv_path)
    elif cv_choice == "2":
        cv_text = read_docx_file(cv_path)
    elif cv_choice == "3":
        cv_text = read_odt_file(cv_path)
    elif cv_choice == "4":
        cv_text = read_pdf_file(cv_path)

    cv_text = "".join(cv_text)
    print("\n🧠 Sending CV to ChatGPT...")
    cv_json = chatgpt_parse_cv(cv_text)

    try:
        cv_data = json.loads(cv_json)
        candidate = CandidateProfile(cv_data)
        candidate.to_json("cv_structured.json")
    except Exception as e:
        print("❌ Failed to parse candidate CV JSON.", e)
        exit()

    print("\n✅ Candidate CV parsed successfully.")
    if input("👀 Display candidate CV? (y/n): ").lower() == "y":
        candidate.display_summary()

    # ---- Comparison ----
    print("\n🔹 Comparing job profile with candidate CV...")

    fit_score, explanations, summary_comment = compare_profiles(job, candidate)

    print(f"\n🔍 Candidate Fit Score: {fit_score:.2f}%")
    for explanation in explanations:
        print(explanation)

    print(f"\n📝 Summary Comment: {summary_comment}")
