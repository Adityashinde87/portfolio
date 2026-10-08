"""Portfolio website (Flask). All content lives in the PORTFOLIO dict below,
so you only edit this file to change text, skills, projects or links."""
from flask import Flask, render_template

app = Flask(__name__)

PORTFOLIO = {
    "name": "Aditya Shinde",
    "title": "Data Scientist | Generative AI Trainer",
    "roles": ["Data Scientist", "Generative AI Trainer", "Data Analytics & ML Trainer"],
    "intro": "I train students in Data Analytics, Machine Learning and Generative AI, "
             "and build practical AI-powered applications, chatbots and predictive models.",
    "summary": "Data Scientist and Generative AI Trainer with 1.6+ years of teaching and technical "
               "training experience in Data Analytics, Machine Learning, and Generative AI. Skilled in "
               "Python, SQL, Power BI, LLMs, Prompt Engineering, RAG, LangChain, Embeddings, and Vector "
               "Databases. Experienced in developing AI-powered applications, intelligent chatbots, "
               "predictive models, and business analytics solutions.",
    "focus": "Passionate about training students and building practical solutions using modern "
             "Generative AI technologies.",
    "email": "adityashinde8742@gmail.com",
    "phone": "9970718742",
    "location": "Pune, India",
    "linkedin": "https://www.linkedin.com/in/aditya-shinde87",
    "github": "https://github.com/Adityashinde87",
    "resume_file": "resume/Aditya_Shinde_Resume.pdf",
    "stats": [("1.6+", "Years of training experience"), ("200+", "Students trained"),
              ("3", "Projects showcased"), ("4", "Core domains")],
    "skills": {
        "Languages": ["Python", "SQL"],
        "Data Analysis": ["EDA", "Data Cleaning", "Data Visualization", "Statistical Analysis",
                          "Feature Engineering", "Business Analytics"],
        "Machine Learning": ["Regression", "Classification", "Clustering", "Bagging", "Boosting",
                             "NLP", "Model Evaluation", "Predictive Modeling"],
        "Generative AI": ["LLMs", "Prompt Engineering", "RAG", "Embeddings", "LangChain",
                          "Vector Databases", "MCP", "LoRA"],
        "Libraries / Tools": ["Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Seaborn", "FAISS"],
        "Database & BI": ["MySQL", "Vector Databases", "Power BI", "Excel"],
    },
    "experience": [{
        "role": "Data Science & Generative AI Trainer",
        "company": "UV Technocrats & Solutions",
        "duration": "2024 – Present",
        "points": [
            "Trained 200+ students in Python, SQL, Data Analytics, Machine Learning, Power BI, and Generative AI.",
            "Conducted practical sessions on EDA, Data Visualization, Predictive Modeling, and Business Analytics.",
            "Delivered hands-on training on LLMs, Prompt Engineering, RAG Systems, LangChain, Embeddings, and Vector Databases.",
            "Guided students in developing Machine Learning and Generative AI projects.",
            "Provided practical exposure to Pandas, NumPy, Scikit-learn, Power BI, SQL, and Generative AI technologies.",
            "Mentored students in GitHub project management, resume building, portfolio development, and interview preparation.",
        ]}],
    "projects": [
        {"name": "E-commerce Sales Analysis", "category": "Data Analytics", "icon": "📊",
         "desc": "Analysis of sales data to uncover customer behavior, trends and business insights.",
         "tech": ["SQL", "Power BI", "Excel"],
         "features": ["Interactive Power BI dashboards for revenue and performance",
                      "SQL for extraction, filtering, aggregation and reporting",
                      "Business-focused visuals for data-driven decisions"]},
        {"name": "Loan Approval Prediction System", "category": "Machine Learning", "icon": "🧠",
         "desc": "Classification model that predicts loan approval status.",
         "tech": ["Python", "Machine Learning", "Scikit-learn"],
         "features": ["Preprocessing, EDA and feature engineering",
                      "Compared classification models using performance metrics",
                      "Identified key factors influencing approval"]},
        {"name": "UV Data Science Support Chatbot", "category": "Generative AI", "icon": "🤖",
         "desc": "AI chatbot answering Data Science and Generative AI queries from course materials.",
         "tech": ["LLM", "RAG", "LangChain", "FAISS", "Python"],
         "features": ["RAG with LangChain and FAISS vector database",
                      "PDF-based knowledge retrieval for course documents",
                      "Better accuracy via embeddings, vector search and prompt engineering"]},
    ],
    "education": [
        {"degree": "B.Sc. in Computer Science", "school": "S.B.B. Alias Appasaheb Jedhe Arts, Commerce & Science College", "year": "2024", "score": "74.64%"},
        {"degree": "Higher Secondary Certificate (HSC)", "school": "MES Sou Vimlabai Garware Junior College", "year": "2020", "score": "50.82%"},
        {"degree": "Secondary School Certificate (SSC)", "school": "MES Boys High School & Junior College", "year": "2018", "score": "76.20%"},
    ],
    "highlights": [
        ("🎓", "200+ students trained", "Python, SQL, Data Analytics, ML, Power BI and GenAI."),
        ("⏱️", "1.6+ years of training", "Hands-on technical training since 2024."),
        ("🧩", "End-to-end projects", "Analytics dashboard, ML model and a RAG chatbot."),
    ],
}


@app.route("/")
def index():
    cats = ["All"] + sorted({p["category"] for p in PORTFOLIO["projects"]})
    return render_template("index.html", p=PORTFOLIO, categories=cats)


if __name__ == "__main__":
    app.run(debug=True)
