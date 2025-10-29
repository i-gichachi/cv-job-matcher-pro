# 🎯 CV-Job Matcher Pro

**Multi-Industry Career Analysis & ATS Optimizer**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://cv-job-matcher-pro.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

**Moringa School AI Capstone Project - October 2025**

---

## 📖 **What is CV-Job Matcher Pro?**

CV-Job Matcher Pro is a web-based career analysis tool that helps job seekers understand which careers match their skills and optimize their CVs for Applicant Tracking Systems (ATS). 

**The Key Innovation:** Unlike most CV analysis tools that focus primarily on technology roles, this system analyzes experience depth equally across 10 different industries using industry-specific depth indicators.

**Live Demo:** [cv-job-matcher-pro.streamlit.app](https://cv-job-matcher-pro.streamlit.app/)

---

## 🎯 **The Problem This Solves**

### **Industry Bias in Career Tools**

After testing existing CV analysis tools (Jobscan, Resume Worded), I discovered they analyze technology roles deeply but give superficial analysis to other professions:

- **Software Developers** get analyzed with depth indicators like: `microservices`, `CI/CD`, `scaled`, `architected`
- **Nurses** get generic keywords like: `patient`, `care`, `nursing`
- **Teachers** barely get analyzed at all

**Impact:** 75% of jobs are non-tech, but most career tools are built by developers for developers.

### **My Solution**

Built industry-specific depth indicator sets for **10 industries equally**:
- Technology: 17 depth indicators
- Healthcare: 19 depth indicators  
- Finance: 20 depth indicators
- Marketing: 19 depth indicators
- Education: 15 depth indicators
- Legal: 20 depth indicators
- Sales: 20 depth indicators
- Operations: 19 depth indicators
- HR: 18 depth indicators
- Creative: 19 depth indicators

**Each profession gets equal quality analysis.**

---

## ✨ **Features**

### **Tab 1: Multi-Industry Career Analysis**

Analyzes your CV across **40+ career paths** in **10 industries**:

**Industries Covered:**
- 🖥️ **Technology** - Full-Stack Developer, Frontend Developer, DevOps Engineer, Data Analyst, Software Developer, IT Support
- 🏥 **Healthcare** - Registered Nurse, Physician, Healthcare Administrator, Pharmacist
- 💰 **Finance** - Accountant/CPA, Financial Analyst, Investment Banker, Risk Manager
- 📢 **Marketing** - Digital Marketing Specialist, Content Manager, Social Media Manager, Brand Manager
- 📚 **Education** - Teacher/Educator, School Administrator, Instructional Designer
- ⚖️ **Legal** - Attorney/Lawyer, Paralegal, Corporate Counsel
- 💼 **Sales** - Sales Representative, Business Development Manager, Account Manager
- 🏭 **Operations** - Operations Manager, Supply Chain Manager, Quality Assurance Manager
- 👥 **HR** - HR Manager, Recruiter, Compensation & Benefits Analyst
- 🎨 **Creative** - Graphic Designer, UX/UI Designer, Art Director

**Analysis Includes:**
- ✅ **Industry Depth Scoring** (0-10 per industry based on specific indicators)
- ✅ **Experience Level Detection** (Entry, Mid, Senior)
- ✅ **Quantified Achievements Tracking** (percentages, numbers, metrics)
- ✅ **Leadership Indicators** (led, managed, directed, spearheaded)
- ✅ **Certification Recognition** (PMP, CPA, CFA, RN, AWS, etc.)
- ✅ **Confidence Ratings** (High/Medium/Low based on demonstrated depth)
- ✅ **Career Match Scores** (0-95% compatibility)

### **Tab 2: ATS Job Matching**

Match your CV against job descriptions using ATS-style analysis:

**Features:**
- ✅ **Keyword Matching** - Identifies keywords found and missing
- ✅ **Phrase Extraction** - Detects industry-specific phrases (e.g., "project management", "patient care")
- ✅ **Compatibility Scoring** - Rates match from 0-99%
- ✅ **Gap Analysis** - Shows exactly what's missing from your CV
- ✅ **Weighted Scoring** - Phrases count 2.5x more than single keywords
- ✅ **Downloadable Reports** - Export as TXT or PDF

---

## 🚀 **Getting Started**

### **Option 1: Use Online (Recommended)**

No installation needed! Visit: **[cv-job-matcher-pro.streamlit.app](https://cv-job-matcher-pro.streamlit.app/)**

### **Option 2: Run Locally**

**Prerequisites:**
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

**Installation Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/i-gichachi/cv-job-matcher-pro.git
cd cv-job-matcher-pro

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
streamlit run app.py
```

**Access the app:** Open your browser to `http://localhost:8501`

---

## 📁 **Project Structure**
```
cv-job-matcher-pro/
│
├── app.py                      # Main application (1200+ lines)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── AI_PROMPT_JOURNAL.md       # AI-assisted learning documentation
├── TOOLKIT_DOCUMENT.md        # Complete beginner's guide
├── .gitignore                 # Git ignore rules
```

---

## 🛠️ **Technology Stack**

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | Streamlit 1.32 | Web application framework |
| **Language** | Python 3.10 | Core programming language |
| **PDF Processing** | PyPDF2 3.0.1 | Extract text from PDF files |
| **PDF Generation** | ReportLab 4.1.0 | Generate downloadable reports |
| **Deployment** | Streamlit Cloud | Free hosting and deployment |
| **Version Control** | Git + GitHub | Code management |

**Why Streamlit?**
- Fast development (4-day project timeline)
- Built-in file upload widgets
- Python-native (no HTML/CSS/JavaScript needed)
- Perfect for data-focused applications
- Free deployment on Streamlit Cloud

---

## 📖 **How to Use**

### **Step 1: Analyze Your CV (Tab 1)**

1. Click the **"Analyze CV"** tab
2. **Upload** your CV (PDF or TXT) OR **paste** your CV text directly
3. Click **"Analyze My CV"** button
4. **Review results:**
   - Experience metrics (years, achievements, leadership score)
   - Industry depth scores (shows which industries you have experience in)
   - Top 10-12 career matches with confidence ratings
   - Enhancement recommendations

**Example Output:**
```
Experience: 4+ years
Achievements: 6 quantified results found
Leadership: 8 indicators detected
Certifications: 2 found

Industry Depth Scores:
Technology: 8/10 ✅
Marketing: 5/10 ℹ️
Sales: 3/10

Top Matches:
1. Frontend Web Developer: 85% (High Confidence)
2. Software Developer: 72% (Medium Confidence)
3. Digital Marketing Specialist: 58% (Medium Confidence)
```

### **Step 2: Match Against Job Description (Tab 2)**

1. Click the **"Match to Job"** tab
2. Your CV is **automatically loaded** from Tab 1
3. **Paste** the complete job description (copy from LinkedIn, Indeed, company website)
4. Click **"Run ATS Analysis"** button
5. **Review results:**
   - ATS compatibility score (0-99%)
   - Matching keywords found in your CV
   - Missing keywords you should add
   - Matching industry phrases
   - Missing critical phrases
   - Actionable recommendations
6. **Download** your analysis report (TXT or PDF)

**Example Output:**
```
ATS Compatibility Score: 67%
⚠️ GOOD - Will likely pass but can improve

Found in Your CV:
- Keywords: javascript, react, html, css, api, database (25 total)
- Phrases: web development, front end, user experience (5 total)

Missing from Your CV:
- Keywords: typescript, docker, kubernetes, ci/cd (15 total)
- Phrases: agile methodology, version control (3 total)

Recommendation: Add missing keywords you actually possess, 
especially: typescript, docker, agile methodology
```

---

## 🔍 **How It Works**

### **Industry-Specific Depth Scoring**

Each industry has custom depth indicators that show expertise level:

**Technology Depth Indicators (17):**
```python
['architected', 'deployed', 'scaled', 'optimized', 'refactored',
 'microservices', 'api', 'database', 'cloud', 'ci/cd', 'devops',
 'github', 'docker', 'kubernetes', 'testing', 'debugging', 'gitlab']
```

**Healthcare Depth Indicators (19):**
```python
['patient', 'clinical', 'diagnosis', 'treatment', 'medical',
 'nursing', 'surgery', 'emergency', 'icu', 'rounds', 'ehr', 'emr',
 'hipaa', 'compliance', 'patient outcomes', 'mortality rate',
 'recovery rate', 'bedside', 'triage']
```

**Finance Depth Indicators (20):**
```python
['audit', 'financial statements', 'gaap', 'ifrs', 'sox',
 'reconciliation', 'budgeting', 'forecasting', 'valuation',
 'portfolio', 'investment', 'risk assessment', 'compliance',
 'cpa', 'cfa', 'financial modeling', 'p&l', 'balance sheet',
 'revenue', 'cost reduction']
```

**Scoring Logic:**
```
Depth Score = Count of depth indicators found in CV
Confidence = High if depth >= minimum_threshold (usually 4)
             Medium if depth >= minimum - 1
             Low if depth < minimum - 1
```

### **Career Matching Algorithm**
```python
For each career role:
    1. Count keyword matches in CV
    2. Calculate base_score = (matches / total_keywords) × 100
    3. Get industry depth score from CV
    4. Apply multiplier based on:
       - Base weight (2-4 depending on role seniority)
       - Depth adjustment (+0.5 if meets minimum, -0.7 if below)
       - Experience boost (+0.1 to +0.5 based on years)
       - Achievement boost (+0.2 to +0.4 based on count)
       - Leadership boost (+0.15 to +0.3 based on indicators)
       - Certification boost (+0.15 to +0.3 based on count)
    5. Final_score = base_score × multiplier / 2
    6. Cap at 95% (perfection is rare)
```

### **ATS Matching Logic**
```python
1. Extract keywords from CV and Job Description
   - Remove stop words (the, and, with, etc.)
   - Keep words 4+ characters
   
2. Extract important phrases
   - Industry-specific: "project management", "patient care"
   - Hardcoded list of 80+ common professional phrases
   
3. Compare CV vs Job Description
   - keyword_matches = CV_keywords ∩ JD_keywords
   - phrase_matches = CV_phrases ∩ JD_phrases
   
4. Calculate score
   - Phrases weighted 2.5× (more valuable than keywords)
   - Score = (matches + phrase_matches×2.5) / (total + total_phrases×2.5) × 100
   - Cap at 99%
```

---

## 📊 **Understanding Your Scores**

### **Career Match Scores**

| Score Range | Rating | Meaning |
|-------------|--------|---------|
| 75-95% | ⭐ Excellent Fit | Strong match, apply with confidence |
| 50-74% | ✓ Strong Fit | Good match, consider applying |
| 25-49% | ○ Potential Fit | Some alignment, may need skill building |
| Below 25% | ✗ Weak Fit | Limited match, major skill gaps |

### **ATS Compatibility Scores**

| Score Range | Rating | Action Needed |
|-------------|--------|---------------|
| 80-99% | ✅ Excellent | CV is ATS-optimized, apply confidently |
| 60-79% | ⚠️ Good | Add missing keywords, then apply |
| 40-59% | ❌ Fair | Significant gaps, tailor CV first |
| Below 40% | 🚫 Poor | Major optimization needed before applying |

### **Confidence Ratings**

- **High Confidence** - You have demonstrated depth in this field (depth score meets minimum + quantified achievements)
- **Medium Confidence** - You have some experience but could strengthen depth indicators
- **Low Confidence** - Keywords match but limited evidence of depth (may need more experience or better CV writing)

---

## 🧪 **Testing & Validation**

### **Test Cases**

**Test 1: Technology Professional**
```
Input: CV with JavaScript, React, Node.js, API development, 5 years experience
Expected: Frontend Developer 80-85%, Software Developer 65-75%
Actual: ✅ Passed
```

**Test 2: Healthcare Professional**
```
Input: CV with patient care, ICU experience, clinical rounds, 8 years nursing
Expected: Registered Nurse 80-90% with High confidence
Actual: ✅ Passed
```

**Test 3: Finance Professional**
```
Input: CV with audit, GAAP, financial modeling, CPA, 6 years
Expected: Accountant/CPA 85-95% with High confidence
Actual: ✅ Passed
```

**Test 4: Cross-Industry CV**
```
Input: CV with marketing campaigns + financial reporting + team management
Expected: Multiple industry matches with varying depth scores
Actual: ✅ Passed - Marketing 6/10, Finance 4/10, Operations 3/10
```

---

## ⚠️ **Common Issues & Solutions**

### **Issue 1: "PDF uploaded but no text extracted"**

**Cause:** PDF is scanned image or has complex formatting

**Solutions:**
- Convert PDF to Word, then save as new PDF
- Use online PDF to Text converter
- Copy-paste CV text directly instead of uploading
- Ensure PDF is text-based, not scanned image

---

### **Issue 2: "Low scores despite good qualifications"**

**Cause 1:** CV uses different terminology than system expects

**Solution:** Review "Matching qualifications" in expander - see which keywords matched. Add synonyms of your skills.

**Cause 2:** Lack of quantified achievements

**Solution:** Add numbers! Instead of "Managed projects" write "Managed 5 cross-functional projects resulting in 30% efficiency gain"

**Cause 3:** Missing industry depth indicators

**Solution:** Use specific industry terms. Instead of "Helped patients" write "Provided clinical care to 20+ ICU patients daily"

---

### **Issue 3: "ATS score is lower than expected"**

**Cause:** Job description uses specific terms not in your CV

**Solution:**
1. Review "Missing Keywords" section carefully
2. Add keywords you actually have experience with (don't lie!)
3. Use exact phrases from job description (e.g., if JD says "project management" don't say "managed projects")
4. Retest after updates

---

### **Issue 4: "Application crashed or won't load"**

**Cause:** File too large or connection issue

**Solutions:**
- Ensure file is under 5MB
- Try pasting text instead of uploading
- Refresh page and try again
- Check internet connection
- Try different browser (Chrome recommended)

---

### **Issue 5: "Port 8501 already in use (local installation)"**

**Cause:** Another Streamlit app is running

**Solutions:**
```bash
# Option 1: Use different port
streamlit run app.py --server.port 8502

# Option 2: Kill existing process
# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID_NUMBER> /F

# macOS/Linux:
lsof -ti:8501 | xargs kill -9
```

---

## 🔮 **Future Enhancements**

### **Planned Features (Not Yet Implemented)**

**Phase 1: Enhanced Intelligence**
- [ ] Integration with Claude API for contextual analysis
- [ ] Synonym recognition (understand "coding" = "programming")
- [ ] Transferable skills detection
- [ ] Multi-language support (Spanish, French, Swahili)

**Phase 2: Professional Tools**
- [ ] User accounts with CV history
- [ ] A/B testing for CV variations
- [ ] ATS-optimized resume templates
- [ ] Job board integration (LinkedIn, Indeed)
- [ ] Interview question generation based on CV

**Phase 3: Additional Industries**
- [ ] Construction, Retail, Hospitality analysis
- [ ] Government/Public Sector roles
- [ ] Non-profit sector careers

**Phase 4: Business Features**
- [ ] Freemium model (basic free, advanced paid)
- [ ] Career coach partnerships
- [ ] University career services licensing

---

## 🎓 **Learning & Development**

### **Development Timeline**

**4-Day Capstone Project:**
- **Day 1 (Oct 27):** Technology selection, Streamlit learning, environment setup
- **Day 2 (Oct 28):** CV upload, basic career matching, UI design
- **Day 3 (Oct 29):** Discovered industry bias problem, designed multi-industry solution, implemented depth analysis
- **Day 4 (Oct 30):** ATS matching system, testing, bug fixes, documentation, deployment

**Total Time Investment:** ~25 hours

### **Key Learning Moments**

**Breakthrough Discovery:**
> "While testing, I uploaded a nurse friend's CV. The system gave her 'Healthcare Professional - 42%' while my developer CV got 'Software Developer - 85%' with similar experience depth. That's when I realized the algorithm had tech bias. I rebuilt it with industry-specific indicators."

**Technical Skills Acquired:**
- ✅ Streamlit framework (0 → production level in 4 days)
- ✅ Text processing and keyword extraction
- ✅ Algorithm design with fairness considerations
- ✅ PDF manipulation (PyPDF2)
- ✅ PDF generation (ReportLab)
- ✅ Session state management
- ✅ Error handling and validation
- ✅ Git version control
- ✅ Cloud deployment (Streamlit Cloud)

**AI-Assisted Development:**
- Used Claude AI for learning acceleration (18 documented prompts)
- 2.5x faster development vs. traditional learning
- AI helped with concepts, not copy-paste code
- Made all architectural and design decisions independently

### **Capstone Requirements Met**

✅ **Learned new technology** (Streamlit framework)  
✅ **Built functional project** (deployed and live)  
✅ **Documented AI learning process** (AI_PROMPT_JOURNAL.md)  
✅ **Created beginner's guide** (TOOLKIT_DOCUMENT.md)  
✅ **Comprehensive README** (this file)  
✅ **Version controlled** (Git + GitHub)  
✅ **Testing & iteration** (multiple CV tests across industries)  
✅ **Out-of-the-box thinking** (solved industry bias problem)

---

## 🤝 **Contributing**

This is an educational project, but improvements are welcome!

**Areas for Contribution:**
- Additional industry depth indicators
- Bug fixes and edge case handling
- UI/UX improvements
- Documentation enhancements
- Test cases for validation

**How to Contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add YourFeature'`)
6. Push to your fork (`git push origin feature/YourFeature`)
7. Open a Pull Request

---

## 📜 **License**

**Educational Project** - Moringa School AI Capstone 2025

**Usage Rights:**
- ✅ Free to use for personal learning
- ✅ Fork and modify for your own projects
- ✅ Share with attribution to original author
- ❌ Commercial use requires permission

**Attribution Format:**
```
CV-Job Matcher Pro by Ian Gichachi
Moringa School AI Capstone Project 2025
https://github.com/i-gichachi/cv-job-matcher-pro
```

---

## 👤 **Author**

**Ian Gichachi**  
Full-Stack Developer | Career Tech Specialist | AI Enthusiast

**Background:**
- 4+ years experience in software development
- Specialized in portfolio development and career tech
- Moringa School Software Development Graduate (2023)
- KCA University - BSc Information Technology (2022)

**Contact:**
- 🌐 Portfolio: [iangichachi.com](https://iangichachi.com/)
- 💼 LinkedIn: [Ian Gichachi](https://www.linkedin.com/in/ian-gichachi-b0890a23b/)
- 📧 Email: iangichachi@gmail.com
- 🐙 GitHub: [@i-gichachi](https://github.com/i-gichachi)
- 📱 Phone: +254 720 064950

---

## 🙏 **Acknowledgments**

**Project Inspiration:**
Working as a Portfolio & Software Developer at Careers Without Borders (a career coaching startup), I noticed my colleagues spending hours manually analyzing client CVs across different industries - healthcare, finance, education, sales, and tech. They'd review each CV, identify career matches, and optimize for ATS systems, but this process was time-consuming and didn't scale.

**The Problem I Wanted to Solve:**
- My team manually analyzes 20+ CVs per month across diverse professions
- Each analysis takes 2-3 hours of expert review time
- Existing automated tools (Jobscan, Resume Worded) only work well for tech roles
- Our non-tech clients (nurses, teachers, accountants) still needed manual analysis
- Team was overwhelmed with workload as client demand grew

**My Goal:**
Lighten the load on my colleagues by creating a faster option - a tool that could do the initial CV analysis across ALL industries (not just tech), giving them a solid starting point. Instead of starting from scratch, they could review the automated analysis and add their expert insights on top.

**The Solution:**
This capstone project builds a multi-industry CV analysis system that:
1. Handles the initial heavy lifting (industry matching, depth scoring, ATS analysis)
2. Works equally well for nurses, teachers, accountants, and developers
3. Reduces analysis time from 2-3 hours to 15-20 minutes of expert review
4. Allows the team to serve more clients without burning out
5. Frees up time for high-value activities (interview prep, strategy sessions)

**Real-World Testing:**
During development, I tested with anonymized client CVs from our database (with permission) across multiple industries. The goal: make sure the automated analysis was good enough that my colleagues could trust it as a starting point, not just another tool to check.

**Impact Goal:**
If successful, this could help our small team scale from 20 clients/month to 50+ clients/month without hiring more analysts - just by automating the initial analysis phase.

**Special Thanks:**
- **Moringa School** - For the AI Access Program, structured capstone framework, and encouraging innovative thinking
- **Capstone Mentor** - For feedback on "thinking out of the box" and questioning industry norms
- **Claude (Anthropic)** - For AI-assisted learning that accelerated development
- **Streamlit Team** - For creating an accessible framework for data applications
- **Open Source Community** - For PyPDF2, ReportLab, and Python ecosystem
- **Beta Testers** - Friends who tested CVs from diverse fields (healthcare, finance, education, sales)


**Mentors & Advisors:**
- Moringa School Capstone Program
- Career coaches who provided industry insights
- Software development peers for code review

---

## 📞 **Support**

### **Need Help?**
**Questions:**
- 📧 Email: iangichachi@gmail.com

**Feature Requests:**
- Submit via GitHub Issues with "Feature Request" label
- Explain the use case and expected benefit

**Live Demo Issues:**
- Try refreshing the page
- Clear browser cache
- Try different browser (Chrome recommended)
- If problem persists, report via email

---

## 📚 **Additional Documentation**

**Complete Guides:**
- 📖 [Complete Toolkit Guide](./TOOLKIT_DOCUMENT.md) - Step-by-step beginner's guide with examples
- 🤖 [AI Learning Journey](./AI_PROMPT_JOURNAL.md) - 18 prompts documenting AI-assisted development process
- 🐙 [GitHub Repository](https://github.com/i-gichachi/cv-job-matcher-pro) - Full source code

**Quick Links:**
- 🌐 [Live Demo](https://cv-job-matcher-pro.streamlit.app/)


---

## 📈 **Project Statistics**

**Code Metrics:**
- Total Lines of Code: ~1,200
- Python Files: 1 (app.py)
- Documentation Files: 3 (README, Toolkit, AI Journal)
- Industries Analyzed: 10
- Career Paths Covered: 40+
- Depth Indicators: 180+ (across all industries)
- Development Time: 30 hours over 4 days

**Technical Metrics:**
- Languages: Python 100%
- Framework: Streamlit
- Dependencies: 3 (Streamlit, PyPDF2, ReportLab)
- Python Version: 3.8+
- Deployment: Streamlit Cloud (free tier)

---

## 🔗 **External Resources**

**Streamlit Learning:**
- [Official Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [30 Days of Streamlit](https://30days.streamlit.app/)

**ATS Understanding:**
- [How ATS Works - Jobscan](https://www.jobscan.co/blog/8-things-you-need-to-know-about-applicant-tracking-systems/)
- [ATS Guide - TopResume](https://www.topresume.com/career-advice/what-is-an-applicant-tracking-system-ats)

**CV Writing Best Practices:**
- [Harvard Resume Guide](https://careerservices.fas.harvard.edu/resources/resumes-cover-letters/)
- [The Muse - Resume Keywords](https://www.themuse.com/advice/resume-keywords)

---

## 💬 **Frequently Asked Questions**

**Q: Is this tool free to use?**  
A: Yes! The live demo at cv-job-matcher-pro.streamlit.app is completely free with no account required.

**Q: Do you store my CV data?**  
A: No. All processing happens in your browser session. When you close the tab, your data is gone. Nothing is saved on servers.

**Q: Can this replace career coaches?**  
A: No. This tool provides data-driven insights, but career coaches offer personalized advice, interview prep, and strategic guidance that algorithms can't replicate.

**Q: Why does my CV get different scores for different roles?**  
A: Each role has different keyword requirements and minimum depth thresholds. Your CV may have strong depth in one industry but not another.

**Q: Can I use this for job applications in other countries?**  
A: The depth indicators are designed for international standards, but some terminology may be US/Kenya-focused. The principles apply globally.

**Q: How accurate is the ATS scoring?**  
A: The system mimics real ATS keyword matching, but actual ATS systems vary by company. Use this as a guide, not a guarantee.

**Q: Can I suggest new career categories?**  
A: Yes! Submit suggestions via GitHub Issues. Include the role name and 10-15 depth indicators that show expertise in that role.

---

**Built with Streamlit, Python, and AI-Assisted Learning**  
**Moringa School AI Capstone Project - October 2025**

*Making career analysis fair across all professions*

---

*Last Updated: October 30, 2025*
*Version: 1.0*
