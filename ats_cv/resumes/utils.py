import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_resume(resume_path):
    """Extract text from a PDF resume."""
    text = ""
    try:
        with open(resume_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + " "
    except Exception as e:
        print(f"Error reading the resume file: {e}")
    return text.strip()

def process_resume(resume_path, job_description):
    """Process resume and calculate similarity with job description."""
    resume_text = extract_text_from_resume(resume_path)
    
    if not resume_text:
        print("No text extracted from resume.")
        return 0  # Return a score of 0 if no text is found

    # Calculate cosine similarity
    vectorizer = TfidfVectorizer()
    documents = [job_description, resume_text]
    tfidf_matrix = vectorizer.fit_transform(documents)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return cosine_sim[0][0]
