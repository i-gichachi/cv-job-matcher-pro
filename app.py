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
st.write("Universal AI-powered CV analysis with cross-industry depth intelligence")

# Tabs
tab1, tab2 = st.tabs(["🔍 Analyze CV", "📊 Match to Job"])

# TAB 1: UNIVERSAL DEPTH ANALYSIS
with tab1:
    st.header("Step 1: Universal Intelligent CV Analysis")
    st.write("🌍 **Cross-Industry Expert System:** Analyzes experience depth across ALL industries - Technology, Healthcare, Finance, Marketing, Education, Legal, Sales, Operations, and more")
    
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
            with st.spinner("🌍 Universal expert system analyzing your CV across all industries..."):
                
                def extract_universal_depth_signals(cv_text):
                    """
                    UNIVERSAL DEPTH ANALYSIS - All Industries
                    Extracts depth indicators for every major field
                    """
                    signals = {
                        'years_experience': 0,
                        'quantified_achievements': [],
                        'leadership_indicators': [],
                        'certifications': [],
                        'specializations': [],
                        'industry_depth': {
                            'technology': 0,
                            'healthcare': 0,
                            'finance': 0,
                            'marketing': 0,
                            'education': 0,
                            'legal': 0,
                            'sales': 0,
                            'operations': 0,
                            'hr': 0,
                            'creative': 0
                        }
                    }
                    
                    cv_lower = cv_text.lower()
                    
                    # Extract years of experience
                    year_patterns = [
                        r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
                        r'over\s*(\d+)\s*years?',
                        r'(\d{4})\s*-\s*(?:present|current|\d{4})'
                    ]
                    
                    for pattern in year_patterns:
                        matches = re.findall(pattern, cv_lower)
                        if matches:
                            try:
                                years = int(matches[0]) if isinstance(matches[0], str) and matches[0].isdigit() else 0
                                signals['years_experience'] = max(signals['years_experience'], years)
                            except:
                                pass
                    
                    # TECHNOLOGY DEPTH INDICATORS
                    tech_depth = [
                        'architected', 'deployed', 'scaled', 'optimized', 'refactored',
                        'microservices', 'api', 'database', 'cloud', 'ci/cd', 'devops',
                        'github', 'gitlab', 'docker', 'kubernetes', 'testing', 'debugging'
                    ]
                    signals['industry_depth']['technology'] = sum(1 for kw in tech_depth if kw in cv_lower)
                    
                    # HEALTHCARE DEPTH INDICATORS
                    healthcare_depth = [
                        'patient', 'clinical', 'diagnosis', 'treatment', 'medical',
                        'nursing', 'surgery', 'emergency', 'icu', 'rounds',
                        'ehr', 'emr', 'hipaa', 'compliance', 'patient outcomes',
                        'mortality rate', 'recovery rate', 'bedside', 'triage'
                    ]
                    signals['industry_depth']['healthcare'] = sum(1 for kw in healthcare_depth if kw in cv_lower)
                    
                    # FINANCE DEPTH INDICATORS
                    finance_depth = [
                        'audit', 'financial statements', 'gaap', 'ifrs', 'sox',
                        'reconciliation', 'budgeting', 'forecasting', 'valuation',
                        'portfolio', 'investment', 'risk assessment', 'compliance',
                        'cpa', 'cfa', 'financial modeling', 'p&l', 'balance sheet',
                        'revenue', 'profit', 'cost reduction', 'roi'
                    ]
                    signals['industry_depth']['finance'] = sum(1 for kw in finance_depth if kw in cv_lower)
                    
                    # MARKETING DEPTH INDICATORS
                    marketing_depth = [
                        'campaign', 'roi', 'conversion', 'engagement', 'reach',
                        'impressions', 'ctr', 'cpc', 'seo', 'sem', 'ppc',
                        'social media', 'content strategy', 'brand awareness',
                        'market research', 'segmentation', 'a/b testing',
                        'google analytics', 'facebook ads', 'email marketing'
                    ]
                    signals['industry_depth']['marketing'] = sum(1 for kw in marketing_depth if kw in cv_lower)
                    
                    # EDUCATION DEPTH INDICATORS
                    education_depth = [
                        'curriculum', 'lesson plan', 'pedagogy', 'assessment',
                        'student outcomes', 'test scores', 'graduation rate',
                        'classroom management', 'differentiated instruction',
                        'special education', 'iep', 'professional development',
                        'teaching methods', 'learning objectives', 'rubrics'
                    ]
                    signals['industry_depth']['education'] = sum(1 for kw in education_depth if kw in cv_lower)
                    
                    # LEGAL DEPTH INDICATORS
                    legal_depth = [
                        'litigation', 'contract', 'negotiation', 'settlement',
                        'court', 'trial', 'deposition', 'discovery', 'brief',
                        'motion', 'jurisdiction', 'case law', 'statute',
                        'regulatory', 'compliance', 'intellectual property',
                        'patent', 'trademark', 'corporate law', 'due diligence'
                    ]
                    signals['industry_depth']['legal'] = sum(1 for kw in legal_depth if kw in cv_lower)
                    
                    # SALES DEPTH INDICATORS
                    sales_depth = [
                        'quota', 'pipeline', 'lead generation', 'prospecting',
                        'closing', 'deal size', 'revenue', 'territory',
                        'b2b', 'b2c', 'enterprise', 'crm', 'salesforce',
                        'cold calling', 'negotiation', 'upselling', 'cross-selling',
                        'account management', 'customer retention', 'sales cycle'
                    ]
                    signals['industry_depth']['sales'] = sum(1 for kw in sales_depth if kw in cv_lower)
                    
                    # OPERATIONS DEPTH INDICATORS
                    operations_depth = [
                        'supply chain', 'logistics', 'inventory', 'procurement',
                        'vendor management', 'process improvement', 'lean', 'six sigma',
                        'efficiency', 'cost reduction', 'throughput', 'capacity',
                        'quality control', 'safety', 'compliance', 'kpi',
                        'warehouse', 'distribution', 'production'
                    ]
                    signals['industry_depth']['operations'] = sum(1 for kw in operations_depth if kw in cv_lower)
                    
                    # HR DEPTH INDICATORS
                    hr_depth = [
                        'recruitment', 'hiring', 'onboarding', 'retention',
                        'employee engagement', 'performance management', 'talent',
                        'compensation', 'benefits', 'hris', 'workforce planning',
                        'training', 'development', 'succession planning',
                        'diversity', 'inclusion', 'employee relations', 'termination'
                    ]
                    signals['industry_depth']['hr'] = sum(1 for kw in hr_depth if kw in cv_lower)
                    
                    # CREATIVE DEPTH INDICATORS
                    creative_depth = [
                        'portfolio', 'design', 'branding', 'visual identity',
                        'photoshop', 'illustrator', 'indesign', 'figma', 'sketch',
                        'wireframe', 'mockup', 'prototype', 'user interface',
                        'typography', 'color theory', 'composition', 'client work',
                        'creative direction', 'art direction'
                    ]
                    signals['industry_depth']['creative'] = sum(1 for kw in creative_depth if kw in cv_lower)
                    
                    # Extract quantified achievements (UNIVERSAL)
                    achievement_patterns = [
                        r'(\d+)%\s*(?:increase|improvement|growth|reduction|decrease)',
                        r'(?:over|more than|up to)\s*(\d+)\s*(?:clients|projects|patients|students|cases|deals)',
                        r'\$(\d+)(?:k|m|K|M)?\s*(?:revenue|sales|savings|budget)',
                        r'(?:managed|led|supervised)\s*(?:team of\s*)?(\d+)\s*(?:people|employees|staff)',
                        r'(\d+)\+\s*(?:years|projects|clients|patients)'
                    ]
                    
                    for pattern in achievement_patterns:
                        matches = re.findall(pattern, cv_lower)
                        signals['quantified_achievements'].extend(matches)
                    
                    # Extract leadership indicators (UNIVERSAL)
                    leadership_keywords = [
                        'led', 'spearheaded', 'managed', 'directed', 'supervised',
                        'coordinated', 'orchestrated', 'established', 'founded',
                        'pioneered', 'initiated', 'transformed', 'drove', 'executed',
                        'championed', 'mentored', 'trained', 'guided'
                    ]
                    
                    for keyword in leadership_keywords:
                        if keyword in cv_lower:
                            signals['leadership_indicators'].append(keyword)
                    
                    # Extract certifications (UNIVERSAL)
                    cert_patterns = [
                        r'\b(pmp|cpa|cfa|cma|cissp|cisa|ccna|ccnp|aws|azure|gcp)\b',
                        r'\b(certified|certification|license|licensed)\b',
                        r'\b(phd|mba|masters|bachelor|degree)\b'
                    ]
                    
                    for pattern in cert_patterns:
                        matches = re.findall(pattern, cv_lower)
                        signals['certifications'].extend(matches)
                    
                    # Detect specializations
                    if 'wix' in cv_lower or 'webflow' in cv_lower or 'wordpress' in cv_lower:
                        signals['specializations'].append('no-code-platforms')
                    
                    if 'chatgpt' in cv_lower or 'prompt' in cv_lower and 'ai' in cv_lower:
                        signals['specializations'].append('ai-prompting')
                    
                    if 'portfolio' in cv_lower and 'building' in cv_lower:
                        signals['specializations'].append('portfolio-development')
                    
                    return signals
                
                def analyze_cv_universal(cv_text):
                    """
                    UNIVERSAL ANALYSIS - All Industries with Equal Depth
                    """
                    cv_lower = cv_text.lower()
                    signals = extract_universal_depth_signals(cv_text)
                    
                    # Comprehensive career database - ALL INDUSTRIES
                    career_categories = {
                        # TECHNOLOGY
                        'Full-Stack Developer': {
                            'keywords': ['full stack', 'full-stack', 'backend', 'frontend', 'node', 'express', 'django', 'flask', 'api', 'database'],
                            'weight': 4,
                            'industry': 'Technology',
                            'depth_key': 'technology',
                            'minimum_depth': 4,
                            'critical_keywords': ['backend', 'api', 'database']
                        },
                        'Frontend Web Developer': {
                            'keywords': ['html', 'css', 'javascript', 'react', 'angular', 'vue', 'frontend', 'ui/ux', 'responsive', 'web'],
                            'weight': 3,
                            'industry': 'Technology',
                            'depth_key': 'technology',
                            'minimum_depth': 3
                        },
                        'Software Developer': {
                            'keywords': ['python', 'java', 'javascript', 'c++', 'c#', 'software', 'developer', 'git', 'testing', 'debugging'],
                            'weight': 3,
                            'industry': 'Technology',
                            'depth_key': 'technology',
                            'minimum_depth': 3
                        },
                        'DevOps / Cloud Engineer': {
                            'keywords': ['aws', 'azure', 'cloud', 'docker', 'kubernetes', 'devops', 'jenkins', 'ci/cd', 'terraform', 'infrastructure'],
                            'weight': 3,
                            'industry': 'Technology',
                            'depth_key': 'technology',
                            'minimum_depth': 4
                        },
                        'Data Analyst / Data Scientist': {
                            'keywords': ['data', 'analytics', 'analysis', 'sql', 'python', 'statistics', 'tableau', 'power bi', 'visualization'],
                            'weight': 3,
                            'industry': 'Technology',
                            'depth_key': 'technology',
                            'minimum_depth': 3
                        },
                        'No-Code / Low-Code Developer': {
                            'keywords': ['wix', 'webflow', 'squarespace', 'wordpress', 'shopify', 'bubble', 'no-code'],
                            'weight': 3,
                            'industry': 'Technology/No-Code',
                            'depth_key': 'technology',
                            'minimum_depth': 1,
                            'boost_if': 'no-code-platforms' in signals['specializations']
                        },
                        'IT Support / Systems Administrator': {
                            'keywords': ['support', 'help desk', 'troubleshooting', 'windows', 'linux', 'network', 'systems', 'administration'],
                            'weight': 2,
                            'industry': 'Technology',
                            'depth_key': 'technology',
                            'minimum_depth': 2
                        },
                        
                        # HEALTHCARE
                        'Registered Nurse / Clinical Nurse': {
                            'keywords': ['nurse', 'nursing', 'patient', 'clinical', 'rn', 'care', 'medical', 'hospital', 'icu', 'bedside'],
                            'weight': 3,
                            'industry': 'Healthcare',
                            'depth_key': 'healthcare',
                            'minimum_depth': 4
                        },
                        'Medical Doctor / Physician': {
                            'keywords': ['doctor', 'physician', 'medical', 'diagnosis', 'treatment', 'patient', 'clinical', 'medicine', 'md'],
                            'weight': 4,
                            'industry': 'Healthcare',
                            'depth_key': 'healthcare',
                            'minimum_depth': 5
                        },
                        'Healthcare Administrator': {
                            'keywords': ['healthcare', 'hospital', 'clinic', 'medical', 'administration', 'hipaa', 'compliance', 'ehr', 'emr'],
                            'weight': 3,
                            'industry': 'Healthcare',
                            'depth_key': 'healthcare',
                            'minimum_depth': 3
                        },
                        'Pharmacist': {
                            'keywords': ['pharmacy', 'pharmacist', 'medication', 'prescription', 'pharmaceutical', 'drug', 'dispensing'],
                            'weight': 3,
                            'industry': 'Healthcare',
                            'depth_key': 'healthcare',
                            'minimum_depth': 3
                        },
                        
                        # FINANCE
                        'Accountant / CPA': {
                            'keywords': ['accounting', 'accountant', 'cpa', 'audit', 'financial statements', 'gaap', 'tax', 'bookkeeping'],
                            'weight': 3,
                            'industry': 'Finance',
                            'depth_key': 'finance',
                            'minimum_depth': 4
                        },
                        'Financial Analyst': {
                            'keywords': ['financial', 'analyst', 'finance', 'modeling', 'forecasting', 'budgeting', 'valuation', 'roi'],
                            'weight': 3,
                            'industry': 'Finance',
                            'depth_key': 'finance',
                            'minimum_depth': 4
                        },
                        'Investment Banker / Analyst': {
                            'keywords': ['investment', 'banking', 'analyst', 'deals', 'm&a', 'valuation', 'financial modeling', 'portfolio'],
                            'weight': 4,
                            'industry': 'Finance',
                            'depth_key': 'finance',
                            'minimum_depth': 5
                        },
                        'Risk Manager / Compliance Officer': {
                            'keywords': ['risk', 'compliance', 'regulatory', 'audit', 'internal controls', 'sox', 'governance'],
                            'weight': 3,
                            'industry': 'Finance',
                            'depth_key': 'finance',
                            'minimum_depth': 3
                        },
                        
                        # MARKETING
                        'Digital Marketing Specialist': {
                            'keywords': ['digital marketing', 'marketing', 'seo', 'sem', 'ppc', 'social media', 'campaigns', 'analytics'],
                            'weight': 3,
                            'industry': 'Marketing',
                            'depth_key': 'marketing',
                            'minimum_depth': 4
                        },
                        'Content Marketing Manager': {
                            'keywords': ['content', 'marketing', 'strategy', 'blog', 'articles', 'copywriting', 'engagement', 'roi'],
                            'weight': 3,
                            'industry': 'Marketing',
                            'depth_key': 'marketing',
                            'minimum_depth': 3
                        },
                        'Social Media Manager': {
                            'keywords': ['social media', 'facebook', 'instagram', 'twitter', 'linkedin', 'engagement', 'community', 'content'],
                            'weight': 2,
                            'industry': 'Marketing',
                            'depth_key': 'marketing',
                            'minimum_depth': 3
                        },
                        'Brand Manager': {
                            'keywords': ['brand', 'branding', 'marketing', 'positioning', 'strategy', 'awareness', 'identity'],
                            'weight': 3,
                            'industry': 'Marketing',
                            'depth_key': 'marketing',
                            'minimum_depth': 3
                        },
                        
                        # EDUCATION
                        'Teacher / Educator': {
                            'keywords': ['teacher', 'teaching', 'education', 'classroom', 'students', 'curriculum', 'lesson', 'instruction'],
                            'weight': 2,
                            'industry': 'Education',
                            'depth_key': 'education',
                            'minimum_depth': 4
                        },
                        'School Administrator / Principal': {
                            'keywords': ['principal', 'administrator', 'school', 'education', 'leadership', 'curriculum', 'staff', 'budget'],
                            'weight': 3,
                            'industry': 'Education',
                            'depth_key': 'education',
                            'minimum_depth': 5
                        },
                        'Instructional Designer': {
                            'keywords': ['instructional', 'design', 'curriculum', 'elearning', 'training', 'learning', 'development', 'education'],
                            'weight': 3,
                            'industry': 'Education',
                            'depth_key': 'education',
                            'minimum_depth': 3
                        },
                        
                        # LEGAL
                        'Attorney / Lawyer': {
                            'keywords': ['attorney', 'lawyer', 'legal', 'law', 'litigation', 'contract', 'court', 'trial', 'case'],
                            'weight': 4,
                            'industry': 'Legal',
                            'depth_key': 'legal',
                            'minimum_depth': 5
                        },
                        'Paralegal / Legal Assistant': {
                            'keywords': ['paralegal', 'legal', 'assistant', 'research', 'documents', 'filing', 'litigation', 'contract'],
                            'weight': 2,
                            'industry': 'Legal',
                            'depth_key': 'legal',
                            'minimum_depth': 3
                        },
                        'Corporate Counsel': {
                            'keywords': ['corporate', 'counsel', 'legal', 'contracts', 'compliance', 'regulatory', 'commercial'],
                            'weight': 4,
                            'industry': 'Legal',
                            'depth_key': 'legal',
                            'minimum_depth': 5
                        },
                        
                        # SALES
                        'Sales Representative / Account Executive': {
                            'keywords': ['sales', 'selling', 'revenue', 'quota', 'pipeline', 'closing', 'deals', 'clients', 'b2b'],
                            'weight': 2,
                            'industry': 'Sales',
                            'depth_key': 'sales',
                            'minimum_depth': 4
                        },
                        'Business Development Manager': {
                            'keywords': ['business development', 'partnerships', 'growth', 'strategy', 'revenue', 'sales', 'pipeline'],
                            'weight': 3,
                            'industry': 'Sales',
                            'depth_key': 'sales',
                            'minimum_depth': 4
                        },
                        'Account Manager / Client Success': {
                            'keywords': ['account', 'manager', 'client', 'relationship', 'retention', 'upselling', 'customer success'],
                            'weight': 2,
                            'industry': 'Sales',
                            'depth_key': 'sales',
                            'minimum_depth': 3
                        },
                        
                        # OPERATIONS
                        'Operations Manager': {
                            'keywords': ['operations', 'manager', 'logistics', 'supply chain', 'efficiency', 'process', 'improvement'],
                            'weight': 3,
                            'industry': 'Operations',
                            'depth_key': 'operations',
                            'minimum_depth': 4
                        },
                        'Supply Chain Manager': {
                            'keywords': ['supply chain', 'logistics', 'procurement', 'vendor', 'inventory', 'warehouse', 'distribution'],
                            'weight': 3,
                            'industry': 'Operations',
                            'depth_key': 'operations',
                            'minimum_depth': 4
                        },
                        'Quality Assurance Manager': {
                            'keywords': ['quality', 'assurance', 'qa', 'compliance', 'standards', 'inspection', 'control', 'improvement'],
                            'weight': 3,
                            'industry': 'Operations',
                            'depth_key': 'operations',
                            'minimum_depth': 3
                        },
                        
                        # HR
                        'HR Manager / HR Business Partner': {
                            'keywords': ['human resources', 'hr', 'recruitment', 'talent', 'employee', 'hiring', 'onboarding', 'retention'],
                            'weight': 3,
                            'industry': 'Human Resources',
                            'depth_key': 'hr',
                            'minimum_depth': 4
                        },
                        'Recruiter / Talent Acquisition': {
                            'keywords': ['recruiter', 'recruitment', 'hiring', 'talent', 'sourcing', 'interviewing', 'candidates'],
                            'weight': 2,
                            'industry': 'Human Resources',
                            'depth_key': 'hr',
                            'minimum_depth': 3
                        },
                        'Compensation & Benefits Analyst': {
                            'keywords': ['compensation', 'benefits', 'payroll', 'salary', 'bonus', 'incentives', 'hris'],
                            'weight': 3,
                            'industry': 'Human Resources',
                            'depth_key': 'hr',
                            'minimum_depth': 3
                        },
                        
                        # CREATIVE
                        'Graphic Designer': {
                            'keywords': ['graphic design', 'design', 'photoshop', 'illustrator', 'visual', 'branding', 'creative', 'portfolio'],
                            'weight': 3,
                            'industry': 'Creative',
                            'depth_key': 'creative',
                            'minimum_depth': 4
                        },
                        'UX/UI Designer': {
                            'keywords': ['ux', 'ui', 'user experience', 'interface', 'design', 'wireframe', 'prototype', 'figma'],
                            'weight': 3,
                            'industry': 'Creative',
                            'depth_key': 'creative',
                            'minimum_depth': 4
                        },
                        'Art Director / Creative Director': {
                            'keywords': ['art director', 'creative director', 'creative', 'direction', 'design', 'team', 'campaigns'],
                            'weight': 4,
                            'industry': 'Creative',
                            'depth_key': 'creative',
                            'minimum_depth': 5
                        },
                        
                        # SPECIALIZED
                        'Portfolio Developer / Career Tech Specialist': {
                            'keywords': ['portfolio', 'career', 'job seeker', 'wix', 'website builder', 'chatgpt', 'prompts'],
                            'weight': 4,
                            'industry': 'Career Tech',
                            'depth_key': 'technology',
                            'minimum_depth': 2,
                            'boost_if': 'portfolio-development' in signals['specializations']
                        },
                        'ChatGPT / AI Prompt Engineer': {
                            'keywords': ['chatgpt', 'gpt', 'prompt', 'ai', 'artificial intelligence', 'llm'],
                            'weight': 3,
                            'industry': 'AI/Emerging Tech',
                            'depth_key': 'technology',
                            'minimum_depth': 2,
                            'boost_if': 'ai-prompting' in signals['specializations']
                        },
                        'Business Analyst': {
                            'keywords': ['business analyst', 'requirements', 'stakeholder', 'process', 'documentation', 'workflow'],
                            'weight': 3,
                            'industry': 'Business',
                            'depth_key': 'operations',
                            'minimum_depth': 3
                        },
                        'Project Manager': {
                            'keywords': ['project management', 'pmp', 'agile', 'scrum', 'planning', 'coordination', 'delivery'],
                            'weight': 3,
                            'industry': 'Business',
                            'depth_key': 'operations',
                            'minimum_depth': 4
                        },
                    }
                    
                    role_scores = {}
                    
                    for role, details in career_categories.items():
                        keyword_matches = 0
                        matched_keywords = []
                        critical_keywords_found = 0
                        
                        # Count keyword matches
                        for keyword in details['keywords']:
                            if keyword in cv_lower:
                                keyword_matches += 1
                                matched_keywords.append(keyword)
                        
                        # Check critical keywords if specified
                        if 'critical_keywords' in details:
                            for critical_kw in details['critical_keywords']:
                                if critical_kw in cv_lower:
                                    critical_keywords_found += 1
                        
                        if keyword_matches > 0:
                            # Base score
                            base_score = (keyword_matches / len(details['keywords'])) * 100
                            
                            # Get industry depth
                            depth_key = details.get('depth_key')
                            industry_depth = signals['industry_depth'].get(depth_key, 0)
                            minimum_depth = details.get('minimum_depth', 2)
                            
                            # Start with base weight
                            multiplier = details['weight']
                            
                            # DEPTH ANALYSIS - Universal across all industries
                            if industry_depth >= minimum_depth:
                                multiplier += 0.5  # Boost for demonstrated depth
                            elif industry_depth < minimum_depth and minimum_depth >= 4:
                                multiplier -= 0.7  # Penalty for claiming advanced role without depth
                            elif industry_depth < minimum_depth:
                                multiplier -= 0.3  # Smaller penalty for junior roles
                            
                            # Critical keywords check (mainly for technical roles)
                            if 'critical_keywords' in details:
                                if critical_keywords_found < len(details['critical_keywords']):
                                    multiplier -= 0.8  # Heavy penalty if missing critical skills
                            
                            # Specialization boost
                            if details.get('boost_if'):
                                if isinstance(details['boost_if'], bool) and details['boost_if']:
                                    multiplier += 0.7
                                elif isinstance(details['boost_if'], str) and eval(details['boost_if']):
                                    multiplier += 0.7
                            
                            # Experience boost (universal)
                            if signals['years_experience'] >= 5:
                                multiplier += 0.5
                            elif signals['years_experience'] >= 3:
                                multiplier += 0.3
                            elif signals['years_experience'] >= 1:
                                multiplier += 0.1
                            
                            # Quantified achievements boost (universal)
                            if len(signals['quantified_achievements']) >= 5:
                                multiplier += 0.4
                            elif len(signals['quantified_achievements']) >= 3:
                                multiplier += 0.2
                            
                            # Leadership indicators boost (universal)
                            if len(signals['leadership_indicators']) >= 5:
                                multiplier += 0.3
                            elif len(signals['leadership_indicators']) >= 3:
                                multiplier += 0.15
                            
                            # Certifications boost (universal)
                            if len(signals['certifications']) >= 2:
                                multiplier += 0.3
                            elif len(signals['certifications']) >= 1:
                                multiplier += 0.15
                            
                            # Calculate final score
                            weighted_score = min(95, base_score * multiplier / 2)
                            weighted_score = max(0, weighted_score)
                            
                            # Determine confidence level
                            if industry_depth >= minimum_depth and len(signals['quantified_achievements']) >= 3:
                                confidence = 'High'
                            elif industry_depth >= minimum_depth - 1:
                                confidence = 'Medium'
                            else:
                                confidence = 'Low'
                            
                            role_scores[role] = {
                                'score': int(weighted_score),
                                'matches': matched_keywords,
                                'industry': details['industry'],
                                'depth_score': industry_depth,
                                'minimum_depth': minimum_depth,
                                'confidence': confidence
                            }
                    
                    sorted_roles = sorted(role_scores.items(), key=lambda x: x[1]['score'], reverse=True)
                    
                    return sorted_roles[:12], signals
                
                roles, signals = analyze_cv_universal(st.session_state.cv_content)
                
                st.success("✅ Universal Analysis Complete!")
                st.markdown("---")
                
                # Show experience insights
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    if signals['years_experience'] > 0:
                        st.metric("Experience", f"{signals['years_experience']}+ yrs")
                    else:
                        st.metric("Experience", "Entry Level")
                
                with col2:
                    achievement_count = len(signals['quantified_achievements'])
                    st.metric("Achievements", achievement_count, delta="Good" if achievement_count >= 3 else "Add more")
                
                with col3:
                    leadership_count = len(set(signals['leadership_indicators']))
                    st.metric("Leadership", leadership_count, delta="Strong" if leadership_count >= 5 else "Build more")
                
                with col4:
                    cert_count = len(set(signals['certifications']))
                    st.metric("Certifications", cert_count, delta="Excellent" if cert_count >= 2 else "Consider adding")
                
                # Show industry depth analysis
                st.markdown("---")
                st.subheader("🌍 Industry Depth Analysis")
                st.caption("Depth score shows demonstrated experience in each industry")
                
                industry_cols = st.columns(5)
                industry_names = ['Technology', 'Healthcare', 'Finance', 'Marketing', 'Education']
                industry_keys = ['technology', 'healthcare', 'finance', 'marketing', 'education']
                
                for idx, (name, key) in enumerate(zip(industry_names, industry_keys)):
                    with industry_cols[idx]:
                        depth = signals['industry_depth'][key]
                        if depth >= 4:
                            st.success(f"**{name}**\n\n{depth}/10")
                        elif depth >= 2:
                            st.info(f"**{name}**\n\n{depth}/10")
                        else:
                            st.caption(f"**{name}**\n\n{depth}/10")
                
                industry_cols2 = st.columns(5)
                industry_names2 = ['Legal', 'Sales', 'Operations', 'HR', 'Creative']
                industry_keys2 = ['legal', 'sales', 'operations', 'hr', 'creative']
                
                for idx, (name, key) in enumerate(zip(industry_names2, industry_keys2)):
                    with industry_cols2[idx]:
                        depth = signals['industry_depth'][key]
                        if depth >= 4:
                            st.success(f"**{name}**\n\n{depth}/10")
                        elif depth >= 2:
                            st.info(f"**{name}**\n\n{depth}/10")
                        else:
                            st.caption(f"**{name}**\n\n{depth}/10")
                
                if signals['specializations']:
                    st.markdown("---")
                    st.info(f"🎯 **Detected Specializations:** {', '.join(signals['specializations'])}")
                
                st.markdown("---")
                st.subheader("💼 Recommended Career Paths")
                st.caption("🌍 **Universal Analysis:** Ranked by demonstrated experience depth and quantified achievements across all industries")
                
                if roles:
                    col1, col2 = st.columns(2)
                    
                    for idx, (role, data) in enumerate(roles):
                        with col1 if idx % 2 == 0 else col2:
                            score = data['score']
                            industry = data.get('industry', '')
                            confidence = data.get('confidence', 'Medium')
                            depth_score = data.get('depth_score', 0)
                            min_depth = data.get('minimum_depth', 2)
                            
                            if score >= 75:
                                st.success(f"**{role}**")
                                st.metric("Match Score", f"{score}%", f"⭐ Excellent ({confidence})")
                            elif score >= 50:
                                st.info(f"**{role}**")
                                st.metric("Match Score", f"{score}%", f"✓ Strong ({confidence})")
                            else:
                                st.warning(f"**{role}**")
                                st.metric("Match Score", f"{score}%", f"○ Potential ({confidence})")
                            
                            st.caption(f"🏢 {industry} | Depth: {depth_score}/{min_depth}")
                            
                            with st.expander("📋 Matching qualifications"):
                                st.write("**Your skills:**")
                                st.write(", ".join(data['matches'][:12]))
                            
                            st.markdown("---")
                    
                    st.success("""
                    ✅ **Next Steps:**
                    1. Focus on roles with **High confidence** - these match your demonstrated experience
                    2. For **Medium/Low confidence** roles, add quantified achievements and depth indicators
                    3. Use these **exact titles** when searching jobs
                    4. Go to **Tab 2** for ATS job matching
                    """)
                    
                    # Universal gap analysis
                    st.markdown("---")
                    st.subheader("🔍 Profile Enhancement Recommendations")
                    
                    if signals['years_experience'] < 2:
                        st.warning("⚠️ **Experience:** Add more years or projects to strengthen senior role applications")
                    
                    if len(signals['quantified_achievements']) < 3:
                        st.info("💡 **Achievements:** Add numbers! (30% increase, $50K saved, 100+ clients served)")
                    
                    if len(signals['leadership_indicators']) < 3:
                        st.info("💡 **Leadership:** Use stronger verbs (led, spearheaded, managed, directed)")
                    
                    if len(signals['certifications']) == 0:
                        st.info("💡 **Certifications:** Industry certifications boost credibility (PMP, CPA, AWS, etc.)")
                    
                    # Show which industry has most depth
                    max_depth_industry = max(signals['industry_depth'], key=signals['industry_depth'].get)
                    max_depth_score = signals['industry_depth'][max_depth_industry]
                    
                    if max_depth_score >= 4:
                        st.success(f"🎯 **Strongest Industry:** {max_depth_industry.title()} (Depth: {max_depth_score}/10)")
                    
                else:
                    st.warning("⚠️ Unable to identify role matches. Add more specific skills and experience.")
                
        else:
            st.warning("⚠️ Please upload or paste your CV first")

# TAB 2: INTELLIGENT ATS MATCHING
with tab2:
    st.header("Step 2: Intelligent ATS Job Matching")
    st.write("""
    🧠 **Context-Aware ATS System:** Goes beyond keyword matching to understand synonyms, 
    related skills, experience levels, and transferable competencies.
    """)
    
    if not st.session_state.cv_content:
        st.error("⚠️ **REQUIRED: Go to Tab 1 first to upload your CV!**")
        st.info("👈 Click 'Analyze CV' tab above")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 Your CV")
        
        if st.session_state.cv_content:
            cv_lines = st.session_state.cv_content.split('\n')
            
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
                "CV Content (auto-loaded):",
                value=preview_text,
                height=400,
                disabled=True
            )
            
            word_count = len(st.session_state.cv_content.split())
            st.caption(f"📊 {word_count} words | {len(st.session_state.cv_content)} characters")
            st.success("✅ CV loaded for analysis!")
        else:
            st.info("👈 Upload CV in Tab 1 first")
    
    with col2:
        st.subheader("💼 Job Description")
        jd_text = st.text_area(
            "Paste complete job description:",
            height=400,
            placeholder="""Paste the full job posting including:
- Job title and level
- Required qualifications
- Responsibilities
- Technical skills
- Experience requirements
- Education/certifications

More details = more accurate analysis!""",
            key="jd_match"
        )

    def extract_context_aware_keywords(text):
        """
        INTELLIGENT KEYWORD EXTRACTION
        - Understands synonyms and related terms
        - Recognizes skill variations
        - Context-aware matching
        """
        text_lower = text.lower()
        
        # Extract base words
        words = re.findall(r'\b[a-z]{4,}\b', text_lower)
        
        # Comprehensive stop words
        stop_words = {
            'that', 'with', 'have', 'this', 'from', 'were', 'been', 'will', 
            'would', 'there', 'their', 'what', 'when', 'where', 'which', 'while',
            'about', 'after', 'before', 'other', 'such', 'than', 'then', 'these',
            'those', 'very', 'your', 'they', 'should', 'could', 'years', 'work',
            'working', 'including', 'related', 'ability', 'strong', 'good', 'excellent',
            'must', 'able', 'well', 'also', 'make', 'take', 'provide', 'ensure'
        }
        
        keywords = set([w for w in words if w not in stop_words and len(w) > 3])
        
        # SYNONYM MAPPING - Universal across industries
        synonym_groups = {
            # Technology
            'programming': ['coding', 'development', 'software development'],
            'javascript': ['js', 'ecmascript'],
            'python': ['py'],
            'database': ['sql', 'nosql', 'data storage'],
            'frontend': ['front-end', 'front end', 'client side'],
            'backend': ['back-end', 'back end', 'server side'],
            'api': ['rest', 'restful', 'web service'],
            
            # Healthcare
            'patient care': ['patient management', 'clinical care', 'bedside care'],
            'nurse': ['nursing', 'rn', 'registered nurse'],
            'medical': ['clinical', 'healthcare'],
            
            # Finance
            'accounting': ['bookkeeping', 'financial reporting'],
            'audit': ['auditing', 'internal audit'],
            'financial analysis': ['financial modeling', 'forecasting'],
            
            # Marketing
            'marketing': ['digital marketing', 'advertising', 'promotion'],
            'social media': ['social', 'facebook', 'instagram', 'twitter'],
            'seo': ['search engine optimization', 'search optimization'],
            
            # Sales
            'sales': ['selling', 'business development'],
            'client': ['customer', 'account', 'client relations'],
            
            # Management (universal)
            'managed': ['led', 'directed', 'supervised', 'coordinated'],
            'project management': ['program management', 'project coordination'],
        }
        
        # Expand keywords with synonyms
        expanded_keywords = keywords.copy()
        for main_term, synonyms in synonym_groups.items():
            if main_term in text_lower:
                expanded_keywords.add(main_term)
            for syn in synonyms:
                if syn in text_lower:
                    expanded_keywords.add(main_term)
        
        # Extract job-relevant phrases (same as before but enhanced)
        important_phrases = [
            # Technology
            'machine learning', 'deep learning', 'artificial intelligence', 'data science',
            'data analysis', 'business intelligence', 'software development', 'web development',
            'full stack', 'front end', 'back end', 'cloud computing', 'devops',
            'database management', 'network security', 'cyber security', 'project management',
            'agile methodology', 'version control', 'quality assurance', 'user experience',
            
            # Healthcare
            'patient care', 'clinical practice', 'emergency medicine', 'primary care',
            'mental health', 'patient outcomes', 'medical records', 'healthcare administration',
            
            # Finance
            'financial analysis', 'financial reporting', 'financial modeling', 'budget management',
            'risk management', 'investment banking', 'portfolio management', 'audit compliance',
            
            # Marketing
            'digital marketing', 'content marketing', 'social media', 'email marketing',
            'seo optimization', 'market research', 'brand management', 'lead generation',
            
            # Education
            'curriculum development', 'instructional design', 'classroom management',
            'student assessment', 'professional development',
            
            # Legal
            'legal research', 'contract management', 'regulatory compliance',
            'intellectual property', 'corporate law',
            
            # Sales
            'business development', 'sales strategy', 'account management', 'client relations',
            
            # Operations
            'supply chain', 'process improvement', 'operations management', 'quality control',
            
            # HR
            'talent acquisition', 'employee relations', 'performance management',
        ]
        
        found_phrases = set()
        for phrase in important_phrases:
            if phrase in text_lower:
                found_phrases.add(phrase)
        
        return expanded_keywords, found_phrases
    
    def intelligent_ats_matching(cv_text, jd_text):
        """
        INTELLIGENT ATS MATCHING
        - Context-aware synonym matching
        - Experience level detection
        - Transferable skills recognition
        - Gap analysis with suggestions
        """
        
        cv_keywords, cv_phrases = extract_context_aware_keywords(cv_text)
        jd_keywords, jd_phrases = extract_context_aware_keywords(jd_text)
        
        # Direct matches
        keyword_matches = cv_keywords.intersection(jd_keywords)
        phrase_matches = cv_phrases.intersection(jd_phrases)
        
        # Missing items
        missing_keywords = jd_keywords - cv_keywords
        missing_phrases = jd_phrases - cv_phrases
        
        # INTELLIGENT ANALYSIS
        # Detect experience level required
        cv_lower = cv_text.lower()
        jd_lower = jd_text.lower()
        
        experience_signals = {
            'senior': ['senior', 'lead', 'principal', 'director', '10+ years', '8+ years'],
            'mid': ['mid-level', 'intermediate', '5+ years', '3-5 years'],
            'junior': ['junior', 'entry', '1-2 years', 'graduate']
        }
        
        jd_level = 'mid'  # default
        for level, indicators in experience_signals.items():
            if any(ind in jd_lower for ind in indicators):
                jd_level = level
                break
        
        cv_experience_years = 0
        year_matches = re.findall(r'(\d+)\+?\s*years?\s*(?:of\s*)?experience', cv_lower)
        if year_matches:
            cv_experience_years = max([int(y) for y in year_matches if y.isdigit()])
        
        # Calculate base score
        total_jd_items = len(jd_keywords) + (len(jd_phrases) * 2.5)
        total_matches = len(keyword_matches) + (len(phrase_matches) * 2.5)
        
        if total_jd_items == 0:
            compatibility_score = 0
        else:
            compatibility_score = (total_matches / total_jd_items) * 100
        
        # INTELLIGENT ADJUSTMENTS
        # Experience level matching
        if jd_level == 'senior' and cv_experience_years < 5:
            compatibility_score *= 0.85  # Reduce if under-experienced
        elif jd_level == 'junior' and cv_experience_years > 8:
            compatibility_score *= 0.95  # Slight reduce if over-qualified
        
        # Boost for leadership indicators in CV
        leadership_words = ['led', 'managed', 'directed', 'spearheaded']
        if any(word in cv_lower for word in leadership_words):
            compatibility_score += 3
        
        # Boost for quantified achievements
        if re.search(r'\d+%', cv_text):
            compatibility_score += 2
        
        compatibility_score = min(int(compatibility_score), 99)
        
        # CONTEXTUAL GAPS
        contextual_insights = {
            'missing_critical': [],
            'transferable_skills': [],
            'experience_gap': None
        }
        
        # Identify critical missing skills
        critical_tech = {'python', 'java', 'javascript', 'sql', 'aws', 'azure'}
        critical_missing = missing_keywords.intersection(critical_tech)
        if critical_missing:
            contextual_insights['missing_critical'] = list(critical_missing)
        
        # Detect transferable skills
        if 'project management' in jd_phrases and 'managed' in cv_lower:
            contextual_insights['transferable_skills'].append('project management experience (demonstrated through "managed")')
        
        if 'data analysis' in jd_phrases and 'analytics' in cv_lower:
            contextual_insights['transferable_skills'].append('analytics experience')
        
        # Experience gap
        if jd_level == 'senior' and cv_experience_years < 5:
            contextual_insights['experience_gap'] = f"Job requires senior level ({jd_level}), you have {cv_experience_years} years"
        
        return compatibility_score, keyword_matches, phrase_matches, missing_keywords, missing_phrases, contextual_insights
    
    def create_pdf_report(analysis_text, match_score):
        """PDF report generation"""
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
        story.append(Paragraph("Intelligent ATS Analysis Report", styles['Heading3']))
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
        story.append(Paragraph("CV-Job Matcher Pro | Intelligent ATS Analysis", footer_style))
        story.append(Paragraph("Universal Career Matching System", footer_style))
        
        doc.build(story)
        buffer.seek(0)
        return buffer

    # ATS ANALYSIS BUTTON
    if st.button("🧠 Run Intelligent ATS Analysis", type="primary", key="ats_analyze_btn", use_container_width=True):
        if not st.session_state.cv_content:
            st.error("❌ **ERROR:** Go to Tab 1 and upload your CV first!")
        elif not jd_text:
            st.warning("⚠️ **WARNING:** Paste the job description above")
        else:
            with st.spinner("🧠 Intelligent ATS system analyzing with context awareness..."):
                try:
                    score, keyword_matches, phrase_matches, missing_keywords, missing_phrases, insights = intelligent_ats_matching(
                        st.session_state.cv_content, 
                        jd_text
                    )
                    
                    st.success("✅ Intelligent Analysis Complete!")
                    st.markdown("---")
                    
                    # Score display
                    st.subheader("🎯 ATS COMPATIBILITY RATING")
                    col1, col2, col3 = st.columns([1,2,1])
                    with col2:
                        if score >= 80:
                            st.success(f"# {score}%")
                            st.success("**✅ EXCELLENT - High ATS pass rate!**")
                            recommendation = "Your CV is well-optimized. Apply with confidence!"
                        elif score >= 60:
                            st.warning(f"# {score}%")
                            st.warning("**⚠️ GOOD - Will likely pass but can improve**")
                            recommendation = "Solid match. Adding missing keywords will strengthen your application."
                        else:
                            st.error(f"# {score}%")
                            st.error("**❌ NEEDS WORK - Low ATS pass rate**")
                            recommendation = "Significant gaps detected. Focus on adding missing skills below."
                    
                    st.info(f"**💡 Recommendation:** {recommendation}")
                    
                    # Show contextual insights if any
                    if insights.get('experience_gap'):
                        st.warning(f"⏰ **Experience Gap:** {insights['experience_gap']}")
                    
                    if insights.get('transferable_skills'):
                        st.success(f"✨ **Transferable Skills Detected:** {', '.join(insights['transferable_skills'])}")
                    
                    st.markdown("---")
                    
                    # Detailed analysis
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ FOUND IN YOUR CV")
                        
                        st.write(f"**Matching Keywords:** {len(keyword_matches)}")
                        if keyword_matches:
                            st.success("These keywords passed ATS:")
                            keyword_display = ", ".join(sorted(list(keyword_matches))[:40])
                            st.write(keyword_display)
                        
                        st.markdown("---")
                        
                        st.write(f"**Matching Key Phrases:** {len(phrase_matches)}")
                        if phrase_matches:
                            st.success("✨ Industry-specific phrases found:")
                            phrase_display = ", ".join(sorted(list(phrase_matches))[:25])
                            st.write(phrase_display)
                    
                    with col2:
                        st.subheader("❌ MISSING FROM YOUR CV")
                        
                        st.write(f"**Missing Keywords:** {len(missing_keywords)}")
                        if missing_keywords:
                            st.error("⚠️ **CRITICAL:** ATS looking for these:")
                            critical_missing = sorted(list(missing_keywords))[:40]
                            st.write(", ".join(critical_missing))
                            
                            if insights.get('missing_critical'):
                                st.warning(f"🔴 **High Priority:** {', '.join(insights['missing_critical'])}")
                        
                        st.markdown("---")
                        
                        st.write(f"**Missing Key Phrases:** {len(missing_phrases)}")
                        if missing_phrases:
                            st.warning("Important phrases not detected:")
                            missing_phrase_display = ", ".join(sorted(list(missing_phrases))[:25])
                            st.write(missing_phrase_display)
                    
                    # Recommendations
                    st.markdown("---")
                    st.subheader("📋 INTELLIGENT RECOMMENDATIONS")
                    
                    if score >= 80:
                        st.success("""
                        **✅ Your CV is ATS-Ready!**
                        
                        1. Maintain all matching keywords
                        2. Use standard formatting (avoid tables/images)
                        3. Save as .docx or .pdf
                        4. Apply confidently!
                        """)
                    elif score >= 60:
                        st.warning("""
                        **⚠️ Strong Foundation - Quick Wins Available**
                        
                        1. Add the missing high-priority keywords listed above
                        2. Incorporate job-specific phrases naturally
                        3. Quantify achievements with numbers
                        4. Mirror exact terminology from job description
                        5. Retest after updates!
                        """)
                    else:
                        st.error("""
                        **❌ Significant Optimization Required**
                        
                        1. **URGENT:** Add missing critical skills you actually possess
                        2. Use industry-standard terminology from job description
                        3. Restructure with clear headers: Skills, Experience, Education
                        4. Avoid graphics/tables that ATS can't read
                        5. Consider tailoring CV specifically for this role
                        6. Update and retest here!
                        """)
                    
                    # Download report
                    analysis_report = f"""
INTELLIGENT ATS COMPATIBILITY ANALYSIS
{'='*70}

COMPATIBILITY SCORE: {score}%

SUMMARY:
{recommendation}

KEYWORDS FOUND ({len(keyword_matches)}):
{', '.join(sorted(list(keyword_matches))[:50])}

KEY PHRASES FOUND ({len(phrase_matches)}):
{', '.join(sorted(list(phrase_matches))[:30])}

MISSING KEYWORDS ({len(missing_keywords)}):
{', '.join(sorted(list(missing_keywords))[:50])}

MISSING PHRASES ({len(missing_phrases)}):
{', '.join(sorted(list(missing_phrases))[:30])}

CONTEXTUAL INSIGHTS:
{insights.get('experience_gap', 'Experience level matches')}
Transferable Skills: {', '.join(insights.get('transferable_skills', ['None detected']))}

RECOMMENDATIONS:
- Focus on missing high-priority keywords
- Use exact terminology from job description
- Add quantified achievements
- Ensure ATS-friendly formatting
- Retest after updates

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Intelligent ATS Analysis - CV-Job Matcher Pro
                    """
                    
                    st.markdown("---")
                    st.subheader("📥 Download Analysis Report")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.download_button(
                            label="📄 Download TXT",
                            data=analysis_report,
                            file_name=f"ats_analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col2:
                        try:
                            pdf_buffer = create_pdf_report(analysis_report, score)
                            st.download_button(
                                label="📑 Download PDF",
                                data=pdf_buffer,
                                file_name=f"ats_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.info("PDF unavailable - TXT download available above")
                    
                except Exception as e:
                    st.error(f"❌ Analysis Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About This Tool")
    st.write("""
    **CV-Job Matcher Pro**
    
    🌍 **Universal System:**
    
    **Tab 1:** Cross-industry expert
    - ALL industries analyzed equally
    - Experience depth detection
    - Quantified achievements tracking
    - 40+ career paths
    
    **Tab 2:** Intelligent ATS
    - Context-aware matching
    - Synonym recognition
    - Transferable skills detection
    - Experience level analysis
    """)
    
    st.header("🌍 Industries Covered")
    st.info("""
    Technology • Healthcare • Finance
    Marketing • Education • Legal
    Sales • Operations • HR • Creative
    
    **Equal depth analysis for all!**
    """)
    
    st.header("⚡ What Makes This Advanced")
    st.success("""
    ✅ Universal depth analysis (not just tech)
    ✅ Context-aware ATS matching
    ✅ Synonym & related term recognition
    ✅ Transferable skills detection
    ✅ Experience level matching
    ✅ Quantified achievement tracking
    ✅ Leadership indicator detection
    ✅ Certification recognition
    """)

st.markdown("---")
st.markdown("*Universal Career Intelligence System | Advanced ATS Matching*")