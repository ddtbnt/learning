# 🤖 Data Science & Machine Learning Learning Roadmap

> 🎯 **Mục tiêu:** Trở thành Data Scientist / ML Engineer + sẵn sàng thi & pass 4 chứng chỉ hàng đầu ngành Data / AI / Cloud  
>
> 🏆 **Chứng chỉ mục tiêu:**
> - TensorFlow Developer Certificate  
> - Microsoft Certified: Azure Data Scientist Associate  
> - Google Professional Data Engineer  
> - AWS Certified Data Analytics – Specialty  
>
> ⚙️ **Phương pháp học:**
> FOUNDATION → DATA ANALYSIS → MACHINE LEARNING → DEEP LEARNING → PROJECT END-TO-END → CLOUD (MLOPS / DATA ENGINEERING) → MOCK EXAM → CERTIFICATION PASS  

---

# 🧠 Tổng quan lộ trình

Math + Programming (Foundation)  
→ Data Analysis (EDA + SQL + Insight)  
→ Machine Learning (Scikit-learn + Model building)  
→ Deep Learning (TensorFlow / Neural Networks)  
→ Project thực tế (End-to-End ML System)  
→ Cloud (MLOps / Data Engineering / Big Data Systems)  
→ Certification (4 chứng chỉ mục tiêu)  
→ Job Data Scientist / ML Engineer  


# 📌 1. Foundation Learning Path (Offline – Nền tảng)

🎯 Mục tiêu: Nắm chắc toán + Python + xử lý dữ liệu  

## Nội dung chính:
- Python for Data Science  
- Numpy / Pandas  
- Data Visualization  
- Math (Linear Algebra, Statistics, Probability)  
- Data Cleaning  

## Mindmap:
<!-- Dán mindmap LOCAL vào đây -->

```
Data Science Foundation Path (From Zero → ML Ready)
│
│ 
│ 
├─ 0. Setup môi trường (Environment Setup – BẮT BUỘC)
│   │
│   ├─ 0.1 Yêu cầu phần cứng
│   │   ├─ RAM: ≥ 8GB (khuyến nghị 16GB)
│   │   ├─ CPU: ≥ 4 cores
│   │   ├─ Ổ cứng: ≥ 20GB trống
│   │   └─ OS: Windows / Linux / macOS
│   │
│   ├─ 0.2 Cài đặt Python
│   │   ├─ Tải từ: python.org
│   │   ├─ Version: Python 3.10+
│   │   │
│   │   ├─ Windows
│   │   │   ├─ Tick "Add Python to PATH"
│   │   │   └─ Kiểm tra: python --version
│   │   │
│   │   ├─ Linux (Ubuntu)
│   │   │   ├─ sudo apt update
│   │   │   ├─ sudo apt install python3 python3-pip
│   │   │   └─ python3 --version
│   │   │
│   │   └─ Mục tiêu
│   │       └─ Chạy được Python CLI
│   │
│   ├─ 0.3 Cài Anaconda (Khuyến nghị cho người mới)
│   │   ├─ Bao gồm:
│   │   │   ├─ NumPy
│   │   │   ├─ Pandas
│   │   │   ├─ Jupyter Notebook
│   │   │   └─ matplotlib
│   │   │
│   │   └─ Mục tiêu
│   │       └─ Có môi trường Data Science sẵn
│   │
│   ├─ 0.4 Visual Studio Code (VS Code)
│   │   ├─ Cài VS Code
│   │   ├─ Extensions:
│   │   │   ├─ Python
│   │   │   └─ Jupyter
│   │   │
│   │   └─ Mục tiêu
│   │       └─ Code + debug dễ dàng
│   │
│   ├─ 0.5 Git (Version Control – Quản lý code)
│   │   ├─ git init / add / commit
│   │   ├─ push GitHub
│   │   └─ clone repo
│   │
│   ├─ 0.6 Virtual Environment (venv – môi trường ảo)
│   │   │
│   │   │
│   │   ├─ pip (Python package manager)
│   │   │   ├─ pip install
│   │   │   ├─ pip freeze
│   │   │   └─ requirements.txt
│   │   │
│   │   ├─ Tạo môi trường
│   │   │   └─ python -m venv venv
│   │   │
│   │   ├─ Activate môi trường
│   │   │
│   │   │   ├─ Windows
│   │   │   │   └─ venv\Scripts\activate
│   │   │   │
│   │   │   ├─ Linux / macOS
│   │   │   │   └─ source venv/bin/activate
│   │   │   │
│   │   │   └─ Dấu hiệu thành công
│   │   │       └─ (venv) xuất hiện trước terminal
│   │   │
│   │   ├─ Cài thư viện
│   │   │   └─ pip install numpy pandas matplotlib
│   │   │
│   │   └─ Mục tiêu
│   │       └─ Quản lý dependency riêng từng project
│   │
│   └─ 0.7 Checkpoint (BẮT BUỘC đạt)
│       ├─ ✔️ Chạy được Python
│       ├─ ✔️ Cài được thư viện bằng pip
│       ├─ ✔️ Dùng được Jupyter Notebook
│       ├─ ✔️ Activate được venv
│       └─ ✔️ Push code lên GitHub
│ 
│ 
├─ 1. Python cơ bản (Core Programming)
│   │
│   ├─ 1.1 Syntax & Control Flow
│   │   ├─ Variables, data types
│   │   ├─ if / else
│   │   ├─ for / while loop
│   │   └─ list comprehension
│   │
│   ├─ 1.2 Data Structures
│   │   ├─ List
│   │   ├─ Tuple
│   │   ├─ Dictionary
│   │   └─ Set
│   │
│   ├─ 1.3 Functions & Modules
│   │   ├─ def function
│   │   ├─ lambda
│   │   ├─ import module
│   │   └─ virtual environment (venv)
│   │
│   ├─ 1.4 OOP cơ bản
│   │   ├─ Class / Object
│   │   ├─ __init__
│   │   └─ Encapsulation
│   │
│   └─ 1.5 Mục tiêu
│   │   └─ Viết code Python sạch & hiểu logic
│   │
│   └─  1.6 Debug & Error Handling
│       ├─ try / except
│       ├─ đọc error message
│       └─ debug bằng print / VS Code
│   
├─ 2. Data Libraries (Cốt lõi Data Science)
│   │
│   ├─ 2.1 NumPy
│   │   ├─ ndarray
│   │   ├─ vector operations
│   │   ├─ broadcasting
│   │   └─ matrix operations
│   │
│   ├─ 2.2 Pandas
│   │   ├─ DataFrame / Series
│   │   ├─ read_csv / read_excel
│   │   ├─ filtering & slicing
│   │   ├─ groupby / aggregation
│   │   └─ merge / join
│   │
│   ├─ 2.3 Data Cleaning
│   │   ├─ Missing values
│   │   ├─ Duplicate data
│   │   ├─ Data type conversion
│   │   ├─ Feature scaling
│   │   ├─ Outliers detection
│   │   └─ Encoding (categorical → số)
│   │
│   └─ 2.4 Mục tiêu
│       └─ Làm sạch & thao tác dữ liệu hiệu quả
│
├─ 3. Data Visualization
│   │
│   ├─ 3.1 Matplotlib
│   │   ├─ line chart
│   │   ├─ bar chart
│   │   └─ histogram
│   │
│   ├─ 3.2 Seaborn
│   │   ├─ heatmap
│   │   ├─ pairplot
│   │   └─ distribution plot
│   │
│   ├─ 3.3 Storytelling with Data
│   │   ├─ chọn biểu đồ phù hợp
│   │   ├─ highlight insight
│   │   └─ tránh misleading charts
│   │
│   └─ 3.4 Mục tiêu
│       └─ Biến data thành insight trực quan
│
├─ 4. Toán nền tảng (RẤT QUAN TRỌNG)
│   │
│   ├─ 4.1 Linear Algebra
│   │   ├─ vector
│   │   ├─ matrix
│   │   ├─ dot product
│   │   └─ eigenvalues (cơ bản)
│   │
│   ├─ 4.2 Probability
│   │   ├─ random variables
│   │   ├─ distributions (normal, binomial)
│   │   └─ conditional probability
│   │
│   ├─ 4.3 Statistics
│   │   ├─ mean / median / mode
│   │   ├─ variance / std
│   │   ├─ hypothesis testing
│   │   └─ correlation
│   │
│   └─ 4.4 Mục tiêu
│       └─ Hiểu bản chất ML algorithm
│
├─ 5. Data Handling & Workflow
│   │
│   ├─ 5.1 File Handling
│   │   ├─ CSV / Excel
│   │   ├─ JSON
│   │   └─ API data
│   │
│   ├─ 5.2 Jupyter Notebook
│   │   ├─ code + markdown
│   │   ├─ visualization inline
│   │   └─ experiment workflow
│   │
│   ├─ 5.3 Git cơ bản
│   │   ├─ git init / add / commit
│   │   └─ push GitHub
│   │
│   └─ 5.4 Mục tiêu
│       └─ Workflow chuẩn của Data Scientist
│
├─ 6. Mini Project (BẮT BUỘC)
│   │
│   ├─ Dataset ví dụ
│   │   ├─ Titanic
│   │   ├─ Sales data
│   │   └─ COVID dataset
│   │
│   ├─ Workflow
│   │   ├─ Load data
│   │   ├─ Clean data
│   │   ├─ Analyze (EDA)
│   │   └─ Visualize
│   │
│   └─ Kết quả
│       └─ Notebook hoàn chỉnh (portfolio)
│
├─ 7. Insight quan trọng
│   ├─ Python là công cụ, không phải mục tiêu
│   ├─ 80% thời gian = data cleaning
│   ├─ Math giúp hiểu ML sâu hơn
│   ├─ Visualization = communication skill
│   └─ Không hiểu data = không làm được ML
│
└─ 8. Checkpoint (BẮT BUỘC đạt)
    ├─ ✔️ Thành thạo Pandas & NumPy
    ├─ ✔️ Làm sạch dataset thực tế
    ├─ ✔️ Vẽ được biểu đồ & giải thích
    ├─ ✔️ Hiểu toán cơ bản cho ML
    └─ ✔️ Có ít nhất 1 project hoàn chỉnh
```
---

# 📊 2. Data Analysis Path

🎯 Mục tiêu: Phân tích dữ liệu & rút insight để hỗ trợ ra quyết định kinh doanh (Business Decision Making)

## Nội dung chính:
- Exploratory Data Analysis (EDA)  
- SQL  
- Data Visualization nâng cao  
- Business insight  

## Mindmap:

```
Data Analysis Path (From Data → Insight → Decision)
│
├─ 0. Environment Setup (Thiết lập môi trường – BẮT BUỘC)
│   │
│   ├─ 0.1 Core Tools (Công cụ nền tảng)
│   │   ├─ Python (>= 3.10)
│   │   ├─ Anaconda / Miniconda (Data environment)
│   │   ├─ Jupyter Notebook / JupyterLab
│   │   ├─ VS Code (code editor)
│   │   └─ Git + GitHub (version control)
│   │
│   ├─ 0.2 Database Tools (SQL environment)
│   │   ├─ PostgreSQL (khuyến nghị)
│   │   ├─ MySQL (phổ biến)
│   │   ├─ SQLite (học cơ bản)
│   │   └─ DBeaver / pgAdmin (GUI quản lý DB)
│   │
│   ├─ 0.3 Data Libraries (Python stack)
│   │   ├─ pandas
│   │   ├─ numpy
│   │   ├─ matplotlib
│   │   ├─ seaborn
│   │   └─ plotly (interactive)
│   │
│   ├─ 0.4 BI Tools (Business Intelligence)
│   │   ├─ Power BI
│   │   ├─ Tableau
│   │   └─ Looker Studio (Google)
│   │
│   └─ 0.5 Goal
│       └─ Có full environment sẵn sàng cho Data Analyst job
│
├─ 1. Exploratory Data Analysis (EDA – Phân tích khám phá dữ liệu)
│   │
│   ├─ 1.1 Data Understanding (Hiểu dữ liệu)
│   │   ├─ Dataset structure (rows / columns)
│   │   ├─ Data types (numeric / categorical / datetime)
│   │   ├─ head() / tail()
│   │   ├─ info() (missing values + types)
│   │   └─ describe() (stat summary)
│   │
│   ├─ 1.2 Data Cleaning (Làm sạch dữ liệu)
│   │   ├─ Missing values
│   │   │   ├─ dropna()
│   │   │   ├─ fillna()
│   │   │   └─ imputation (mean/median/mode)
│   │   │
│   │   ├─ Duplicate data
│   │   │   └─ drop_duplicates()
│   │   │
│   │   ├─ Data type fixing
│   │   │   ├─ datetime conversion
│   │   │   ├─ numeric conversion
│   │   │   └─ categorical encoding (label/one-hot basic)
│   │   │
│   │   ├─ Outliers handling
│   │   │   ├─ IQR method
│   │   │   ├─ Z-score
│   │   │   └─ boxplot detection
│   │   │
│   │   └─ Data consistency
│   │       ├─ standardization (format)
│   │       ├─ fix spelling/categories
│   │       └─ remove invalid values
│   │
│   ├─ 1.3 Univariate Analysis
│   │   ├─ distribution
│   │   ├─ histogram
│   │   ├─ boxplot
│   │   ├─ bar chart
│   │   └─ value_counts()
│   │
│   ├─ 1.4 Bivariate Analysis
│   │   ├─ correlation
│   │   ├─ scatter plot
│   │   ├─ groupby comparison
│   │   └─ pivot table
│   │
│   ├─ 1.5 Multivariate Analysis
│   │   ├─ correlation matrix
│   │   ├─ heatmap
│   │   ├─ pairplot
│   │   └─ feature relationships
│   │
│   └─ 1.6 Goal
│       └─ Hiểu dữ liệu trước khi phân tích / ML
│
├─ 2. SQL (Structured Query Language)
│   │
│   ├─ 2.1 Basic SQL
│   │   ├─ SELECT
│   │   ├─ WHERE
│   │   ├─ ORDER BY
│   │   └─ LIMIT
│   │
│   ├─ 2.2 Aggregation
│   │   ├─ COUNT / SUM / AVG / MIN / MAX
│   │   ├─ GROUP BY
│   │   └─ HAVING
│   │
│   ├─ 2.3 JOINs
│   │   ├─ INNER JOIN
│   │   ├─ LEFT JOIN
│   │   ├─ RIGHT JOIN
│   │   └─ FULL JOIN (concept)
│   │
│   ├─ 2.4 Advanced SQL
│   │   ├─ Subquery
│   │   ├─ CTE (WITH)
│   │   ├─ Window Functions
│   │   │   ├─ ROW_NUMBER()
│   │   │   ├─ RANK()
│   │   │   └─ OVER (PARTITION BY)
│   │   │
│   │   └─ Time-series analysis
│   │
│   └─ 2.5 Goal
│       └─ Extract & transform data từ database
│
├─ 3. Data Visualization nâng cao
│   │
│   ├─ 3.1 Visualization Tools
│   │   ├─ Matplotlib
│   │   ├─ Seaborn
│   │   ├─ Plotly (interactive)
│   │   └─ pandas plotting
│   │
│   ├─ 3.2 BI Tools (Business Intelligence)
│   │   ├─ Power BI
│   │   ├─ Tableau
│   │   └─ Looker Studio
│   │
│   ├─ 3.3 Business Dashboards
│   │   ├─ KPI dashboard
│   │   ├─ Sales dashboard
│   │   ├─ Customer dashboard (CLV, churn)
│   │   └─ Marketing dashboard (CAC, ROI)
│   │
│   ├─ 3.4 Data Storytelling
│   │   ├─ đặt câu hỏi đúng (ask why)
│   │   ├─ chọn chart phù hợp
│   │   ├─ highlight insight
│   │   └─ tránh misleading visualization
│   │
│   └─ 3.5 Goal
│       └─ Trình bày data cho business users dễ hiểu
│
├─ 4. Business Insight (Tư duy kinh doanh)
│   │
│   ├─ 4.1 Business Metrics
│   │   ├─ Revenue
│   │   ├─ Profit
│   │   ├─ Cost
│   │   ├─ Conversion Rate
│   │   ├─ Retention
│   │   └─ Churn Rate
│   │
│   ├─ 4.2 Analytical Thinking
│   │   ├─ 5 Whys (why analysis)
│   │   ├─ Root Cause Analysis
│   │   ├─ Hypothesis building
│   │   └─ Data-driven decision making
│   │
│   ├─ 4.3 A/B Testing
│   │   ├─ control vs experiment
│   │   ├─ p-value (statistical significance)
│   │   └─ decision making
│   │
│   ├─ 4.4 Use Cases
│   │   ├─ Customer segmentation
│   │   ├─ Sales optimization
│   │   ├─ Marketing performance
│   │   └─ Churn prediction logic
│   │
│   └─ 4.5 Goal
│       └─ Biến data → business decision có giá trị
│
├─ 5. Mini Project (BẮT BUỘC)
│   │
│   ├─ 5.1 Project Types
│   │   ├─ Sales analysis
│   │   ├─ Customer analysis
│   │   ├─ Churn analysis
│   │   └─ Marketing analysis
│   │
│   ├─ 5.2 Workflow (End-to-End)
│   │   ├─ SQL extract data
│   │   ├─ Data cleaning (Python)
│   │   ├─ EDA
│   │   ├─ Visualization
│   │   ├─ Insight generation
│   │   └─ Recommendation
│   │
│   ├─ 5.3 Output
│   │   ├─ Dashboard (Power BI / Tableau)
│   │   ├─ Notebook (Jupyter)
│   │   ├─ Report (Markdown / PDF)
│   │   └─ GitHub portfolio
│   │
│   └─ 5.4 Goal
│       └─ Portfolio sẵn sàng xin việc Data Analyst
│
├─ 6. Key Industry Skills
│   ├─ Data Analysis = asking right questions
│   ├─ SQL is mandatory skill in all companies
│   ├─ Visualization = communication tool
│   ├─ Business context = core of insight
│   ├─ 80% work = data cleaning + understanding
│   └─ Communication > technical in many DA jobs
│
└─ 7. Checkpoint (JOB READY)
    ├─ ✔ EDA thành thạo (Python + pandas)
    ├─ ✔ SQL (JOIN + GROUP BY + Window functions)
    ├─ ✔ Dashboard Power BI / Tableau
    ├─ ✔ Insight logic rõ ràng + có storytelling
    ├─ ✔ 1–3 project hoàn chỉnh
    └─ ✔ GitHub portfolio publish
```
---

# 🤖 3. Machine Learning Path

🎯 Mục tiêu: Xây model dự đoán  

## Nội dung chính:
- Supervised Learning  
- Unsupervised Learning  
- Model evaluation  
- Feature engineering  

## Mindmap:
<!-- Dán mindmap MACHINE LEARNING vào đây -->

```
Machine Learning Path (From Data → Model → Prediction → Deployment)
│
├─ 0. ML Environment Setup (BẮT BUỘC)
│   │
│   ├─ 0.1 Core Tools
│   │   ├─ Python (>= 3.10)
│   │   ├─ Jupyter Notebook / JupyterLab
│   │   ├─ VS Code
│   │   └─ Git + GitHub
│   │
│   ├─ 0.2 ML Libraries
│   │   ├─ numpy
│   │   ├─ pandas
│   │   ├─ scikit-learn
│   │   ├─ matplotlib
│   │   ├─ seaborn
│   │   └─ scipy
│   │
│   ├─ 0.3 Deep Learning (chuẩn bị sớm)
│   │   ├─ TensorFlow
│   │   └─ Keras
│   │
│   └─ 0.4 Goal
│       └─ Sẵn sàng build ML pipeline end-to-end
│
├─ 1. Machine Learning Fundamentals (Nền tảng ML)
│   │
│   ├─ 1.1 ML Overview
│   │   ├─ Machine Learning là gì
│   │   ├─ AI vs ML vs DL
│   │   ├─ Types of ML problems
│   │   │   ├─ Regression
│   │   │   ├─ Classification
│   │   │   └─ Clustering
│   │
│   ├─ 1.2 ML Workflow
│   │   ├─ Data collection
│   │   ├─ Data preprocessing
│   │   ├─ Feature engineering
│   │   ├─ Model training
│   │   ├─ Evaluation
│   │   └─ Deployment
│   │
│   └─ 1.3 Goal
│       └─ Hiểu toàn bộ pipeline ML end-to-end
│
├─ 2. Supervised Learning (Học có giám sát)
│   │
│   ├─ 2.1 Regression Models
│   │   ├─ Linear Regression
│   │   ├─ Multiple Linear Regression
│   │   ├─ Polynomial Regression
│   │   └─ Regularization (Ridge, Lasso)
│   │
│   ├─ 2.2 Classification Models
│   │   ├─ Logistic Regression
│   │   ├─ K-Nearest Neighbors (KNN)
│   │   ├─ Support Vector Machine (SVM)
│   │   ├─ Decision Tree
│   │   └─ Random Forest
│   │
│   ├─ 2.3 Ensemble Methods
│   │   ├─ Bagging
│   │   ├─ Boosting (XGBoost / LightGBM)
│   │   └─ Voting Classifier
│   │
│   └─ 2.4 Goal
│       └─ Build predictive models chính xác cao
│
├─ 3. Unsupervised Learning (Học không giám sát)
│   │
│   ├─ 3.1 Clustering
│   │   ├─ K-Means
│   │   ├─ Hierarchical Clustering
│   │   └─ DBSCAN
│   │
│   ├─ 3.2 Dimensionality Reduction
│   │   ├─ PCA (Principal Component Analysis)
│   │   ├─ t-SNE (visualization)
│   │   └─ Feature reduction
│   │
│   ├─ 3.3 Association Rules
│   │   ├─ Apriori Algorithm
│   │   └─ Market Basket Analysis
│   │
│   └─ 3.4 Goal
│       └─ Tìm pattern ẩn trong dữ liệu
│
├─ 4. Feature Engineering (RẤT QUAN TRỌNG)
│   │
│   ├─ 4.1 Data Transformation
│   │   ├─ Scaling (StandardScaler / MinMaxScaler)
│   │   ├─ Normalization
│   │   └─ Log transformation
│   │
│   ├─ 4.2 Feature Creation
│   │   ├─ Interaction features
│   │   ├─ Time-based features
│   │   └─ Domain-based features
│   │
│   ├─ 4.3 Encoding
│   │   ├─ One-hot encoding
│   │   ├─ Label encoding
│   │   └─ Target encoding (advanced)
│   │
│   ├─ 4.4 Feature Selection
│   │   ├─ Correlation filtering
│   │   ├─ Feature importance
│   │   └─ Recursive Feature Elimination (RFE)
│   │
│   └─ 4.5 Goal
│       └─ Tăng accuracy model bằng dữ liệu tốt hơn
│
├─ 5. Model Evaluation (Đánh giá mô hình)
│   │
│   ├─ 5.1 Regression Metrics
│   │   ├─ MAE (Mean Absolute Error)
│   │   ├─ MSE (Mean Squared Error)
│   │   ├─ RMSE
│   │   └─ R² Score
│   │
│   ├─ 5.2 Classification Metrics
│   │   ├─ Accuracy
│   │   ├─ Precision
│   │   ├─ Recall
│   │   ├─ F1 Score
│   │   └─ Confusion Matrix
│   │
│   ├─ 5.3 Validation Techniques
│   │   ├─ Train/Test Split
│   │   ├─ K-Fold Cross Validation
│   │   └─ Stratified Sampling
│   │
│   └─ 5.4 Goal
│       └─ Đánh giá model đúng cách, tránh overfitting
│
├─ 6. Model Optimization (Tối ưu mô hình)
│   │
│   ├─ 6.1 Overfitting vs Underfitting
│   │   ├─ bias vs variance
│   │   └─ diagnosis techniques
│   │
│   ├─ 6.2 Hyperparameter Tuning
│   │   ├─ Grid Search
│   │   ├─ Random Search
│   │   └─ Bayesian Optimization (advanced)
│   │
│   ├─ 6.3 Regularization
│   │   ├─ L1 (Lasso)
│   │   ├─ L2 (Ridge)
│   │   └─ Dropout concept (bridge to DL)
│   │
│   └─ 6.4 Goal
│       └─ Tối ưu accuracy + generalization
│
├─ 7. ML Pipeline (End-to-End System)
│   │
│   ├─ 7.1 Data Pipeline
│   │   ├─ data ingestion
│   │   ├─ preprocessing pipeline
│   │   └─ feature pipeline
│   │
│   ├─ 7.2 Model Pipeline
│   │   ├─ training pipeline
│   │   ├─ evaluation pipeline
│   │   └─ model saving (pickle / joblib)
│   │
│   ├─ 7.3 Deployment Basics
│   │   ├─ FastAPI / Flask
│   │   ├─ REST API model serving
│   │   └─ Docker (basic)
│   │
│   └─ 7.4 Goal
│       └─ Biến model thành sản phẩm thật
│
├─ 8. Mini Projects (BẮT BUỘC)
│   │
│   ├─ 8.1 Beginner Projects
│   │   ├─ House Price Prediction
│   │   ├─ Titanic Survival Prediction
│   │   └─ Customer Churn Prediction
│   │
│   ├─ 8.2 Intermediate Projects
│   │   ├─ Fraud Detection
│   │   ├─ Sales Forecasting
│   │   └─ Recommendation System
│   │
│   ├─ 8.3 Advanced Projects
│   │   ├─ End-to-End ML Pipeline
│   │   ├─ API deployed model
│   │   └─ Cloud ML deployment
│   │
│   └─ 8.4 Goal
│       └─ Portfolio ML Engineer ready
│
├─ 9. Key Industry Insights
│   ├─ 80% ML work = data preprocessing
│   ├─ Feature engineering > model choice
│   ├─ Simple model + good data > complex model
│   ├─ Evaluation is more important than training
│   └─ Deployment is what makes ML valuable
│
└─ 10. Checkpoint (JOB / CERT READY)
    ├─ ✔ Build regression + classification models
    ├─ ✔ Handle feature engineering properly
    ├─ ✔ Evaluate models correctly
    ├─ ✔ Build ML pipeline end-to-end
    ├─ ✔ Deploy simple API model
    └─ ✔ 2–3 ML projects on GitHub
```
---

# 🧠 4. Deep Learning Path

🎯 Mục tiêu: Làm AI (image, NLP)  

## Nội dung chính:
- Neural Network  
- CNN (Computer Vision)  
- RNN / Transformer (NLP)  
- Framework  

## Mindmap:

```
Deep Learning Path (From Features → Neural Networks → AI Systems)
│
├─ 0. Deep Learning Environment Setup (BẮT BUỘC)
│   │
│   ├─ 0.1 Core Tools
│   │   ├─ Python (>= 3.10)
│   │   ├─ Jupyter Notebook / JupyterLab
│   │   ├─ VS Code
│   │   └─ Git + GitHub
│   │
│   ├─ 0.2 Deep Learning Frameworks
│   │   ├─ TensorFlow (Google – TensorFlow Cert)
│   │   ├─ Keras (high-level API)
│   │   ├─ PyTorch (industry standard research)
│   │   └─ NumPy (tensor operations)
│   │
│   ├─ 0.3 Hardware (QUAN TRỌNG)
│   │   ├─ GPU (NVIDIA recommended)
│   │   ├─ CUDA + cuDNN (GPU acceleration)
│   │   └─ Google Colab (free GPU)
│   │
│   └─ 0.4 Goal
│       └─ Sẵn sàng train neural networks + GPU computing
│
├─ 1. Deep Learning Fundamentals
│   │
│   ├─ 1.1 Neural Network Basics
│   │   ├─ Perceptron
│   │   ├─ Neuron structure
│   │   ├─ Activation functions (ReLU, Sigmoid, Softmax)
│   │   └─ Forward propagation
│   │
│   ├─ 1.2 Training Process
│   │   ├─ Loss function (MSE, Cross-Entropy)
│   │   ├─ Backpropagation
│   │   ├─ Gradient descent
│   │   └─ Learning rate
│   │
│   ├─ 1.3 Optimization
│   │   ├─ SGD
│   │   ├─ Adam optimizer
│   │   └─ Momentum
│   │
│   └─ 1.4 Goal
│       └─ Hiểu cách neural network học từ dữ liệu
│
├─ 2. Deep Learning Framework (TensorFlow / Keras)
│   │
│   ├─ 2.1 TensorFlow Basics
│   │   ├─ Tensors
│   │   ├─ tf.data pipeline
│   │   ├─ model.fit()
│   │   └─ model.evaluate()
│   │
│   ├─ 2.2 Keras API
│   │   ├─ Sequential model
│   │   ├─ Functional API
│   │   ├─ Dense layers
│   │   └─ Dropout
│   │
│   ├─ 2.3 Model Training Flow
│   │   ├─ compile()
│   │   ├─ fit()
│   │   ├─ predict()
│   │   └─ save/load model
│   │
│   └─ 2.4 Goal
│       └─ Build neural networks bằng TensorFlow
│
├─ 3. Computer Vision (CNN – Convolutional Neural Networks)
│   │
│   ├─ 3.1 CNN Basics
│   │   ├─ Convolution layer
│   │   ├─ Pooling layer
│   │   ├─ Feature maps
│   │   └─ Flatten layer
│   │
│   ├─ 3.2 Advanced CNN
│   │   ├─ VGGNet
│   │   ├─ ResNet
│   │   ├─ EfficientNet
│   │   └─ Transfer Learning
│   │
│   ├─ 3.3 Image Tasks
│   │   ├─ Image classification
│   │   ├─ Object detection
│   │   └─ Image segmentation
│   │
│   └─ 3.4 Goal
│       └─ Build AI model xử lý hình ảnh
│
├─ 4. NLP (Natural Language Processing)
│   │
│   ├─ 4.1 RNN Models
│   │   ├─ RNN
│   │   ├─ LSTM
│   │   └─ GRU
│   │
│   ├─ 4.2 Transformer Architecture
│   │   ├─ Attention mechanism
│   │   ├─ Self-attention
│   │   ├─ Encoder / Decoder
│   │   └─ BERT / GPT concept
│   │
│   ├─ 4.3 Text Processing
│   │   ├─ Tokenization
│   │   ├─ Embedding (Word2Vec, GloVe)
│   │   └─ Text preprocessing
│   │
│   └─ 4.4 NLP Tasks
│       ├─ Sentiment analysis
│       ├─ Text classification
│       ├─ Machine translation
│       └─ Chatbot system
│
├─ 5. Model Optimization (Deep Learning tuning)
│   │
│   ├─ 5.1 Overfitting control
│   │   ├─ Dropout
│   │   ├─ Data augmentation
│   │   └─ Early stopping
│   │
│   ├─ 5.2 Hyperparameter tuning
│   │   ├─ batch size
│   │   ├─ learning rate
│   │   └─ epochs
│   │
│   ├─ 5.3 Regularization
│   │   ├─ L1 / L2
│   │   └─ weight decay
│   │
│   └─ 5.4 Goal
│       └─ Tăng accuracy + tránh overfitting
│
├─ 6. MLOps Basics (AI Deployment)
│   │
│   ├─ 6.1 Model Deployment
│   │   ├─ Flask / FastAPI
│   │   ├─ REST API serving
│   │   └─ model inference pipeline
│   │
│   ├─ 6.2 Model Saving
│   │   ├─ .h5 (TensorFlow)
│   │   ├─ SavedModel format
│   │   └─ model versioning
│   │
│   ├─ 6.3 Containerization
│   │   ├─ Docker basics
│   │   └─ containerized ML app
│   │
│   └─ 6.4 Goal
│       └─ Biến model thành AI product
│
├─ 7. Mini Projects (BẮT BUỘC)
│   │
│   ├─ 7.1 Beginner
│   │   ├─ Handwritten digit recognition (MNIST)
│   │   ├─ Image classification (cats vs dogs)
│   │   └─ Sentiment analysis
│   │
│   ├─ 7.2 Intermediate
│   │   ├─ Face recognition system
│   │   ├─ Text classifier chatbot
│   │   └─ Recommendation system DL
│   │
│   ├─ 7.3 Advanced
│   │   ├─ End-to-end AI system
│   │   ├─ CNN + API deployment
│   │   └─ NLP chatbot (Transformer-based)
│   │
│   └─ 7.4 Goal
│       └─ Portfolio AI Engineer ready
│
├─ 8. Industry Insights
│   ├─ Data quality quan trọng hơn model
│   ├─ Transfer learning > training from scratch
│   ├─ GPU required for real training
│   ├─ Most DL models are pre-trained
│   └─ Deployment = value of AI system
│
└─ 9. Checkpoint (CERT + JOB READY)
    ├─ ✔ Build CNN image classifier
    ├─ ✔ Build NLP text model
    ├─ ✔ Use TensorFlow/Keras fluently
    ├─ ✔ Apply transfer learning
    ├─ ✔ Deploy model via API
    └─ ✔ 2–3 AI projects on GitHub
```
---

# ☁️ 5. Data / ML Cloud Path

🎯 Mục tiêu: Deploy model & xử lý data trên cloud  

## Nội dung chính:
- Data pipeline  
- Model deployment  
- Big Data tools  
- MLOps  

---

## Mindmap:

```
Data / ML Cloud Path (From Local → Cloud → Production)
│
├─ 1. Data Pipeline (Luồng dữ liệu)
│   │
│   ├─ 1.1 Data Ingestion (Thu thập dữ liệu)
│   │   ├─ Batch processing (theo lô)
│   │   ├─ Streaming (real-time data)
│   │   ├─ API data ingestion
│   │   └─ Database extraction (SQL / NoSQL)
│   │
│   ├─ 1.2 Tools
│   │   ├─ Apache Kafka (streaming)
│   │   ├─ AWS Kinesis
│   │   ├─ Google Pub/Sub
│   │   └─ REST API / Web scraping
│   │
│   └─ 1.3 Goal
│       └─ Tự động hóa thu thập dữ liệu từ nhiều nguồn
│
├─ 2. ETL / ELT Pipeline (Data Engineering Core Concept)
│
│   ├─ 2.1 ETL (Extract → Transform → Load)
│   │
│   │   ├─ 🔹 2.1.1 Extract (Trích xuất dữ liệu)
│   │   │   ├─ Nguồn dữ liệu:
│   │   │   │   ├─ Relational DB (MySQL, PostgreSQL)
│   │   │   │   ├─ NoSQL (MongoDB, DynamoDB)
│   │   │   │   ├─ API (REST / GraphQL)
│   │   │   │   ├─ File (CSV, JSON, Parquet, Excel)
│   │   │   │   └─ Streaming logs (Kafka / Kinesis)
│   │   │   │
│   │   │   ├─ Phương thức:
│   │   │   │   ├─ Full extract
│   │   │   │   ├─ Incremental extract
│   │   │   │   └─ CDC (Change Data Capture)
│   │   │   │
│   │   │   └─ Exam keywords:
│   │   │       ├─ latency
│   │   │       ├─ throughput
│   │   │       └─ data freshness
│   │   │
│   │   ├─ 🔹 2.1.2 Transform (Biến đổi dữ liệu)
│   │   │   ├─ Data Cleaning:
│   │   │   │   ├─ Missing values
│   │   │   │   ├─ Duplicate removal
│   │   │   │   ├─ Outlier handling (IQR / Z-score)
│   │   │   │   └─ Data type correction
│   │   │   │
│   │   │   ├─ Data Transformation:
│   │   │   │   ├─ Normalization / Scaling
│   │   │   │   ├─ Encoding (One-hot / Label)
│   │   │   │   ├─ Aggregation (SUM / AVG / COUNT)
│   │   │   │   └─ Feature engineering
│   │   │   │
│   │   │   ├─ Business Transformation:
│   │   │   │   ├─ KPI calculation
│   │   │   │   ├─ Cohort analysis
│   │   │   │   └─ Time-based grouping
│   │   │   │
│   │   │   └─ Exam keywords:
│   │   │       ├─ data quality
│   │   │       ├─ schema transformation
│   │   │       └─ normalization vs denormalization
│   │   │
│   │   └─ 🔹 2.1.3 Load (Nạp dữ liệu)
│   │       ├─ Target systems:
│   │       │   ├─ Data Warehouse (BigQuery / Redshift / Synapse)
│   │       │   ├─ Data Lake (S3 / GCS / ADLS)
│   │       │   └─ OLAP systems
│   │       │
│   │       ├─ Load types:
│   │       │   ├─ Full load
│   │       │   ├─ Incremental load
│   │       │   └─ Upsert
│   │       │
│   │       └─ Exam keywords:
│   │           ├─ partitioning
│   │           ├─ indexing
│   │           └─ schema-on-write
│
│   ├─ 2.2 ELT (Extract → Load → Transform)
│   │
│   │   ├─ Khác ETL
│   │   │   ├─ ETL: transform trước load
│   │   │   ├─ ELT: load trước transform
│   │   │   └─ ELT = cloud-native approach
│   │   │
│   │   ├─ Khi dùng ELT
│   │   │   ├─ Big Data scale lớn
│   │   │   ├─ Cloud warehouse mạnh
│   │   │   ├─ cần giữ raw data
│   │   │   └─ analytics linh hoạt
│   │   │
│   │   ├─ Kiến trúc ELT
│   │   │   ├─ Raw → Data Lake
│   │   │   ├─ Load → Warehouse
│   │   │   ├─ Transform → SQL engine
│   │   │   └─ BI / ML consumption
│   │   │
│   │   └─ Exam keywords:
│   │       ├─ schema-on-read
│   │       ├─ scalability
│   │       └─ cost optimization
│
│   ├─ 2.3 Tools (CẤP THI CHỨNG CHỈ)
│   │
│   │   ├─ Orchestration
│   │   │   ├─ Apache Airflow (DAG)
│   │   │   ├─ AWS Step Functions
│   │   │   ├─ Azure Data Factory
│   │   │   └─ GCP Cloud Composer
│   │   │
│   │   ├─ Processing
│   │   │   ├─ Apache Spark
│   │   │   ├─ AWS Glue
│   │   │   └─ dbt
│   │   │
│   │   └─ Storage integration
│   │       ├─ BigQuery SQL
│   │       ├─ S3 + Athena
│   │       └─ Synapse
│
│   ├─ 2.4 Advanced Concepts (EXAM CRITICAL)
│   │
│   │   ├─ Data Quality
│   │   ├─ Data Governance
│   │   │   ├─ lineage
│   │   │   └─ metadata
│   │   ├─ Performance optimization
│   │   │   ├─ partitioning
│   │   │   └─ indexing
│   │   └─ Reliability
│   │       ├─ retry
│   │       └─ fault tolerance
│
│   └─ 2.5 Goal
│       ├─ Build end-to-end pipeline
│       ├─ Understand ETL vs ELT
│       ├─ Use Airflow DAG
│       ├─ SQL + Spark + dbt workflow
│       └─ Ready for AWS / GCP / Azure exams
│
├─ 3. Data Storage (Lưu trữ dữ liệu - Data Engineering Core)
│
│   ├─ 3.1 Data Warehouse (Structured Data - OLAP System)
│   │
│   │   ├─ 🔹 3.1.1 Khái niệm
│   │   │   ├─ Lưu dữ liệu đã xử lý (clean + structured)
│   │   │   ├─ Dùng cho BI / Analytics / Reporting
│   │   │   ├─ Schema-on-write (thiết kế schema trước khi load)
│   │   │   └─ Dữ liệu dạng bảng (rows / columns)
│   │   │
│   │   ├─ 🔹 3.1.2 Đặc điểm
│   │   │   ├─ OLAP (Online Analytical Processing)
│   │   │   ├─ Query phức tạp (JOIN / GROUP BY)
│   │   │   ├─ Read-heavy (ưu tiên đọc)
│   │   │   └─ Tối ưu dashboard & reporting
│   │   │
│   │   ├─ 🔹 3.1.3 Cloud Data Warehouse
│   │   │   ├─ BigQuery (GCP)
│   │   │   │   ├─ Serverless
│   │   │   │   ├─ Auto-scale
│   │   │   │   └─ SQL-based analytics
│   │   │   │
│   │   │   ├─ Amazon Redshift (AWS)
│   │   │   │   ├─ Columnar storage
│   │   │   │   ├─ Cluster-based
│   │   │   │   └─ Tuning performance
│   │   │   │
│   │   │   └─ Azure Synapse Analytics
│   │   │       ├─ Unified analytics
│   │   │       ├─ SQL + Spark integration
│   │   │       └─ Pipeline support
│   │   │
│   │   ├─ 🔹 3.1.4 Data Modeling
│   │   │   ├─ Fact table (revenue, sales)
│   │   │   ├─ Dimension table (user, product)
│   │   │   ├─ Star schema
│   │   │   └─ Snowflake schema
│   │   │
│   │   ├─ 🔹 3.1.5 Exam keywords
│   │   │   ├─ OLAP vs OLTP
│   │   │   ├─ columnar vs row storage
│   │   │   ├─ partitioning
│   │   │   └─ query optimization
│   │   │
│   │   └─ 🔹 3.1.6 Use cases
│   │       ├─ BI dashboard
│   │       ├─ KPI reporting
│   │       ├─ Sales analytics
│   │       └─ Customer analysis
│   │
│   ├─ 3.2 Data Lake (Raw Data Storage System)
│   │
│   │   ├─ 🔹 3.2.1 Khái niệm
│   │   │   ├─ Lưu raw data (structured + unstructured)
│   │   │   ├─ Schema-on-read
│   │   │   ├─ Không cần xử lý trước khi lưu
│   │   │   └─ Phục vụ ML / Data Science
│   │   │
│   │   ├─ 🔹 3.2.2 Đặc điểm
│   │   │   ├─ Storage rẻ
│   │   │   ├─ Scale lớn (TB → PB)
│   │   │   ├─ Linh hoạt dữ liệu
│   │   │   └─ Phù hợp AI / ML training
│   │   │
│   │   ├─ 🔹 3.2.3 Cloud Data Lake
│   │   │   ├─ AWS S3
│   │   │   │   ├─ Object storage
│   │   │   │   ├─ Durable
│   │   │   │   └─ Integrate Athena / Glue
│   │   │   │
│   │   │   ├─ Google Cloud Storage (GCS)
│   │   │   │   ├─ Multi-tier storage
│   │   │   │   └─ BigQuery integration
│   │   │   │
│   │   │   └─ Azure Data Lake Storage (ADLS)
│   │   │       ├─ Hierarchical namespace
│   │   │       ├─ Spark integration
│   │   │       └─ Analytics optimized
│   │   │
│   │   ├─ 🔹 3.2.4 Data Lake Zones
│   │   │   ├─ Raw zone
│   │   │   ├─ Cleaned zone
│   │   │   ├─ Curated zone
│   │   │   └─ Feature zone (ML)
│   │   │
│   │   ├─ 🔹 3.2.5 Exam keywords
│   │   │   ├─ schema-on-read
│   │   │   ├─ object storage
│   │   │   ├─ data lifecycle
│   │   │   └─ partitioning
│   │   │
│   │   └─ 🔹 3.2.6 Use cases
│   │       ├─ ML training data
│   │       ├─ Log analysis
│   │       ├─ IoT data
│   │       └─ Data archival
│   │
│   ├─ 3.3 Data Warehouse vs Data Lake (EXAM CRITICAL)
│   │   ├─ Structure
│   │   │   ├─ Warehouse: structured
│   │   │   └─ Lake: all data types
│   │   │
│   │   ├─ Schema
│   │   │   ├─ Warehouse: schema-on-write
│   │   │   └─ Lake: schema-on-read
│   │   │
│   │   ├─ Users
│   │   │   ├─ Warehouse: BI analysts
│   │   │   └─ Lake: Data scientists
│   │   │
│   │   ├─ Cost
│   │   │   ├─ Warehouse: compute expensive
│   │   │   └─ Lake: storage cheap
│   │   │
│   │   └─ Exam keywords
│   │       ├─ structured vs unstructured
│   │       ├─ analytics vs ML
│   │       └─ governance
│   │
│   └─ 3.4 Goal (QUAN TRỌNG NHẤT)
│       ├─ Hiểu kiến trúc storage hiện đại
│       ├─ Phân biệt Warehouse vs Lake
│       ├─ Chọn đúng system theo use-case
│       ├─ Hiểu AWS / GCP / Azure storage services
│       └─ Sẵn sàng exam scenario questions
│
├─ 4. Model Deployment (Triển khai ML Model)
│   │
│   ├─ 4.1 Deployment Types (Các kiểu triển khai model)
│   │   │
│   │   ├─ 🔹 4.1.1 REST API Deployment
│   │   │   ├─ Framework:
│   │   │   │   ├─ Flask (lightweight)
│   │   │   │   └─ FastAPI (modern, high performance)
│   │   │   │
│   │   │   ├─ Workflow:
│   │   │   │   ├─ Load trained model (.pkl / .h5)
│   │   │   │   ├─ Create API endpoint (/predict)
│   │   │   │   ├─ Receive input (JSON request)
│   │   │   │   ├─ Preprocess input
│   │   │   │   ├─ Model inference
│   │   │   │   └─ Return prediction (JSON response)
│   │   │   │
│   │   │   ├─ Use cases:
│   │   │   │   ├─ Web apps
│   │   │   │   ├─ Mobile apps
│   │   │   │   └─ Real-time prediction systems
│   │   │   │
│   │   │   └─ Exam keywords:
│   │   │       ├─ latency (độ trễ thấp)
│   │   │       ├─ synchronous request
│   │   │       └─ stateless service
│   │   │
│   │   ├─ 🔹 4.1.2 Batch Prediction
│   │   │   ├─ Đặc điểm:
│   │   │   │   ├─ Không real-time
│   │   │   │   ├─ Xử lý theo lô (batch)
│   │   │   │   └─ Output lưu vào database / file
│   │   │   │
│   │   │   ├─ Workflow:
│   │   │   │   ├─ Load dataset lớn
│   │   │   │   ├─ Run inference hàng loạt
│   │   │   │   ├─ Save results (CSV / DB / Data Warehouse)
│   │   │   │   └─ Schedule job (Airflow / cron)
│   │   │   │
│   │   │   ├─ Use cases:
│   │   │   │   ├─ Churn prediction hàng ngày
│   │   │   │   ├─ Recommendation system offline
│   │   │   │   └─ Financial reporting
│   │   │   │
│   │   │   └─ Exam keywords:
│   │   │       ├─ throughput (cao)
│   │   │       └─ cost-efficient
│   │   │
│   │   └─ 🔹 4.1.3 Real-time Prediction
│   │       ├─ Đặc điểm:
│   │       │   ├─ Response ngay lập tức (ms–seconds)
│   │       │   ├─ API-based serving
│   │       │   └─ Always-on system
│   │       │
│   │       ├─ Architecture:
│   │       │   ├─ Client → API Gateway → Model Service → Response
│   │       │
│   │       ├─ Use cases:
│   │       │   ├─ Fraud detection (ngân hàng)
│   │       │   ├─ Recommendation (TikTok, YouTube)
│   │       │   └─ Ad targeting
│   │       │
│   │       └─ Exam keywords:
│   │           ├─ low latency requirement
│   │           └─ scalability
│   │
│   ├─ 4.2 Tools (Công cụ triển khai)
│   │   │
│   │   ├─ 🔹 4.2.1 API Frameworks
│   │   │   ├─ Flask
│   │   │   │   ├─ simple routing
│   │   │   │   └─ good for prototypes
│   │   │   │
│   │   │   └─ FastAPI
│   │   │       ├─ async support
│   │   │       ├─ auto Swagger docs
│   │   │       └─ high performance
│   │   │
│   │   ├─ 🔹 4.2.2 Containerization
│   │   │   ├─ Docker
│   │   │   │   ├─ containerize model + API
│   │   │   │   ├─ reproducible environment
│   │   │   │   └─ isolate dependencies
│   │   │   │
│   │   │   └─ Docker concepts:
│   │   │       ├─ Dockerfile
│   │   │       ├─ Image
│   │   │       └─ Container
│   │   │
│   │   ├─ 🔹 4.2.3 Orchestration
│   │   │   ├─ Kubernetes
│   │   │   │   ├─ auto-scaling
│   │   │   │   ├─ load balancing
│   │   │   │   └─ fault tolerance
│   │   │   │
│   │   │   └─ Cloud alternatives:
│   │   │       ├─ AWS EKS
│   │   │       ├─ Azure AKS
│   │   │       └─ GCP GKE
│   │   │
│   │   └─ 🔹 4.2.4 ML Lifecycle Tools
│   │       ├─ MLflow
│   │       │   ├─ experiment tracking
│   │       │   ├─ model registry
│   │       │   └─ versioning
│   │       │
│   │       └─ Experiment tracking tools:
│   │           ├─ Weights & Biases
│   │           └─ Neptune.ai
│   │
│   └─ 4.3 Goal (Mục tiêu cuối)
│       │
│       ├─ Deploy ML model thành service thực tế
│       ├─ Biết chọn đúng kiểu deployment:
│       │   ├─ API (real-time)
│       │   ├─ Batch (offline)
│       │   └─ Streaming (advanced)
│       │
│       ├─ Containerize model bằng Docker
│       ├─ Hiểu CI/CD cơ bản cho ML
│       └─ Sẵn sàng production system (cloud-ready)
│
├─ 5. Big Data Processing (Xử lý dữ liệu lớn)
│   │
│   ├─ 5.1 Distributed Computing (Điện toán phân tán)
│   │   │
│   │   ├─ 🔹 5.1.1 Khái niệm cốt lõi
│   │   │   ├─ Xử lý dữ liệu trên nhiều máy (cluster)
│   │   │   ├─ Chia nhỏ dữ liệu (data partitioning)
│   │   │   ├─ Parallel processing (xử lý song song)
│   │   │   └─ Fault tolerance (chịu lỗi khi node chết)
│   │   │
│   │   ├─ 🔹 5.1.2 Kiến trúc hệ thống
│   │   │   ├─ Master node (điều phối)
│   │   │   ├─ Worker nodes (xử lý dữ liệu)
│   │   │   ├─ Cluster manager (YARN / Kubernetes)
│   │   │   └─ Distributed storage layer
│   │   │
│   │   ├─ 🔹 5.1.3 Vấn đề cần giải quyết
│   │   │   ├─ Data too large (không fit 1 máy)
│   │   │   ├─ Processing time quá lâu
│   │   │   ├─ Fault tolerance khi node fail
│   │   │   └─ Scalability (mở rộng hệ thống)
│   │   │
│   │   └─ 🔹 5.1.4 Exam keywords
│   │       ├─ horizontal scaling
│   │       ├─ distributed system
│   │       ├─ cluster computing
│   │       └─ parallel execution
│   │
│   ├─ 5.2 Tools (Công cụ Big Data)
│   │   │
│   │   ├─ 🔹 5.2.1 Apache Spark (QUAN TRỌNG NHẤT)
│   │   │   │
│   │   │   ├─ Core concept:
│   │   │   │   ├─ In-memory computing (nhanh hơn Hadoop)
│   │   │   │   ├─ Distributed data processing
│   │   │   │   └─ Lazy evaluation
│   │   │   │
│   │   │   ├─ Spark Components:
│   │   │   │   ├─ Spark Core (engine)
│   │   │   │   ├─ Spark SQL (query dữ liệu như SQL)
│   │   │   │   ├─ Spark Streaming (real-time data)
│   │   │   │   └─ MLlib (Machine Learning library)
│   │   │   │
│   │   │   ├─ Data Abstraction:
│   │   │   │   ├─ RDD (Resilient Distributed Dataset)
│   │   │   │   ├─ DataFrame (structured data)
│   │   │   │   └─ Dataset (typed API)
│   │   │   │
│   │   │   ├─ Use cases:
│   │   │   │   ├─ Big data processing
│   │   │   │   ├─ ETL pipelines
│   │   │   │   ├─ ML at scale
│   │   │   │   └─ Streaming analytics
│   │   │   │
│   │   │   └─ Exam keywords:
│   │   │       ├─ in-memory processing
│   │   │       ├─ DAG execution
│   │   │       └─ lazy evaluation
│   │   │
│   │   └─ 🔹 5.2.2 Hadoop Ecosystem (FOUNDATION SYSTEM)
│   │       │
│   │       ├─ HDFS (Hadoop Distributed File System)
│   │       │   ├─ lưu trữ dữ liệu phân tán
│   │       │   ├─ replication (sao chép dữ liệu)
│   │       │   └─ fault tolerance
│   │       │
│   │       ├─ MapReduce (processing model)
│   │       │   ├─ Map step: xử lý dữ liệu song song
│   │       │   ├─ Shuffle step: gom dữ liệu
│   │       │   └─ Reduce step: tổng hợp kết quả
│   │       │
│   │       ├─ YARN (resource management)
│   │       │   ├─ job scheduling
│   │       │   └─ resource allocation
│   │       │
│   │       └─ Limitation:
│   │           ├─ chậm hơn Spark
│   │           ├─ disk-based processing
│   │           └─ complex setup
│   │
│   ├─ 5.3 Advanced Big Data Concepts (RẤT QUAN TRỌNG CHO CERT)
│   │   │
│   │   ├─ 🔹 Data Partitioning
│   │   │   ├─ chia dữ liệu theo key
│   │   │   ├─ tăng performance query
│   │   │   └─ giảm cost processing
│   │   │
│   │   ├─ 🔹 Data Shuffling
│   │   │   ├─ di chuyển data giữa nodes
│   │   │   └─ expensive operation (tốn tài nguyên)
│   │   │
│   │   ├─ 🔹 Fault Tolerance
│   │   │   ├─ recompute khi node fail
│   │   │   └─ replication strategy
│   │   │
│   │   ├─ 🔹 Scalability
│   │   │   ├─ horizontal scaling (thêm node)
│   │   │   └─ elastic compute (cloud)
│   │   │
│   │   └─ 🔹 Performance Optimization
│   │       ├─ caching data
│   │       ├─ reducing shuffle
│   │       └─ efficient joins
│   │
│   └─ 5.4 Goal (MỤC TIÊU QUAN TRỌNG NHẤT)
│       │
│       ├─ Xử lý dữ liệu TB–PB scale
│       ├─ Hiểu Spark architecture & execution model
│       ├─ Biết phân biệt Spark vs Hadoop
│       ├─ Thiết kế pipeline data lớn
│       ├─ Tối ưu performance distributed system
│       └─ Sẵn sàng cho AWS / GCP / Azure Big Data questions
│
├─ 6. MLOps (Machine Learning Operations)
│   │
│   ├─ 6.1 ML Lifecycle (Vòng đời Machine Learning)
│   │   │
│   │   ├─ 🔹 6.1.1 Full Pipeline Overview
│   │   │   ├─ Data Collection (thu thập dữ liệu)
│   │   │   ├─ Data Processing (clean + transform)
│   │   │   ├─ Feature Engineering
│   │   │   ├─ Model Training
│   │   │   ├─ Model Evaluation
│   │   │   ├─ Model Deployment
│   │   │   ├─ Monitoring
│   │   │   └─ Retraining loop (continuous learning)
│   │   │
│   │   ├─ 🔹 6.1.2 MLOps vs ML truyền thống
│   │   │   ├─ ML truyền thống: chỉ train model
│   │   │   ├─ MLOps: production system end-to-end
│   │   │   └─ automation + monitoring + scaling
│   │   │
│   │   ├─ 🔹 6.1.3 Production Requirements
│   │   │   ├─ scalability (mở rộng hệ thống)
│   │   │   ├─ reproducibility (tái lập kết quả)
│   │   │   ├─ versioning (data + model)
│   │   │   └─ reliability (ổn định hệ thống)
│   │   │
│   │   └─ 🔹 6.1.4 Exam keywords
│   │       ├─ feedback loop
│   │       ├─ continuous training
│   │       └─ automation pipeline
│   │
│   ├─ 6.2 CI/CD for ML (DevOps cho Machine Learning)
│   │   │
│   │   ├─ 🔹 6.2.1 CI (Continuous Integration)
│   │   │   ├─ code test tự động
│   │   │   ├─ validate data pipeline
│   │   │   ├─ model training test
│   │   │   └─ linting + unit tests
│   │   │
│   │   ├─ 🔹 6.2.2 CD (Continuous Deployment)
│   │   │   ├─ deploy model lên cloud
│   │   │   ├─ update API service
│   │   │   ├─ rollback khi lỗi
│   │   │   └─ blue-green deployment
│   │   │
│   │   ├─ 🔹 6.2.3 Tools
│   │   │   ├─ GitHub Actions
│   │   │   │   ├─ workflow automation
│   │   │   │   └─ trigger on push / PR
│   │   │   │
│   │   │   ├─ Jenkins
│   │   │   │   ├─ pipeline orchestration
│   │   │   │   └─ enterprise CI/CD
│   │   │   │
│   │   │   └─ Azure DevOps
│   │   │       ├─ pipelines
│   │   │       └─ integration với Azure ML
│   │   │
│   │   └─ 🔹 6.2.4 Exam keywords
│   │       ├─ automation
│   │       ├─ pipeline orchestration
│   │       └─ continuous delivery
│   │
│   ├─ 6.3 Model Monitoring (Giám sát mô hình)
│   │   │
│   │   ├─ 🔹 6.3.1 Data Drift Detection
│   │   │   ├─ dữ liệu input thay đổi theo thời gian
│   │   │   ├─ distribution shift
│   │   │   └─ ảnh hưởng accuracy model
│   │   │
│   │   ├─ 🔹 6.3.2 Concept Drift
│   │   │   ├─ mối quan hệ X → Y thay đổi
│   │   │   ├─ model trở nên outdated
│   │   │   └─ cần retrain
│   │   │
│   │   ├─ 🔹 6.3.3 Performance Monitoring
│   │   │   ├─ accuracy / precision / recall
│   │   │   ├─ latency API
│   │   │   ├─ throughput system
│   │   │   └─ error rate
│   │   │
│   │   ├─ 🔹 6.3.4 Monitoring Strategy
│   │   │   ├─ logging predictions
│   │   │   ├─ alert system
│   │   │   ├─ dashboards
│   │   │   └─ anomaly detection
│   │   │
│   │   └─ 🔹 6.3.5 Exam keywords
│   │       ├─ model degradation
│   │       ├─ drift detection
│   │       └─ observability
│   │
│   ├─ 6.4 Tools (Công cụ MLOps)
│   │   │
│   │   ├─ 🔹 6.4.1 MLflow (QUAN TRỌNG NHẤT)
│   │   │   ├─ experiment tracking
│   │   │   ├─ model registry
│   │   │   ├─ model versioning
│   │   │   └─ reproducibility
│   │   │
│   │   ├─ 🔹 6.4.2 Weights & Biases (W&B)
│   │   │   ├─ experiment visualization
│   │   │   ├─ hyperparameter tracking
│   │   │   └─ collaboration team ML
│   │   │
│   │   ├─ 🔹 6.4.3 Monitoring Tools
│   │   │   ├─ Prometheus
│   │   │   │   ├─ metrics collection
│   │   │   │   └─ time-series monitoring
│   │   │   │
│   │   │   └─ Grafana
│   │   │       ├─ dashboards
│   │   │       ├─ visualization metrics
│   │   │       └─ alert system
│   │   │
│   │   └─ 🔹 6.4.4 Cloud MLOps Tools
│   │       ├─ AWS SageMaker Pipelines
│   │       ├─ Azure ML Pipelines
│   │       └─ Vertex AI Pipelines (GCP)
│   │
│   └─ 6.5 Goal (MỤC TIÊU QUAN TRỌNG NHẤT)
│       │
│       ├─ Build ML system end-to-end (production-ready)
│       ├─ Automate training + deployment pipeline
│       ├─ Monitor model performance real-time
│       ├─ Detect drift + retrain automatically
│       ├─ Version control data + model + code
│       └─ Sẵn sàng MLOps questions trong AWS / GCP / Azure exam
│
├─ 7. Cloud Platforms (Multi-Cloud Mapping)
│   │
│   ├─ 7.1 AWS vs Azure vs GCP (So sánh hệ sinh thái Cloud)
│   │   │
│   │   ├─ 🔹 7.1.1 Storage (Lưu trữ dữ liệu)
│   │   │   │
│   │   │   ├─ AWS S3 (Simple Storage Service)
│   │   │   │   ├─ Object storage (file-based)
│   │   │   │   ├─ scalability: gần như unlimited
│   │   │   │   ├─ use case:
│   │   │   │   │   ├─ Data lake
│   │   │   │   │   ├─ Backup / archive
│   │   │   │   │   └─ ML dataset storage
│   │   │   │   └─ exam keywords:
│   │   │   │       ├─ durability (11 9s)
│   │   │   │       └─ object storage vs block storage
│   │   │   │
│   │   │   ├─ Azure Blob Storage
│   │   │   │   ├─ Object storage tương tự S3
│   │   │   │   ├─ integration Azure ecosystem
│   │   │   │   ├─ tiers:
│   │   │   │   │   ├─ hot / cool / archive
│   │   │   │   │   └─ cost optimization
│   │   │   │   └─ use case:
│   │   │   │       ├─ enterprise data lake
│   │   │   │       └─ analytics storage
│   │   │   │
│   │   │   └─ Google Cloud Storage (GCS)
│   │   │       ├─ object storage
│   │   │       ├─ strong integration BigQuery
│   │   │       ├─ multi-region storage
│   │   │       └─ use case:
│   │   │           ├─ ML datasets
│   │   │           └─ analytics pipelines
│   │   │
│   │   ├─ 🔹 7.1.2 Data Warehouse (Kho dữ liệu phân tích)
│   │   │   │
│   │   │   ├─ AWS Redshift
│   │   │   │   ├─ columnar database
│   │   │   │   ├─ optimized for OLAP
│   │   │   │   ├─ SQL-based analytics
│   │   │   │   └─ integration: S3 + Glue
│   │   │   │
│   │   │   ├─ Azure Synapse Analytics
│   │   │   │   ├─ combined: Data warehouse + Big Data
│   │   │   │   ├─ SQL + Spark integration
│   │   │   │   └─ enterprise analytics platform
│   │   │   │
│   │   │   └─ Google BigQuery
│   │   │       ├─ serverless data warehouse
│   │   │       ├─ no infrastructure management
│   │   │       ├─ extremely fast SQL queries
│   │   │       └─ pay-per-query model
│   │   │
│   │   ├─ 🔹 7.1.3 ML Platforms (Machine Learning as a Service)
│   │   │   │
│   │   │   ├─ AWS SageMaker
│   │   │   │   ├─ full ML lifecycle platform
│   │   │   │   ├─ training + deployment + monitoring
│   │   │   │   ├─ built-in algorithms
│   │   │   │   └─ exam keywords:
│   │   │   │       ├─ managed ML service
│   │   │   │       └─ end-to-end ML pipeline
│   │   │   │
│   │   │   ├─ Azure Machine Learning
│   │   │   │   ├─ drag-and-drop + code-based ML
│   │   │   │   ├─ AutoML support
│   │   │   │   ├─ model registry
│   │   │   │   └─ integration with Azure DevOps
│   │   │   │
│   │   │   └─ Google Vertex AI
│   │   │       ├─ unified ML platform
│   │   │       ├─ training + deployment + pipelines
│   │   │       ├─ AutoML + custom training
│   │   │       └─ strong integration BigQuery + GCS
│   │   │
│   │   ├─ 🔹 7.1.4 Streaming (Real-time data processing)
│   │   │   │
│   │   │   ├─ AWS Kinesis
│   │   │   │   ├─ real-time data ingestion
│   │   │   │   ├─ streaming analytics
│   │   │   │   └─ use case:
│   │   │   │       ├─ logs processing
│   │   │   │       └─ real-time dashboards
│   │   │   │
│   │   │   ├─ Azure Event Hub
│   │   │   │   ├─ big data streaming
│   │   │   │   ├─ telemetry ingestion
│   │   │   │   └─ integration IoT + analytics
│   │   │   │
│   │   │   └─ Google Pub/Sub
│   │   │       ├─ messaging + streaming system
│   │   │       ├─ decoupled architecture
│   │   │       └─ event-driven systems
│   │   │
│   │   └─ 🔹 7.1.5 Exam keywords (rất quan trọng)
│   │       ├─ serverless vs managed service
│   │       ├─ scalability vs elasticity
│   │       ├─ OLTP vs OLAP
│   │       └─ batch vs streaming processing
│   │
│   └─ 7.2 Goal (Mục tiêu quan trọng)
│       │
│       ├─ Hiểu hệ sinh thái cloud 3 ông lớn:
│       │   ├─ AWS (market leader)
│       │   ├─ Azure (enterprise mạnh)
│       │   └─ GCP (data + ML mạnh nhất)
│       │
│       ├─ Biết mapping service cross-cloud
│       ├─ Hiểu khi nào dùng service nào
│       ├─ Thiết kế architecture Data / ML trên cloud
│       └─ Sẵn sàng case study trong AWS / GCP / Azure exam
│
├─ 8. End-to-End Architecture (Hệ thống ML hoàn chỉnh)
│   │
│   ├─ 🔹 8.1 Data Source (Nguồn dữ liệu)
│   │   │
│   │   ├─ Internal data sources
│   │   │   ├─ Database (MySQL / PostgreSQL)
│   │   │   ├─ Application logs
│   │   │   └─ User behavior data
│   │   │
│   │   ├─ External data sources
│   │   │   ├─ Public APIs
│   │   │   ├─ Third-party datasets
│   │   │   └─ Web scraping
│   │   │
│   │   └─ Streaming sources
│   │       ├─ IoT devices
│   │       ├─ clickstream data
│   │       └─ real-time events
│   │
│   ├─ 🔹 8.2 Data Ingestion (Thu thập dữ liệu)
│   │   │
│   │   ├─ Batch ingestion
│   │   │   ├─ scheduled ETL jobs
│   │   │   ├─ daily/hourly sync
│   │   │   └─ bulk data transfer
│   │   │
│   │   ├─ Streaming ingestion
│   │   │   ├─ Kafka
│   │   │   ├─ Kinesis / PubSub / Event Hub
│   │   │   └─ real-time pipelines
│   │   │
│   │   └─ API ingestion
│   │       ├─ REST API pulling
│   │       ├─ webhook events
│   │       └─ third-party integrations
│   │
│   ├─ 🔹 8.3 Data Storage Layer (Lưu trữ)
│   │   │
│   │   ├─ Data Lake (Raw storage)
│   │   │   ├─ S3 (AWS)
│   │   │   ├─ GCS (GCP)
│   │   │   └─ Azure Data Lake
│   │   │
│   │   ├─ Data Warehouse (Processed data)
│   │   │   ├─ BigQuery
│   │   │   ├─ Redshift
│   │   │   └─ Synapse
│   │   │
│   │   └─ Feature Store (ML-specific storage)
│   │       ├─ online features (real-time)
│   │       └─ offline features (batch training)
│   │
│   ├─ 🔹 8.4 Data Processing (Xử lý dữ liệu)
│   │   │
│   │   ├─ ETL / ELT pipelines
│   │   │   ├─ data cleaning
│   │   │   ├─ transformation
│   │   │   └─ aggregation
│   │   │
│   │   ├─ Distributed processing
│   │   │   ├─ Apache Spark
│   │   │   ├─ Databricks
│   │   │   └─ Hadoop ecosystem
│   │   │
│   │   └─ Output datasets
│   │       ├─ training dataset
│   │       ├─ validation dataset
│   │       └─ inference dataset
│   │
│   ├─ 🔹 8.5 Feature Engineering (Tạo đặc trưng)
│   │   │
│   │   ├─ Feature types
│   │   │   ├─ numerical features
│   │   │   ├─ categorical features
│   │   │   ├─ time-series features
│   │   │   └─ text embeddings
│   │   │
│   │   ├─ Feature operations
│   │   │   ├─ scaling / normalization
│   │   │   ├─ encoding
│   │   │   ├─ aggregation features
│   │   │   └─ feature selection
│   │   │
│   │   └─ Feature store usage
│   │       ├─ reuse features across models
│   │       └─ consistency training vs serving
│   │
│   ├─ 🔹 8.6 Model Training (Huấn luyện model)
│   │   │
│   │   ├─ Training environment
│   │   │   ├─ local machine
│   │   │   ├─ cloud VM
│   │   │   └─ distributed training (Spark / GPU cluster)
│   │   │
│   │   ├─ Training process
│   │   │   ├─ model selection
│   │   │   ├─ hyperparameter tuning
│   │   │   ├─ cross-validation
│   │   │   └─ evaluation metrics
│   │   │
│   │   └─ Output
│   │       ├─ trained model artifact
│   │       └─ training logs
│   │
│   ├─ 🔹 8.7 Model Registry (Quản lý model)
│   │   │
│   │   ├─ Versioning
│   │   │   ├─ model v1 / v2 / v3
│   │   │   └─ rollback support
│   │   │
│   │   ├─ Metadata tracking
│   │   │   ├─ accuracy
│   │   │   ├─ training data version
│   │   │   └─ hyperparameters
│   │   │
│   │   └─ Tools
│   │       ├─ MLflow Model Registry
│   │       ├─ SageMaker Model Registry
│   │       └─ Vertex AI Model Registry
│   │
│   ├─ 🔹 8.8 Deployment (Triển khai model)
│   │   │
│   │   ├─ Deployment types
│   │   │   ├─ REST API (FastAPI / Flask)
│   │   │   ├─ Batch inference
│   │   │   └─ Streaming inference
│   │   │
│   │   ├─ Infrastructure
│   │   │   ├─ Docker container
│   │   │   ├─ Kubernetes cluster
│   │   │   └─ Serverless (Lambda / Cloud Functions)
│   │   │
│   │   └─ Scaling
│   │       ├─ auto-scaling
│   │       ├─ load balancing
│   │       └─ multi-region deployment
│   │
│   ├─ 🔹 8.9 Monitoring (Giám sát hệ thống)
│   │   │
│   │   ├─ Model monitoring
│   │   │   ├─ accuracy drop detection
│   │   │   ├─ data drift
│   │   │   └─ concept drift
│   │   │
│   │   ├─ System monitoring
│   │   │   ├─ latency
│   │   │   ├─ throughput
│   │   │   └─ error rate
│   │   │
│   │   └─ Tools
│   │       ├─ Prometheus
│   │       ├─ Grafana
│   │       └─ CloudWatch / Azure Monitor
│   │
│   ├─ 🔹 8.10 Retraining Loop (Vòng lặp học lại)
│   │   │
│   │   ├─ Trigger conditions
│   │   │   ├─ data drift detected
│   │   │   ├─ performance drop
│   │   │   └─ scheduled retraining
│   │   │
│   │   ├─ Retraining pipeline
│   │   │   ├─ new data ingestion
│   │   │   ├─ retrain model
│   │   │   ├─ evaluate new model
│   │   │   └─ deploy if better
│   │   │
│   │   └─ Automation
│   │       ├─ CI/CD trigger
│   │       ├─ Airflow pipeline
│   │       └─ ML pipeline orchestration
│   │
│   └─ 🔹 8.11 Goal (Mục tiêu tổng thể)
│       │
│       ├─ Build hệ thống ML production-ready end-to-end
│       ├─ Hiểu toàn bộ data → model → deployment flow
│       ├─ Có khả năng thiết kế system giống Big Tech
│       ├─ Deploy + scale + monitor model thực tế
│       └─ Sẵn sàng interview + AWS/GCP/Azure exam scenarios
│
├─ 9. Key Insights
│   ├─ Cloud = scale hệ thống
│   ├─ ML production ≠ ML học thuật
│   ├─ Automation là bắt buộc
│   ├─ Data luôn thay đổi → phải retrain
│   └─ System design quan trọng hơn model
│
└─ 10. Checkpoint
    ├─ ✔ Hiểu ETL / ELT pipeline
    ├─ ✔ Biết Data Warehouse vs Data Lake
    ├─ ✔ Deploy model bằng API
    ├─ ✔ Hiểu Docker / Kubernetes cơ bản
    ├─ ✔ Biết Spark / Big Data concept
    ├─ ✔ Hiểu MLOps lifecycle
    └─ ✔ Làm được 1 project deploy hoàn chỉnh

```

## 🧠 5.1. Multi-Cloud Mapping (AWS vs Azure vs GCP)

| Concept            | AWS                              | Azure                              | Google Cloud                     | Ý nghĩa thi chứng chỉ |
|--------------------|----------------------------------|------------------------------------|----------------------------------|------------------------|
| Data Warehouse     | Redshift                         | Synapse Analytics                  | BigQuery                        | Query data SQL scale lớn |
| Data Lake          | S3                               | Data Lake Storage Gen2             | Cloud Storage                   | Lưu raw data (unstructured) |
| Batch Processing   | AWS Glue                         | Data Factory                      | Dataflow (Batch mode)           | ETL theo lô |
| Stream Processing  | Kinesis                          | Event Hub + Stream Analytics      | Pub/Sub + Dataflow Streaming    | Real-time data |
| Big Data Engine    | EMR (Spark/Hadoop)              | Azure Databricks                  | Dataproc                        | Xử lý distributed |
| ML Platform        | SageMaker                       | Azure ML Studio                   | Vertex AI                      | Train + deploy model |
| Orchestration      | Step Functions                  | Logic Apps                       | Cloud Composer (Airflow)       | DAG pipeline |
| Monitoring         | CloudWatch                      | Azure Monitor                    | Cloud Monitoring              | Tracking system |
| IAM / Security     | IAM Roles                       | Azure RBAC                      | IAM                            | Security & access control |
| Streaming Queue    | SQS / Kinesis                   | Event Hub                      | Pub/Sub                       | Event-driven systems |

---

## 🧠 5.2. Data Pipeline Flow (From Data → Insight → ML → Production)

```text

Data Sources
   │
   ├─ Internal (DB, CRM, ERP)
   ├─ External (API, Web, 3rd-party data)
   └─ Streaming (logs, IoT, events)
   │
   ▼
Data Ingestion
   │
   ├─ Batch Ingestion (scheduled ETL)
   ├─ Streaming Ingestion (real-time events)
   └─ API ingestion (REST / webhook)
   │
   ▼
Data Storage Layer
   │
   ├─ Data Lake (S3 / GCS / ADLS)
   │   → Raw / unprocessed data
   │
   ├─ Data Warehouse (BigQuery / Redshift / Synapse)
   │   → Structured analytics data
   │
   └─ Data Lakehouse (modern hybrid concept)
   │
   ▼
Data Processing (ETL / ELT)
   │
   ├─ Clean missing values
   ├─ Transform data
   ├─ Feature engineering
   └─ Aggregation / filtering
   │
   ▼
Feature Engineering Layer
   │
   ├─ Encoding categorical features
   ├─ Scaling numeric features
   ├─ Time-series features
   └─ Feature Store (Vertex AI / SageMaker)
   │
   ▼
Model Training
   │
   ├─ Train / validation split
   ├─ Hyperparameter tuning
   ├─ Model selection
   └─ Evaluation metrics (accuracy, F1, RMSE)
   │
   ▼
Model Registry
   │
   ├─ Version control model
   ├─ Store artifacts
   └─ Track experiments (MLflow)
   │
   ▼
Deployment
   │
   ├─ REST API (FastAPI / Flask)
   ├─ Batch prediction (offline scoring)
   └─ Real-time inference (endpoint cloud)
   │
   ▼
Monitoring
   │
   ├─ System monitoring (latency, CPU)
   ├─ Model monitoring (drift, accuracy drop)
   └─ Alerting system
   │
   ▼
Retraining Loop
   │
   ├─ Detect data drift
   ├─ Trigger retraining pipeline
   └─ Redeploy updated model
```

# 🏆 6. Roadmap Data/ML + 4 Certifications (12 tháng)

Mục tiêu:
- Nền tảng vững + có project
- Đạt 4 chứng chỉ:
  - TensorFlow Developer
  - Azure Data Scientist (DP-100)
  - Google Data Engineer
  - AWS Data Analytics

---

## 🧠 Mindmap tổng thể

```
ROADMAP DATA/ML (12M)
│
├─ 🧱 Foundation (T1-2)
│   ├─ Python / Pandas / SQL
│   ├─ Math (stats, probability)
│   └─ Mini projects (cleaning + SQL)
│   👉 Output: Code + xử lý data OK
│
├─ 📊 Data Analysis (T3-4)
│   ├─ EDA + Visualization
│   ├─ SQL advanced
│   ├─ KPI / Business thinking
│   └─ Dashboard
│   👉 Output: EDA + Dashboard
│
├─ 🤖 Machine Learning (T5-6)
│   ├─ Regression / Classification
│   ├─ Clustering
│   ├─ Feature engineering
│   └─ Evaluation
│   👉 Output: 2 ML projects
│   🎯 Cert: Azure DP-100
│
├─ 🧠 Deep Learning (T7-8)
│   ├─ Neural Network
│   ├─ CNN / NLP
│   └─ TensorFlow
│   👉 Output: CNN + NLP project
│   🎯 Cert: TensorFlow
│
├─ ☁️ Data Engineering (T9-10)
│   ├─ ETL / Pipeline
│   ├─ BigQuery / Spark
│   └─ Data flow
│   👉 Output: Pipeline project
│   🎯 Cert: Google Data Engineer
│
└─ 🚀 MLOps & Cloud (T11-12)
    ├─ API (FastAPI)
    ├─ Docker / CI/CD
    ├─ AWS (S3, Glue)
    └─ Deploy model
    👉 Output: Production project
    🎯 Cert: AWS Data Analytics
```
---

## ⚡ Lộ trình hành động (rút gọn)

### Giai đoạn 1 (T1-2)
- Học Python + Pandas + SQL
- Làm 2 mini project  
✔ Goal: Code + xử lý data được  

### Giai đoạn 2 (T3-4)
- Làm EDA + Dashboard  
✔ Goal: Biết đọc & giải thích data  

### Giai đoạn 3 (T5-6)
- Build ML model  
✔ Goal: Train + evaluate model  
🎯 Thi: Azure DP-100  

### Giai đoạn 4 (T7-8)
- Học TensorFlow + CNN/NLP  
✔ Goal: Build DL model  
🎯 Thi: TensorFlow Cert  

### Giai đoạn 5 (T9-10)
- Làm pipeline + BigQuery  
✔ Goal: Hiểu data system  
🎯 Thi: Google Data Engineer  

### Giai đoạn 6 (T11-12)
- Deploy model + Docker + AWS  
✔ Goal: Production-ready  
🎯 Thi: AWS Data Analytics  

---

## 🔥 Thứ tự thi chuẩn

1. Azure (ML core)  
2. TensorFlow (Deep Learning)  
3. Google DE (Pipeline)  
4. AWS (Hardest)  

---

## 💡 Nguyên tắc

- Học = phải có project  
- Thi = mock ≥ 70%  
- Không skip foundation  
- Luôn build song song  

---

## 🏆 Outcome

- 4 chứng chỉ quốc tế  
- 5–7 project  
- Full skill: Data → ML → Cloud  
- Level: Junior Data Scientist / ML Engineer  

---

# 🔥 7. Insight quan trọng

## 💡 7.1. Data Science = Math + Code + Business
- Không chỉ code  
- Phải hiểu dữ liệu + bài toán  

---

## 💡 7.2. Project quan trọng hơn chứng chỉ
- 1 project tốt > 10 khóa học  
- Portfolio = yếu tố quyết định  

---

## 💡 7.3. ML không phải chỉ train model
- 80% thời gian = xử lý data  
- 20% = model  

---

## 💡 7.4. Cloud = bắt buộc (với Data lớn)
- Local chỉ đủ demo  
- Production phải dùng cloud  

---

# 🚀 8. Mục tiêu cuối

## 🎯 Technical Goals
- ✔️ Làm sạch & phân tích data  
- ✔️ Build ML model  
- ✔️ Deploy model  
- ✔️ Xây pipeline data  

---

## ☁️ Cloud Goals
- ✔️ Dùng BigQuery / Redshift / Synapse  
- ✔️ Deploy ML model trên cloud  
- ✔️ Hiểu pipeline production  

---

## 🏆 Certification Goals
- ✔️ Có ≥ 1 chứng chỉ Data / ML  
- ✔️ Làm mock exam ≥ 70%  

---

## 💼 Career Goals
- ✔️ Portfolio GitHub  
- ✔️ Project thực tế  
- ✔️ Apply Data Scientist / ML Engineer  

---

## 🔥 Checklist hoàn thành

- [ ] Python + Pandas vững  
- [ ] EDA thành thạo  
- [ ] ML model chạy được  
- [ ] Deep Learning cơ bản  
- [ ] Có project thực tế  
- [ ] Deploy lên cloud  
- [ ] Có chứng chỉ  
- [ ] Sẵn sàng apply job  

---

## 🔥 Gợi ý thêm (rất đáng giá)

- 🔥 Fill đầy đủ **mindmap giống DevOps (siêu chi tiết)**  
- Hoặc làm luôn **lộ trình học 30–60–90 ngày cho Data/ML**  