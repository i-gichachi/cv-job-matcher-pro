import streamlit as st
import PyPDF2
import re
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from io import BytesIO

# Page config
st.set_page_config(page_title="CV-Job Matcher Pro", page_icon="🎯", layout="wide")

# Initialize session state
if 'cv_content' not in st.session_state:
    st.session_state.cv_content = ""

# Title
st.title("🎯 CV-Job Matcher Pro")
st.write("Expert-level CV analysis powered by 30 years of recruitment and ATS expertise")

# Tabs
tab1, tab2 = st.tabs(["🔍 Analyze CV", "📊 Match to Job"])

# TAB 1: CV Analysis
with tab1:
    st.header("Step 1: Analyze Your CV")
    st.write("📋 **Expert System:** You are a job search expert with 30 years of experience helping clients find roles that match their qualifications.")
    
    cv_analyze_file = st.file_uploader("Upload your CV (PDF/TXT):", type=['pdf', 'txt'], key="cv_file_analyze")
    
    if cv_analyze_file:
        if cv_analyze_file.type == "text/plain":
            uploaded_cv = cv_analyze_file.read().decode()
            st.session_state.cv_content = uploaded_cv
        elif cv_analyze_file.type == "application/pdf":
            try:
                pdf_reader = PyPDF2.PdfReader(cv_analyze_file)
                uploaded_cv = ""
                for page in pdf_reader.pages:
                    uploaded_cv += page.extract_text()
                st.session_state.cv_content = uploaded_cv
                st.success(f"✅ PDF uploaded successfully! Extracted {len(uploaded_cv)} characters.")
            except Exception as e:
                st.error(f"Error reading PDF: {e}")
    
    cv_analyze_text = st.text_area(
        "Or paste your CV here:",
        value=st.session_state.cv_content,
        height=400,
        placeholder="Paste your complete CV text here...",
        key="cv_analyze"
    )
    
    if cv_analyze_text:
        st.session_state.cv_content = cv_analyze_text
    
    if st.button("🔍 Analyze My CV", type="primary", key="analyze_cv_btn"):
        if st.session_state.cv_content:
            with st.spinner("🎯 Expert system analyzing your CV with 30 years of recruitment experience..."):
                def analyze_cv_as_expert(cv_text):
                    """
                    EXPERT PROMPT: You are a job search expert with 30 years of experience 
                    helping clients find roles that match their qualifications.
                    
                    Analyze the CV and identify the best-matching career paths based on:
                    - Skills and technical competencies
                    - Experience level and domain expertise
                    - Industry-specific keywords
                    - Professional qualifications
                    """
                    cv_lower = cv_text.lower()
                    
                    # Comprehensive career database with industry-standard keywords
                    career_categories = {
                        'Software Developer': {
                            'keywords': ['python', 'java', 'javascript', 'c++', 'c#', 'programming', 'coding', 'software', 'developer', 'development', 'git', 'api', 'algorithms', 'data structures'],
                            'weight': 3,
                            'industry': 'Technology'
                        },
                        'Web Developer': {
                            'keywords': ['html', 'css', 'javascript', 'react', 'angular', 'vue', 'web', 'frontend', 'backend', 'full stack', 'node', 'django', 'flask', 'responsive'],
                            'weight': 3,
                            'industry': 'Technology'
                        },
                        'Mobile Developer': {
                            'keywords': ['android', 'ios', 'mobile', 'app', 'flutter', 'react native', 'swift', 'kotlin', 'mobile development'],
                            'weight': 3,
                            'industry': 'Technology'
                        },
                        'Data Analyst / Data Scientist': {
                            'keywords': ['data', 'analytics', 'analysis', 'sql', 'python', 'statistics', 'tableau', 'power bi', 'excel', 'visualization', 'insights', 'reporting'],
                            'weight': 3,
                            'industry': 'Technology/Analytics'
                        },
                        'DevOps / Cloud Engineer': {
                            'keywords': ['aws', 'azure', 'cloud', 'docker', 'kubernetes', 'devops', 'jenkins', 'ci/cd', 'infrastructure', 'automation', 'terraform'],
                            'weight': 3,
                            'industry': 'Technology'
                        },
                        'IT Support / Systems Administrator': {
                            'keywords': ['support', 'help desk', 'troubleshooting', 'windows', 'linux', 'network', 'systems', 'administration', 'hardware', 'technical support'],
                            'weight': 2,
                            'industry': 'Technology'
                        },
                        'Accountant / Financial Analyst': {
                            'keywords': ['accounting', 'finance', 'financial', 'audit', 'tax', 'bookkeeping', 'budget', 'cpa', 'ifrs', 'gaap', 'ledger', 'reconciliation'],
                            'weight': 3,
                            'industry': 'Finance'
                        },
                        'Business Analyst': {
                            'keywords': ['business analyst', 'requirements', 'stakeholder', 'process', 'analysis', 'documentation', 'strategy', 'workflow', 'improvement'],
                            'weight': 3,
                            'industry': 'Business'
                        },
                        'Project Manager': {
                            'keywords': ['project management', 'pmp', 'agile', 'scrum', 'planning', 'coordination', 'delivery', 'timeline', 'budget', 'stakeholder', 'risk'],
                            'weight': 3,
                            'industry': 'Business'
                        },
                        'Sales / Business Development': {
                            'keywords': ['sales', 'business development', 'revenue', 'clients', 'negotiation', 'pipeline', 'crm', 'b2b', 'targets', 'closing'],
                            'weight': 2,
                            'industry': 'Sales'
                        },
                        'Marketing Specialist': {
                            'keywords': ['marketing', 'campaigns', 'branding', 'strategy', 'social media', 'digital marketing', 'seo', 'content', 'email', 'analytics'],
                            'weight': 3,
                            'industry': 'Marketing'
                        },
                        'Content Writer / Copywriter': {
                            'keywords': ['writing', 'content', 'copywriting', 'editor', 'articles', 'blog', 'copy', 'creative writing', 'seo writing'],
                            'weight': 2,
                            'industry': 'Marketing/Creative'
                        },
                        'Graphic Designer': {
                            'keywords': ['graphic design', 'photoshop', 'illustrator', 'design', 'visual', 'creative', 'branding', 'ui/ux', 'adobe', 'figma'],
                            'weight': 3,
                            'industry': 'Creative'
                        },
                        'Social Media Manager': {
                            'keywords': ['social media', 'facebook', 'instagram', 'twitter', 'linkedin', 'engagement', 'community', 'content', 'campaigns'],
                            'weight': 2,
                            'industry': 'Marketing'
                        },
                        'Nurse / Healthcare Professional': {
                            'keywords': ['nurse', 'nursing', 'patient', 'care', 'clinical', 'healthcare', 'medical', 'hospital', 'rn', 'treatment', 'bedside'],
                            'weight': 3,
                            'industry': 'Healthcare'
                        },
                        'Medical Doctor / Physician': {
                            'keywords': ['doctor', 'physician', 'medical', 'diagnosis', 'treatment', 'clinical', 'patient', 'medicine', 'healthcare'],
                            'weight': 3,
                            'industry': 'Healthcare'
                        },
                        'Pharmacist': {
                            'keywords': ['pharmacy', 'pharmacist', 'medication', 'prescription', 'pharmaceutical', 'drug', 'dispensing', 'patient counseling'],
                            'weight': 3,
                            'industry': 'Healthcare'
                        },
                        'Teacher / Educator': {
                            'keywords': ['teacher', 'teaching', 'education', 'classroom', 'students', 'curriculum', 'lesson', 'instruction', 'tutor', 'pedagogy'],
                            'weight': 2,
                            'industry': 'Education'
                        },
                        'Training & Development Specialist': {
                            'keywords': ['training', 'learning', 'development', 'facilitation', 'workshop', 'coaching', 'instructional', 'employee development'],
                            'weight': 2,
                            'industry': 'HR/Training'
                        },
                        'Legal Professional / Lawyer': {
                            'keywords': ['legal', 'law', 'attorney', 'lawyer', 'litigation', 'contracts', 'compliance', 'paralegal', 'court', 'legal research'],
                            'weight': 3,
                            'industry': 'Legal'
                        },
                        'Human Resources Specialist': {
                            'keywords': ['human resources', 'hr', 'recruitment', 'hiring', 'talent', 'employee', 'onboarding', 'payroll', 'benefits', 'relations'],
                            'weight': 2,
                            'industry': 'HR'
                        },
                        'Administrative Assistant': {
                            'keywords': ['administrative', 'admin', 'office', 'scheduling', 'coordination', 'clerical', 'secretary', 'support', 'organization'],
                            'weight': 2,
                            'industry': 'Administration'
                        },
                        'Operations Manager': {
                            'keywords': ['operations', 'logistics', 'supply chain', 'inventory', 'procurement', 'warehouse', 'management', 'process improvement'],
                            'weight': 3,
                            'industry': 'Operations'
                        },
                        'Customer Service Representative': {
                            'keywords': ['customer service', 'support', 'customer', 'help', 'clients', 'satisfaction', 'call center', 'complaints', 'resolution'],
                            'weight': 2,
                            'industry': 'Customer Service'
                        },
                        'Engineer': {
                            'keywords': ['engineer', 'engineering', 'mechanical', 'electrical', 'civil', 'technical', 'design', 'cad', 'manufacturing', 'autocad'],
                            'weight': 3,
                            'industry': 'Engineering'
                        },
                    }
                    
                    role_scores = {}
                    
                    for role, details in career_categories.items():
                        keyword_matches = 0
                        matched_keywords = []
                        
                        for keyword in details['keywords']:
                            if keyword in cv_lower:
                                keyword_matches += 1
                                matched_keywords.append(keyword)
                        
                        if keyword_matches > 0:
                            # Calculate score based on keyword density and weight
                            base_score = (keyword_matches / len(details['keywords'])) * 100
                            weighted_score = min(95, base_score * details['weight'] / 2)
                            role_scores[role] = {
                                'score': int(weighted_score),
                                'matches': matched_keywords,
                                'industry': details['industry']
                            }
                    
                    sorted_roles = sorted(role_scores.items(), key=lambda x: x[1]['score'], reverse=True)
                    
                    return sorted_roles[:8]
                
                roles = analyze_cv_as_expert(st.session_state.cv_content)
                
                st.success("✅ Expert Analysis Complete!")
                st.markdown("---")
                
                st.subheader("💼 Recommended Career Paths (Expert Assessment)")
                st.caption("🎯 **30-Year Recruitment Expert Analysis:** Based on your qualifications, experience, and skill set, here are your best-fit roles:")
                
                if roles:
                    col1, col2 = st.columns(2)
                    
                    for idx, (role, data) in enumerate(roles):
                        with col1 if idx % 2 == 0 else col2:
                            score = data['score']
                            industry = data.get('industry', '')
                            
                            if score >= 75:
                                st.success(f"**{role}**")
                                st.metric("Match Strength", f"{score}%", "Excellent Fit ⭐")
                            elif score >= 50:
                                st.info(f"**{role}**")
                                st.metric("Match Strength", f"{score}%", "Strong Fit")
                            else:
                                st.warning(f"**{role}**")
                                st.metric("Match Strength", f"{score}%", "Potential Fit")
                            
                            st.caption(f"🏢 Industry: {industry}")
                            
                            with st.expander("📋 See matching qualifications"):
                                st.write("**Your matching skills:**")
                                st.write(", ".join(data['matches'][:15]))
                            
                            st.markdown("---")
                    
                    st.success("""
                    ✅ **Next Steps:**
                    1. Use these **exact role titles** when searching on LinkedIn, Indeed, or BrighterMonday
                    2. Tailor your CV for each role using the matching keywords shown
                    3. Go to **Tab 2** to match your CV against specific job descriptions
                    4. Your CV is automatically saved for Tab 2!
                    """)
                else:
                    st.warning("⚠️ Unable to identify strong role matches. Consider adding more industry-specific skills, certifications, and experience details to your CV.")
                
        else:
            st.warning("⚠️ Please upload or paste your CV first")

# TAB 2: ATS-Powered Job Matching
with tab2:
    st.header("Step 2: ATS-Powered Job Matching")
    st.write("""
    🤖 **ATS Expert System:** Your task is to evaluate a job seeker's CV against a job description 
    and provide a compatibility rating out of 100 with 99% accuracy.
    
    You're an ATS systems scanner programmed to search for keywords in resumes to match them 
    with job descriptions. Exact keyword matches matter most to ATS systems.
    """)
    
    if not st.session_state.cv_content:
        st.error("⚠️ **REQUIRED: Please go to Tab 1 first to upload/paste your CV!**")
        st.info("👈 Click on 'Analyze CV' tab above to get started")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 Your CV")
        
        if st.session_state.cv_content:
            # Show actual CV content in readable format
            cv_lines = st.session_state.cv_content.split('\n')
            
            # Take first 30 lines or 1500 characters, whichever is smaller
            preview_lines = []
            char_count = 0
            for line in cv_lines:
                if char_count < 1500 and len(preview_lines) < 30:
                    preview_lines.append(line)
                    char_count += len(line)
                else:
                    break
            
            preview_text = '\n'.join(preview_lines)
            if len(st.session_state.cv_content) > 1500 or len(cv_lines) > 30:
                preview_text += "\n\n... (CV content continues)"
            
            st.text_area(
                "CV Content (auto-loaded from Tab 1):",
                value=preview_text,
                height=400,
                disabled=True,
                help="Your complete CV was automatically loaded from Tab 1"
            )
            
            # Show CV stats
            word_count = len(st.session_state.cv_content.split())
            char_count = len(st.session_state.cv_content)
            st.caption(f"📊 CV Stats: {word_count} words | {char_count} characters")
            
            st.success("✅ CV loaded and ready for ATS analysis!")
        else:
            st.info("👈 Go to Tab 1 to add your CV first")
    
    with col2:
        st.subheader("💼 Job Description")
        jd_text = st.text_area(
            "Paste the complete job description:",
            height=400,
            placeholder="""Paste the full job posting here, including:
- Job title
- Required qualifications
- Responsibilities
- Required skills
- Experience requirements
- Education requirements

The more complete the job description, the more accurate the ATS analysis!""",
            key="jd_match"
        )

    def extract_ats_keywords(text):
        """
        SMART ATS SYSTEM: Extract critical keywords and JOB-RELEVANT phrases only
        - Technical skills
        - Certifications
        - Industry-specific multi-word terms (NOT generic phrases)
        - Professional qualifications
        """
        text_lower = text.lower()
        
        # Extract all meaningful words (4+ characters)
        words = re.findall(r'\b[a-z]{4,}\b', text_lower)
        
        # ATS stop words (words ATS systems typically ignore)
        ats_stop_words = {
            'that', 'with', 'have', 'this', 'from', 'were', 'been', 'will', 
            'would', 'there', 'their', 'what', 'when', 'where', 'which', 'while',
            'about', 'after', 'before', 'other', 'such', 'than', 'then', 'these',
            'those', 'very', 'your', 'they', 'should', 'could', 'years', 'work',
            'working', 'including', 'related', 'ability', 'strong', 'good', 'excellent',
            'must', 'able', 'well', 'also', 'make', 'take', 'provide', 'ensure',
            'across', 'within', 'through', 'between', 'during', 'under', 'over'
        }
        
        # Filter keywords
        keywords = [w for w in words if w not in ats_stop_words and len(w) > 3]
        
        # ============================================================
        # SMART PHRASE EXTRACTION - Industry & role-specific ONLY
        # ============================================================
        # These are JOB-RELEVANT phrases that actually matter in ATS scoring
        # NOT generic phrases like "years experience" or "strong communication"
        
        important_phrase_patterns = [
            # TECHNOLOGY & IT
            'machine learning', 'deep learning', 'artificial intelligence', 'data science',
            'data analysis', 'data analytics', 'business intelligence', 'software development',
            'web development', 'mobile development', 'full stack', 'front end', 'back end',
            'cloud computing', 'cloud infrastructure', 'devops engineer', 'system administrator',
            'database management', 'database administrator', 'network security', 'cyber security',
            'information security', 'project management', 'product management', 'agile methodology',
            'version control', 'continuous integration', 'continuous deployment', 'quality assurance',
            'software testing', 'test automation', 'user experience', 'user interface',
            'react native', 'angular framework', 'vue framework', 'node.js', 'ruby rails',
            'software engineer', 'senior developer', 'lead developer', 'technical lead',
            'solution architect', 'cloud architect', 'infrastructure engineer',
            
            # BUSINESS & FINANCE
            'business development', 'business analyst', 'business strategy', 'strategic planning',
            'financial analysis', 'financial reporting', 'financial modeling', 'budget management',
            'risk management', 'change management', 'stakeholder management', 'vendor management',
            'supply chain', 'inventory management', 'operations management', 'process improvement',
            'quality control', 'customer service', 'client relations', 'account management',
            'relationship management', 'portfolio management', 'asset management',
            'business operations', 'operational excellence', 'performance metrics',
            
            # MARKETING & SALES
            'digital marketing', 'content marketing', 'social media', 'email marketing',
            'search engine', 'seo optimization', 'market research', 'brand management',
            'sales strategy', 'lead generation', 'customer acquisition', 'revenue growth',
            'growth marketing', 'performance marketing', 'marketing automation',
            'content strategy', 'social media management', 'community management',
            
            # HR & ADMINISTRATION
            'human resources', 'talent acquisition', 'employee relations', 'performance management',
            'compensation benefits', 'organizational development', 'training development',
            'administrative support', 'office management', 'executive assistant',
            'workforce planning', 'employee engagement', 'change management',
            
            # HEALTHCARE
            'patient care', 'clinical practice', 'medical records', 'health information',
            'nursing care', 'emergency medicine', 'primary care', 'mental health',
            'clinical research', 'healthcare administration', 'medical coding',
            
            # EDUCATION
            'curriculum development', 'instructional design', 'classroom management',
            'student assessment', 'educational technology', 'professional development',
            'learning management', 'training programs', 'course development',
            
            # ENGINEERING (Non-Software)
            'civil engineering', 'mechanical engineering', 'electrical engineering',
            'systems engineering', 'product development', 'technical support',
            'technical documentation', 'quality engineering', 'process engineering',
            
            # LEGAL
            'legal research', 'contract management', 'regulatory compliance',
            'intellectual property', 'corporate law', 'legal analysis',
            'legal counsel', 'contract negotiation', 'compliance management',
            
            # PROJECT/PRODUCT MANAGEMENT
            'project coordination', 'program management', 'product lifecycle',
            'sprint planning', 'scrum master', 'product owner', 'roadmap planning',
            'cross functional', 'team leadership', 'resource planning'
        ]
        
        # Extract ONLY important phrases that actually appear in the text
        found_phrases = set()
        for phrase in important_phrase_patterns:
            if phrase in text_lower:
                found_phrases.add(phrase)
        
        # ALSO extract skill + tool/action combinations
        # (e.g., "python programming", "react development", "aws infrastructure")
        skill_keywords = {
            'python', 'java', 'javascript', 'react', 'angular', 'vue', 'node',
            'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'sql', 'nosql', 'mongodb',
            'postgresql', 'redis', 'git', 'jenkins', 'terraform', 'ansible',
            'typescript', 'golang', 'rust', 'swift', 'kotlin', 'flutter',
            'django', 'flask', 'fastapi', 'spring', 'rails', 'laravel'
        }
        
        action_words = {
            'programming', 'development', 'engineering', 'administration',
            'management', 'design', 'testing', 'deployment', 'integration',
            'optimization', 'analysis', 'architect', 'developer', 'engineer',
            'infrastructure', 'automation', 'framework', 'implementation'
        }
        
        # Find skill + action combinations that are job-relevant
        words_list = text_lower.split()
        for i in range(len(words_list) - 1):
            word1, word2 = words_list[i], words_list[i+1]
            
            # Skill + action (e.g., "python programming", "aws infrastructure")
            if word1 in skill_keywords and word2 in action_words:
                found_phrases.add(f"{word1} {word2}")
            
            # Action + skill (e.g., "cloud computing")
            if word2 in skill_keywords and word1 in action_words:
                found_phrases.add(f"{word1} {word2}")
        
        return set(keywords), found_phrases

    def ats_compatibility_score(cv_text, jd_text):
        """
        ATS COMPATIBILITY ANALYSIS with 99% accuracy goal
        
        This function mimics how Applicant Tracking Systems score resumes:
        1. Extract all keywords from job description
        2. Extract ONLY job-relevant phrases (not generic ones)
        3. Check which keywords/phrases appear in CV
        4. Calculate match percentage
        5. Identify missing critical keywords
        """
        
        # Extract keywords using SMART ATS logic
        cv_keywords, cv_phrases = extract_ats_keywords(cv_text)
        jd_keywords, jd_phrases = extract_ats_keywords(jd_text)
        
        # Calculate exact matches (ATS systems prioritize exact matches)
        keyword_matches = cv_keywords.intersection(jd_keywords)
        phrase_matches = cv_phrases.intersection(jd_phrases)
        
        # Missing keywords (critical for improvement)
        missing_keywords = jd_keywords - cv_keywords
        missing_phrases = jd_phrases - cv_phrases
        
        # ATS Scoring Algorithm
        # Phrases weighted MUCH HIGHER as they're job-specific and more meaningful
        total_jd_items = len(jd_keywords) + (len(jd_phrases) * 2.5)
        total_matches = len(keyword_matches) + (len(phrase_matches) * 2.5)
        
        if total_jd_items == 0:
            compatibility_score = 0
        else:
            compatibility_score = int((total_matches / total_jd_items) * 100)
        
        # Cap at 99% (as no match is 100% perfect)
        compatibility_score = min(compatibility_score, 99)
        
        return compatibility_score, keyword_matches, phrase_matches, missing_keywords, missing_phrases

    def create_pdf_report(analysis_text, match_score):
        """Generate professional PDF report"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor='#1f77b4',
            alignment=TA_CENTER,
            spaceAfter=20
        )
        
        story = []
        story.append(Paragraph("CV-JOB MATCHER PRO", title_style))
        story.append(Paragraph("ATS Compatibility Analysis Report", styles['Heading3']))
        story.append(Spacer(1, 0.2*inch))
        
        date_text = f"<b>Generated:</b> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
        story.append(Paragraph(date_text, styles['BodyText']))
        
        score_color = 'green' if match_score >= 80 else 'orange' if match_score >= 60 else 'red'
        score_text = f"<b>ATS Compatibility Score:</b> <font size=18 color={score_color}>{match_score}%</font>"
        story.append(Paragraph(score_text, styles['BodyText']))
        story.append(Spacer(1, 0.3*inch))
        
        for line in analysis_text.split('\n'):
            if line.strip():
                try:
                    story.append(Paragraph(line, styles['BodyText']))
                    story.append(Spacer(1, 0.1*inch))
                except:
                    pass
        
        story.append(Spacer(1, 0.5*inch))
        footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=9, textColor='gray', alignment=TA_CENTER)
        story.append(Paragraph("Generated by CV-Job Matcher Pro | ATS-Powered Analysis", footer_style))
        story.append(Paragraph("Moringa School AI Capstone Project 2025", footer_style))
        
        doc.build(story)
        buffer.seek(0)
        return buffer

    # ATS ANALYSIS BUTTON
    if st.button("🤖 Run ATS Analysis", type="primary", key="ats_analyze_btn", use_container_width=True):
        if not st.session_state.cv_content:
            st.error("❌ **ERROR:** Please go to Tab 1 and add your CV first!")
            st.info("The ATS system cannot analyze without a CV.")
        elif not jd_text:
            st.warning("⚠️ **WARNING:** Please paste the job description above")
        else:
            with st.spinner("🤖 ATS System analyzing compatibility with 99% accuracy goal..."):
                try:
                    # Run SMART ATS analysis
                    score, keyword_matches, phrase_matches, missing_keywords, missing_phrases = ats_compatibility_score(
                        st.session_state.cv_content, 
                        jd_text
                    )
                    
                    # Display ATS Compatibility Score
                    st.success("✅ ATS Analysis Complete!")
                    st.markdown("---")
                    
                    # Prominent score display
                    st.subheader("🎯 ATS COMPATIBILITY RATING")
                    col1, col2, col3 = st.columns([1,2,1])
                    with col2:
                        if score >= 80:
                            st.success(f"# {score}%")
                            st.success("**✅ EXCELLENT - High chance of passing ATS!**")
                            recommendation = "Your CV is well-optimized for ATS systems. You should apply with confidence!"
                        elif score >= 60:
                            st.warning(f"# {score}%")
                            st.warning("**⚠️ GOOD - May pass ATS but needs improvement**")
                            recommendation = "Your CV has decent ATS compatibility, but adding missing keywords will significantly improve your chances."
                        else:
                            st.error(f"# {score}%")
                            st.error("**❌ NEEDS WORK - Low ATS pass rate**")
                            recommendation = "Your CV needs significant optimization. Focus on adding the missing keywords below to improve ATS compatibility."
                    
                    st.info(f"**💡 Recommendation:** {recommendation}")
                    
                    st.markdown("---")
                    
                    # Detailed ATS Analysis
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ ATS FOUND IN YOUR CV")
                        
                        st.write(f"**Matching Keywords:** {len(keyword_matches)}")
                        if keyword_matches:
                            st.success("These keywords were successfully detected by the ATS:")
                            keyword_display = ", ".join(sorted(list(keyword_matches))[:40])
                            st.write(keyword_display)
                        else:
                            st.warning("Very few keyword matches found!")
                        
                        st.markdown("---")
                        
                        st.write(f"**Matching Job-Relevant Phrases:** {len(phrase_matches)}")
                        if phrase_matches:
                            st.success("✨ These industry-specific phrases were found:")
                            phrase_display = ", ".join(sorted(list(phrase_matches))[:25])
                            st.write(phrase_display)
                            st.caption("💡 These are high-value, job-specific terms that ATS prioritizes!")
                        else:
                            st.info("No job-specific phrases detected")
                    
                    with col2:
                        st.subheader("❌ MISSING FROM YOUR CV")
                        
                        st.write(f"**Missing Keywords:** {len(missing_keywords)}")
                        if missing_keywords:
                            st.error("⚠️ **CRITICAL:** ATS is looking for these keywords but couldn't find them in your CV:")
                            critical_missing = sorted(list(missing_keywords))[:40]
                            st.write(", ".join(critical_missing))
                            
                            st.markdown("**🎯 Priority Action:**")
                            top_missing = critical_missing[:10]
                            st.warning(f"Add these ASAP: **{', '.join(top_missing)}**")
                        else:
                            st.success("✅ All keywords covered!")
                        
                        st.markdown("---")
                        
                        st.write(f"**Missing Job-Relevant Phrases:** {len(missing_phrases)}")
                        if missing_phrases:
                            st.warning("🔍 Critical industry-specific phrases not found:")
                            missing_phrase_display = ", ".join(sorted(list(missing_phrases))[:25])
                            st.write(missing_phrase_display)
                            st.caption("⚡ Adding these will significantly boost your ATS score!")
                        else:
                            st.success("✅ All job-specific phrases covered!")
                    
                    # ATS Optimization Recommendations
                    st.markdown("---")
                    st.subheader("📋 ATS OPTIMIZATION RECOMMENDATIONS")
                    
                    if score >= 80:
                        st.success("""
                        **✅ Your CV is ATS-Ready!**
                        
                        Your resume has excellent ATS compatibility. Minor suggestions:
                        
                        1. **Maintain keyword density** - Keep all matching keywords in your final version
                        2. **Use standard formatting** - Avoid tables, text boxes, or images that ATS can't read
                        3. **Save as .docx or .pdf** - These formats work best with ATS systems
                        4. **Proofread** - Ensure no typos in your keywords
                        5. **Apply with confidence** - Your CV should pass ATS filters successfully!
                        """)
                    elif score >= 60:
                        st.warning("""
                        **⚠️ Good Match - Optimization Needed**
                        
                        Your CV will likely pass ATS but can be improved:
                        
                        1. **Add missing job-specific phrases** - Incorporate the industry phrases shown above (e.g., "project management", "data analysis")
                        2. **Use exact wording from job description** - ATS looks for exact matches, not synonyms
                        3. **Prioritize missing critical phrases** - Multi-word industry terms carry MORE weight than single keywords
                        4. **Quantify achievements** - Add metrics alongside keywords (e.g., "Managed Python projects for 50+ clients")
                        5. **Mirror job description language** - Use similar phrasing and terminology
                        6. **Check spelling** - ATS can't match misspelled keywords
                        
                        **Rerun this analysis after updates to track improvement!**
                        """)
                    else:
                        st.error("""
                        **❌ Significant ATS Optimization Required**
                        
                        Your CV needs major improvements to pass ATS filters:
                        
                        1. **URGENT: Add missing job-relevant phrases** - Focus on the industry-specific multi-word terms listed above
                        2. **Add critical keywords** - Review the "Missing Keywords" list and add ALL relevant ones you actually possess
                        3. **Use industry-standard terminology** - Include exact phrases from the job description (e.g., "machine learning", "project management")
                        4. **Restructure your CV** - Use clear section headers: "Skills", "Experience", "Education"
                        5. **Use standard job titles** - Match industry-standard role names from the job description
                        6. **Avoid graphics and fancy formatting** - ATS can't read images, text boxes, or complex layouts
                        7. **Update and retest** - Make changes and run this analysis again to track improvement
                        
                        **⚠️ Warning:** At this score, your CV likely won't pass automated ATS screening. Prioritize adding job-relevant phrases!
                        """)
                    
                    # Create downloadable analysis report
                    analysis_report = f"""
ATS COMPATIBILITY ANALYSIS REPORT
{'='*60}

COMPATIBILITY SCORE: {score}%

ANALYSIS SUMMARY:
{recommendation}

KEYWORDS FOUND IN YOUR CV ({len(keyword_matches)}):
{', '.join(sorted(list(keyword_matches))[:50])}

JOB-RELEVANT PHRASES FOUND ({len(phrase_matches)}):
{', '.join(sorted(list(phrase_matches))[:30])}

MISSING CRITICAL KEYWORDS ({len(missing_keywords)}):
{', '.join(sorted(list(missing_keywords))[:50])}

MISSING JOB-RELEVANT PHRASES ({len(missing_phrases)}):
{', '.join(sorted(list(missing_phrases))[:30])}

RECOMMENDATIONS:
- Focus on adding the missing JOB-SPECIFIC PHRASES (e.g., "project management", "data analysis")
- Add missing keywords that genuinely apply to your experience
- Use exact wording from the job description
- Ensure your CV format is ATS-friendly (avoid complex formatting)
- Rerun this analysis after making updates

NOTE: Job-relevant phrases are weighted higher in scoring as they are more specific and valuable to ATS systems.

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Smart ATS Analysis System - CV-Job Matcher Pro
                    """
                    
                    # Download buttons
                    st.markdown("---")
                    st.subheader("📥 Download Your ATS Analysis Report")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.download_button(
                            label="📄 Download as TXT",
                            data=analysis_report,
                            file_name=f"ats_analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col2:
                        try:
                            pdf_buffer = create_pdf_report(analysis_report, score)
                            st.download_button(
                                label="📑 Download as PDF",
                                data=pdf_buffer,
                                file_name=f"ats_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.info("PDF generation unavailable - TXT download is available above")
                    
                except Exception as e:
                    st.error(f"❌ Analysis Error: {str(e)}")
                    st.info("Please check that both your CV and job description are properly formatted and try again.")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About This Tool")
    st.write("""
    **CV-Job Matcher Pro**
    
    🎯 **Dual Expert System:**
    
    **Tab 1:** 30-year recruitment expert
    - Career path recommendations
    - Skills analysis
    - Role matching
    
    **Tab 2:** Smart ATS scanner
    - 99% accuracy goal
    - Job-relevant phrase matching
    - Industry-specific scoring
    """)
    
    st.header("📊 How to Use")
    st.write("""
    **Step 1:** Upload CV in Tab 1
    - Get expert career recommendations
    - CV saved automatically
    
    **Step 2:** Paste job description in Tab 2
    - Get ATS compatibility score
    - See missing job-specific phrases
    - Download analysis report
    """)
    
    st.header("🎯 Universal Coverage")
    st.info("""
    **ALL Industries Supported:**
    
    Technology • Finance • Healthcare
    Marketing • Education • Legal • HR
    Sales • Operations • Engineering
    Administration • Customer Service
    
    **& Many More!**
    """)
    
    st.header("⚡ Success Tips")
    st.success("""
    **Maximize Your ATS Score:**
    
    ✅ Use job-specific phrases (e.g., "project management")
    ✅ Include exact keywords from posting
    ✅ Add industry certifications
    ✅ Use standard section headers
    ✅ Avoid complex formatting
    ✅ Aim for 80%+ compatibility
    """)

st.markdown("---")
st.markdown("*Universal Career Coaching Tool with Smart ATS Intelligence | Moringa School AI Capstone 2025*")