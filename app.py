import streamlit as st
import pandas as pd
from datetime import datetime
import os
import hashlib
import numpy as np
import time

# Page configuration
st.set_page_config(
    page_title="Multi-Cloud Container Deployment System",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS - NAVY BLUE, GOLD & CREAM THEME
# ============================================

st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
    }
    
    /* Main Background - Navy Blue Gradient */
    .stApp {
        background: linear-gradient(135deg, #0a1922 0%, #0f2a3a 50%, #0a1922 100%);
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Sidebar - Dark Navy with Gold Accent */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1922 0%, #0f1f2a 100%);
        border-right: 2px solid #d4af37;
    }
    
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    
    h1 {
        background: linear-gradient(135deg, #d4af37 0%, #f5c542 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem !important;
    }
    
    /* Buttons - Gold Gradient */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #b8960f 100%);
        color: #0a1922 !important;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5);
        background: linear-gradient(135deg, #f5c542 0%, #d4af37 100%);
        color: #0a1922 !important;
    }
    
    /* Cards - Navy with Gold Border */
    .dashboard-card, .metric-card {
        background: linear-gradient(135deg, #0f2a3a 0%, #0a1f2a 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #d4af37;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    
    .dashboard-card:hover {
        transform: translateY(-5px);
        border-color: #f5c542;
        box-shadow: 0 12px 30px rgba(212, 175, 55, 0.2);
    }
    
    /* Dataframes */
    .stDataFrame {
        background: #0f2a3a;
        border-radius: 12px;
        border: 1px solid #d4af37;
    }
    
    .dataframe {
        background: #0f2a3a;
        color: #ffffff !important;
    }
    
    .dataframe th {
        background: #d4af37 !important;
        color: #0a1922 !important;
        font-weight: 600;
    }
    
    .dataframe td {
        background: #0f2a3a !important;
        color: #ffffff !important;
        border-color: #2a4a5a !important;
    }
    
    /* Input Fields - Cream/Gold Themed */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input {
        background-color: #f5f0e1 !important;
        border: 1px solid #d4af37 !important;
        border-radius: 10px !important;
        color: #0a1922 !important;
        padding: 0.5rem !important;
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input {
        color: #0a1922 !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #f5c542 !important;
        box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2) !important;
    }
    
    /* Selectbox/Dropdown Styles - Make text BLACK */
    .stSelectbox > div > div {
        background-color: #f5f0e1 !important;
        border: 1px solid #d4af37 !important;
        border-radius: 10px !important;
        color: #000000 !important;
    }
    
    .stSelectbox > div > div > div {
        color: #000000 !important;
        background-color: #f5f0e1 !important;
    }
    
    /* Dropdown menu items */
    div[data-baseweb="select"] > div {
        background-color: #f5f0e1 !important;
        color: #000000 !important;
    }
    
    div[data-baseweb="select"] ul {
        background-color: #f5f0e1 !important;
        color: #000000 !important;
    }
    
    div[data-baseweb="select"] li {
        background-color: #f5f0e1 !important;
        color: #000000 !important;
    }
    
    div[data-baseweb="select"] li:hover {
        background-color: #d4af37 !important;
        color: #000000 !important;
    }
    
    /* Selectbox value display */
    .stSelectbox [data-baseweb="select"] span {
        color: #000000 !important;
        font-weight: 500;
    }
    
    /* Labels */
    label {
        color: #ffffff !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #0f2a3a;
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #0a1922;
        color: #ffffff !important;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        border: 1px solid #d4af37;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #d4af37 0%, #b8960f 100%);
        color: #0a1922 !important;
        border: none;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #0f2a3a 0%, #0a1922 100%);
        color: #ffffff !important;
        border-radius: 10px;
        border: 1px solid #d4af37;
        font-weight: 600;
    }
    
    .streamlit-expanderContent {
        background: #0a1922;
        border-radius: 0 0 10px 10px;
        border: 1px solid #d4af37;
        border-top: none;
        color: #ffffff !important;
    }
    
    /* Alerts */
    .stAlert {
        background: #0f2a3a !important;
        border-left: 4px solid #d4af37 !important;
        color: #ffffff !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background-color: #d4af37 !important;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background: #0a1922 !important;
        border: 1px solid #d4af37 !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    
    /* Status indicators */
    .status-running {
        color: #d4af37;
        font-weight: 600;
    }
    
    /* Card styling */
    .gold-card {
        background: linear-gradient(135deg, #0f2a3a 0%, #0a1922 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #d4af37;
        margin: 0.5rem 0;
    }
    
    .gold-card-title {
        color: #d4af37 !important;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .gold-card-value {
        color: #ffffff !important;
        font-size: 2rem;
        font-weight: 800;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main .block-container {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a1922;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #d4af37;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #f5c542;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1.5rem;
        margin-top: 2rem;
        border-top: 1px solid #d4af37;
        color: #ffffff !important;
        font-size: 0.8rem;
    }
    
    /* Login/Register Container */
    .auth-container {
        background: linear-gradient(135deg, #0f2a3a 0%, #0a1922 100%);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid #d4af37;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        margin-bottom: 1rem;
    }
    
    /* Welcome Section */
    .welcome-section {
        text-align: center;
        padding: 3rem;
        background: linear-gradient(135deg, #0f2a3a 0%, #0a1922 100%);
        border-radius: 20px;
        border: 1px solid #d4af37;
        margin-bottom: 2rem;
    }
    
    /* Metrics and text */
    .stMetric {
        color: #ffffff !important;
    }
    
    .stMetric label {
        color: #ffffff !important;
    }
    
    /* Info/Warning/Success boxes */
    .stAlert div {
        color: #ffffff !important;
    }
    
    /* Selectbox text - Ensure BLACK */
    .stSelectbox div div div {
        color: #000000 !important;
    }
    
    /* Number input text */
    .stNumberInput input {
        color: #0a1922 !important;
    }
    
    /* Text area text */
    .stTextArea textarea {
        color: #0a1922 !important;
    }
    
    /* Markdown text */
    .markdown-text-container p {
        color: #ffffff !important;
    }
    
    /* DataFrame text */
    .dataframe tbody tr td {
        color: #ffffff !important;
    }
    
    /* Expander content text */
    .streamlit-expanderContent p, 
    .streamlit-expanderContent div,
    .streamlit-expanderContent span {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Data directory setup
DATA_DIR = "multi_cloud_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "deployments" not in st.session_state:
    st.session_state.deployments = []
if "selected_cloud" not in st.session_state:
    st.session_state.selected_cloud = None
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"
if "show_register" not in st.session_state:
    st.session_state.show_register = False

# ============================================
# DATABASE FUNCTIONS
# ============================================

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def init_database():
    """Initialize CSV database files with proper columns"""
    
    # Users table
    users_file = os.path.join(DATA_DIR, "users.csv")
    if not os.path.exists(users_file):
        users = pd.DataFrame(columns=[
            "user_id", "username", "password_hash", "full_name", 
            "email", "phone", "user_role", "class_level", 
            "date_registered", "last_login"
        ])
        users.to_csv(users_file, index=False)
    
    # Cloud Providers
    providers_file = os.path.join(DATA_DIR, "cloud_providers.csv")
    if not os.path.exists(providers_file):
        providers = pd.DataFrame(columns=[
            "provider_id", "provider_name", "api_endpoint", 
            "regions", "is_active", "date_added"
        ])
        providers.to_csv(providers_file, index=False)
    
    # Environments
    envs_file = os.path.join(DATA_DIR, "environments.csv")
    if not os.path.exists(envs_file):
        envs = pd.DataFrame(columns=[
            "env_id", "env_name", "cloud_provider", "region", 
            "config", "created_by", "date_created"
        ])
        envs.to_csv(envs_file, index=False)
    
    # Deployments
    deployments_file = os.path.join(DATA_DIR, "deployments.csv")
    if not os.path.exists(deployments_file):
        deployments = pd.DataFrame(columns=[
            "deployment_id", "app_name", "cloud_provider", "env",
            "status", "started_at", "completed_at", "logs", "deployed_by"
        ])
        deployments.to_csv(deployments_file, index=False)
    else:
        deployments = pd.read_csv(deployments_file)
        if "deployed_by" not in deployments.columns:
            deployments["deployed_by"] = ""
            deployments.to_csv(deployments_file, index=False)
    
    # Workloads
    workloads_file = os.path.join(DATA_DIR, "workloads.csv")
    if not os.path.exists(workloads_file):
        workloads = pd.DataFrame(columns=[
            "workload_id", "workload_name", "namespace", "environment",
            "image", "replicas", "status", "health_score", "created_by"
        ])
        workloads.to_csv(workloads_file, index=False)
    else:
        workloads = pd.read_csv(workloads_file)
        if "created_by" not in workloads.columns:
            workloads["created_by"] = ""
            workloads.to_csv(workloads_file, index=False)

def load_data():
    """Load all data safely"""
    users = pd.read_csv(os.path.join(DATA_DIR, "users.csv"))
    providers = pd.read_csv(os.path.join(DATA_DIR, "cloud_providers.csv"))
    envs = pd.read_csv(os.path.join(DATA_DIR, "environments.csv"))
    deployments = pd.read_csv(os.path.join(DATA_DIR, "deployments.csv"))
    workloads = pd.read_csv(os.path.join(DATA_DIR, "workloads.csv"))
    return users, providers, envs, deployments, workloads

def save_users(users_df):
    """Save users dataframe to CSV"""
    users_df.to_csv(os.path.join(DATA_DIR, "users.csv"), index=False)

def save_deployments(deployments_df):
    """Save deployments dataframe to CSV"""
    deployments_df.to_csv(os.path.join(DATA_DIR, "deployments.csv"), index=False)

def save_workloads(workloads_df):
    """Save workloads dataframe to CSV"""
    workloads_df.to_csv(os.path.join(DATA_DIR, "workloads.csv"), index=False)

# Initialize database
init_database()

# ============================================
# REGISTRATION FUNCTION
# ============================================

def register_user(username, password, full_name, email, phone, user_role, class_level=""):
    """Register a new user"""
    users_df = pd.read_csv(os.path.join(DATA_DIR, "users.csv"))
    
    if username in users_df["username"].values:
        return False, "Username already exists."
    
    if email in users_df["email"].values:
        return False, "Email already registered."
    
    new_id = users_df["user_id"].max() + 1 if not users_df.empty else 1
    
    new_user = pd.DataFrame([{
        "user_id": new_id,
        "username": username,
        "password_hash": hash_password(password),
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "user_role": user_role,
        "class_level": class_level if class_level else "",
        "date_registered": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_login": ""
    }])
    
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    save_users(users_df)
    
    return True, "Registration successful!"

# ============================================
# AUTHENTICATION FUNCTION - FIXED
# ============================================

def authenticate_user(username, password):
    """Authenticate user with CSV database"""
    users_df = pd.read_csv(os.path.join(DATA_DIR, "users.csv"))
    hashed_password = hash_password(password)
    
    user = users_df[(users_df["username"] == username) & (users_df["password_hash"] == hashed_password)]
    
    if not user.empty:
        user_dict = user.iloc[0].to_dict()
        
        # FIX: Convert last_login column to string type to avoid dtype issues
        if "last_login" in users_df.columns:
            users_df["last_login"] = users_df["last_login"].astype(str)
        
        # Update timestamp as string
        users_df.loc[users_df["username"] == username, "last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_users(users_df)
        return True, user_dict
    
    return False, None

# ============================================
# CLOUD PROVIDER FUNCTIONS
# ============================================

def get_available_providers():
    """Get list of available cloud providers"""
    providers = [
        {"name": "AWS", "icon": "☁️", "regions": ["us-east-1", "us-west-2", "eu-west-1"]},
        {"name": "Azure", "icon": "🔷", "regions": ["eastus", "westus2", "northeurope"]},
        {"name": "GCP", "icon": "🟢", "regions": ["us-central1", "europe-west1", "asia-southeast1"]}
    ]
    return providers

def deploy_to_cloud(cloud_name, app_name, replicas, region, username):
    """Mock deployment function"""
    logs = []
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 Starting deployment to {cloud_name}")
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 👤 Deployed by: {username}")
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 📦 Application: {app_name}")
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🌍 Region: {region}")
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🔄 Replicas: {replicas}")
    
    time.sleep(1)
    
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Creating container registry")
    time.sleep(0.5)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🐳 Building container image")
    time.sleep(0.5)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 📤 Pushing image to {cloud_name} container registry")
    time.sleep(0.5)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] ⚙️ Configuring load balancer")
    time.sleep(0.5)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🎉 Deployment completed successfully!")
    
    return {
        "status": "success",
        "logs": "\n".join(logs),
        "deployment_id": f"dep_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    }

# ============================================
# UI COMPONENTS
# ============================================

def show_registration():
    """Display registration form"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 4rem;">🌟</div>
        <h1>Create an Account</h1>
        <p style="color: #ffffff;">Join the Multi-Cloud Deployment Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Full Name *", placeholder="John Doe")
            username = st.text_input("Username *", placeholder="johndoe")
            email = st.text_input("Email *", placeholder="john@example.com")
            phone = st.text_input("Phone Number", placeholder="+1234567890")
        
        with col2:
            password = st.text_input("Password *", type="password", placeholder="••••••••")
            confirm_password = st.text_input("Confirm Password *", type="password", placeholder="••••••••")
            user_role = st.selectbox("Role *", ["student", "teacher", "devops", "admin"])
            class_level = st.text_input("Class Level (for students)", placeholder="e.g., Grade 10")
        
        st.markdown("---")
        
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            submitted = st.form_submit_button("📝 Register", use_container_width=True)
        with col_btn2:
            if st.form_submit_button("← Back to Login", use_container_width=True):
                st.session_state.show_register = False
                st.rerun()
        
        if submitted:
            if not full_name or not username or not password or not email:
                st.error("Please fill in all required fields (*)")
            elif password != confirm_password:
                st.error("Passwords do not match!")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long!")
            else:
                success, message = register_user(
                    username, password, full_name, email, phone, user_role, class_level
                )
                
                if success:
                    st.success(message)
                    st.balloons()
                    time.sleep(1.5)
                    st.session_state.show_register = False
                    st.rerun()
                else:
                    st.error(message)

def show_login():
    """Display login form"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 4rem;">🌟</div>
        <h1>Welcome Back</h1>
        <p style="color: #ffffff;">Login to access the Multi-Cloud Deployment Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            submitted = st.form_submit_button("🔐 Login", use_container_width=True)
        with col_btn2:
            if st.form_submit_button("📝 New User? Register", use_container_width=True):
                st.session_state.show_register = True
                st.rerun()
        
        if submitted:
            if not username or not password:
                st.error("Please enter both username and password")
            else:
                success, user = authenticate_user(username, password)
                
                if success:
                    st.session_state.authenticated = True
                    st.session_state.current_user = user
                    st.success(f"✅ Welcome back, {user['full_name']}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password. Please register for an account.")
    
    st.markdown("---")
    st.markdown("### 👋 Demo Accounts")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Admin Demo**\nUsername: `admin`\nPassword: `admin`")
    with col2:
        st.info("**DevOps Demo**\nUsername: `devops`\nPassword: `devops`")

def show_dashboard():
    """Main dashboard view"""
    # Header with greeting
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    st.markdown(f"""
    <div style="margin-bottom: 2rem;">
        <h1>{greeting}, {st.session_state.current_user['full_name']}!</h1>
        <p style="color: #ffffff; font-size: 1.1rem;">Welcome to your Multi-Cloud Command Center 🌟</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    _, providers_df, envs_df, deployments_df, workloads_df = load_data()
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="dashboard-card" style="text-align: center;">
            <div style="font-size: 2rem;">☁️</div>
            <div class="gold-card-title">Active Clouds</div>
            <div class="gold-card-value">{len(providers_df) if not providers_df.empty else 3}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="dashboard-card" style="text-align: center;">
            <div style="font-size: 2rem;">🌍</div>
            <div class="gold-card-title">Environments</div>
            <div class="gold-card-value">{len(envs_df)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if not deployments_df.empty and "deployed_by" in deployments_df.columns:
            user_deployments = len(deployments_df[deployments_df["deployed_by"] == st.session_state.current_user["username"]])
        else:
            user_deployments = 0
        st.markdown(f"""
        <div class="dashboard-card" style="text-align: center;">
            <div style="font-size: 2rem;">🚀</div>
            <div class="gold-card-title">My Deployments</div>
            <div class="gold-card-value">{user_deployments}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        running = len(workloads_df[workloads_df["status"] == "running"]) if not workloads_df.empty else 0
        st.markdown(f"""
        <div class="dashboard-card" style="text-align: center;">
            <div style="font-size: 2rem;">⚙️</div>
            <div class="gold-card-title">Running Workloads</div>
            <div class="gold-card-value">{running}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent Deployments
    st.markdown('<h2>📊 Recent Deployments</h2>', unsafe_allow_html=True)
    
    if not deployments_df.empty and "deployed_by" in deployments_df.columns:
        user_deployments_df = deployments_df[deployments_df["deployed_by"] == st.session_state.current_user["username"]]
        if not user_deployments_df.empty:
            recent = user_deployments_df.tail(5)
            st.dataframe(recent[["app_name", "cloud_provider", "env", "status", "started_at"]], use_container_width=True)
        else:
            st.info("You haven't made any deployments yet. Go to the Deploy page to create your first deployment!")
    else:
        st.info("No deployments yet. Create your first deployment!")
    
    # System Health
    st.markdown('<h2>🩺 System Health</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="gold-card"><div class="gold-card-title">Cloud Provider Status</div>', unsafe_allow_html=True)
        providers = get_available_providers()
        for provider in providers:
            st.markdown(f'<p style="color: #d4af37;">🟢 <strong>{provider["name"]}</strong> - All systems operational</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="gold-card"><div class="gold-card-title">Active Incidents</div>', unsafe_allow_html=True)
        st.markdown('<p style="color: #ffffff;">✅ No active incidents</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def show_deployment():
    """Deployment interface"""
    st.markdown("""
    <h1>🚀 Multi-Cloud Deployment</h1>
    <p style="color: #ffffff; margin-bottom: 2rem;">Deploy your containerized applications across AWS, Azure, and GCP</p>
    """, unsafe_allow_html=True)
    
    with st.form("deployment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            app_name = st.text_input("Application Name", placeholder="my-app")
            container_image = st.text_input("Container Image", placeholder="nginx:latest")
            replicas = st.number_input("Number of Replicas", min_value=1, max_value=10, value=3)
        
        with col2:
            cloud_provider = st.selectbox(
                "Target Cloud Provider",
                ["AWS", "Azure", "GCP", "Multi-Cloud (All)"]
            )
            
            if cloud_provider == "AWS":
                region = st.selectbox("Region", ["us-east-1", "us-west-2", "eu-west-1"])
            elif cloud_provider == "Azure":
                region = st.selectbox("Region", ["eastus", "westus2", "northeurope"])
            elif cloud_provider == "GCP":
                region = st.selectbox("Region", ["us-central1", "europe-west1", "asia-southeast1"])
            else:
                region = st.selectbox("Region", ["us-east-1", "eastus", "us-central1"])
            
            environment = st.selectbox("Environment", ["dev", "staging", "production"])
        
        submitted = st.form_submit_button("🚀 Deploy Application", use_container_width=True)
        
        if submitted:
            if not app_name:
                st.error("Please enter an application name")
            else:
                with st.spinner(f"Deploying {app_name} to {cloud_provider}..."):
                    username = st.session_state.current_user["username"]
                    
                    if cloud_provider == "Multi-Cloud (All)":
                        providers = ["AWS", "Azure", "GCP"]
                        results = []
                        for provider in providers:
                            result = deploy_to_cloud(provider, app_name, replicas, region, username)
                            results.append(result)
                        
                        st.success(f"✅ Successfully deployed to {', '.join(providers)}!")
                        
                        for i, result in enumerate(results):
                            with st.expander(f"📋 Deployment Logs - {providers[i]}"):
                                st.code(result["logs"], language="bash")
                    else:
                        result = deploy_to_cloud(cloud_provider, app_name, replicas, region, username)
                        
                        if result["status"] == "success":
                            st.success(f"✅ Successfully deployed {app_name} to {cloud_provider}!")
                            
                            with st.expander("📋 View Deployment Logs"):
                                st.code(result["logs"], language="bash")
                            
                            # Save deployment record
                            deployments_df = pd.read_csv(os.path.join(DATA_DIR, "deployments.csv"))
                            new_deployment = pd.DataFrame([{
                                "deployment_id": result["deployment_id"],
                                "app_name": app_name,
                                "cloud_provider": cloud_provider,
                                "env": environment,
                                "status": "success",
                                "started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "logs": result["logs"],
                                "deployed_by": username
                            }])
                            deployments_df = pd.concat([deployments_df, new_deployment], ignore_index=True)
                            save_deployments(deployments_df)
                            
                            # Add to workloads
                            workloads_df = pd.read_csv(os.path.join(DATA_DIR, "workloads.csv"))
                            new_workload = pd.DataFrame([{
                                "workload_id": len(workloads_df) + 1,
                                "workload_name": app_name,
                                "namespace": environment,
                                "environment": environment,
                                "image": container_image,
                                "replicas": replicas,
                                "status": "running",
                                "health_score": 100,
                                "created_by": username
                            }])
                            workloads_df = pd.concat([workloads_df, new_workload], ignore_index=True)
                            save_workloads(workloads_df)
                            
                            st.rerun()
                        else:
                            st.error("Deployment failed. Check logs for details.")

def show_workloads():
    """Workload management interface"""
    st.markdown("""
    <h1>📦 Workload Management</h1>
    <p style="color: #ffffff; margin-bottom: 2rem;">Monitor and manage your deployed container workloads</p>
    """, unsafe_allow_html=True)
    
    workloads_df = pd.read_csv(os.path.join(DATA_DIR, "workloads.csv"))
    
    if workloads_df.empty:
        st.info("No workloads deployed yet. Go to the Deployment page to deploy applications.")
    else:
        if "created_by" in workloads_df.columns:
            user_workloads = workloads_df[workloads_df["created_by"] == st.session_state.current_user["username"]]
        else:
            user_workloads = workloads_df
        
        if user_workloads.empty:
            st.info("You haven't deployed any workloads yet.")
        else:
            st.dataframe(
                user_workloads[["workload_name", "environment", "image", "replicas", "status", "health_score"]],
                use_container_width=True
            )
            
            st.markdown("---")
            st.markdown('<h2>🔧 Workload Actions</h2>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                workload_to_scale = st.selectbox(
                    "Select Workload to Scale",
                    user_workloads["workload_name"].tolist()
                )
                new_replicas = st.number_input("New Replica Count", min_value=1, max_value=20, value=3)
                
                if st.button("Scale Workload", use_container_width=True):
                    st.success(f"✅ Scaling {workload_to_scale} to {new_replicas} replicas")
                    workloads_df.loc[workloads_df["workload_name"] == workload_to_scale, "replicas"] = new_replicas
                    save_workloads(workloads_df)
                    st.rerun()
            
            with col2:
                workload_to_restart = st.selectbox(
                    "Select Workload to Restart",
                    user_workloads["workload_name"].tolist(),
                    key="restart_select"
                )
                
                if st.button("Restart Workload", use_container_width=True):
                    with st.spinner(f"Restarting {workload_to_restart}..."):
                        time.sleep(2)
                        st.success(f"✅ {workload_to_restart} restarted successfully")

def show_monitoring():
    """Monitoring dashboard"""
    st.markdown("""
    <h1>📊 Monitoring & Observability</h1>
    <p style="color: #ffffff; margin-bottom: 2rem;">Real-time metrics across all cloud environments</p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="gold-card"><div class="gold-card-title">📈 CPU Usage</div>', unsafe_allow_html=True)
        chart_data = pd.DataFrame({
            "AWS": np.random.randint(30, 70, 10),
            "Azure": np.random.randint(25, 65, 10),
            "GCP": np.random.randint(35, 75, 10)
        })
        st.line_chart(chart_data)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="gold-card"><div class="gold-card-title">💾 Memory Usage</div>', unsafe_allow_html=True)
        memory_data = pd.DataFrame({
            "AWS": np.random.randint(40, 80, 10),
            "Azure": np.random.randint(35, 75, 10),
            "GCP": np.random.randint(45, 85, 10)
        })
        st.line_chart(memory_data)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="gold-card"><div class="gold-card-title">🚦 Active Alerts</div>', unsafe_allow_html=True)
        alerts = [
            {"severity": "warning", "message": "High CPU usage on AWS cluster", "time": "2 min ago"},
            {"severity": "info", "message": "New deployment successful to Azure", "time": "5 min ago"},
            {"severity": "critical", "message": "GCP region experiencing latency", "time": "15 min ago"}
        ]
        
        for alert in alerts:
            if alert["severity"] == "critical":
                st.error(f"🔴 {alert['message']} - {alert['time']}")
            elif alert["severity"] == "warning":
                st.warning(f"⚠️ {alert['message']} - {alert['time']}")
            else:
                st.info(f"ℹ️ {alert['message']} - {alert['time']}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="gold-card"><div class="gold-card-title">📊 Deployment Success Rate</div>', unsafe_allow_html=True)
        success_rate = 98.5
        st.progress(success_rate / 100)
        st.write(f"Success Rate: {success_rate}% over last 30 days")
        st.markdown('</div>', unsafe_allow_html=True)

def show_configuration():
    """Infrastructure as Code configuration"""
    st.markdown("""
    <h1>⚙️ Infrastructure as Code</h1>
    <p style="color: #ffffff; margin-bottom: 2rem;">Define your infrastructure using declarative templates</p>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Terraform", "Pulumi", "CloudFormation"])
    
    with tab1:
        st.subheader("Terraform Configuration")
        terraform_template = st.text_area(
            "Terraform HCL",
            value='''# Multi-cloud Terraform Configuration
provider "aws" {
  region = "us-east-1"
}

resource "kubernetes_deployment" "app" {
  metadata {
    name = "my-app"
    labels = {
      app = "my-app"
    }
  }
  
  spec {
    replicas = 3
    
    selector {
      match_labels = {
        app = "my-app"
      }
    }
    
    template {
      metadata {
        labels = {
          app = "my-app"
        }
      }
      
      spec {
        container {
          image = "nginx:latest"
          name  = "my-app"
          
          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
          }
        }
      }
    }
  }
}''',
            height=300
        )
        
        if st.button("Validate Terraform", key="tf_validate"):
            st.success("✅ Terraform configuration is valid")
        
        if st.button("Apply Configuration", key="tf_apply"):
            st.success("🚀 Configuration applied successfully to all cloud providers")
    
    with tab2:
        st.subheader("Pulumi Configuration")
        st.code('''
import pulumi
from pulumi_kubernetes import apps

app_labels = {"app": "my-app"}
deployment = apps.v1.Deployment(
    "my-app",
    spec=apps.v1.DeploymentSpecArgs(
        replicas=3,
        selector=apps.v1.LabelSelectorArgs(match_labels=app_labels),
        template=apps.v1.PodTemplateSpecArgs(
            metadata=apps.v1.ObjectMetaArgs(labels=app_labels),
            spec=apps.v1.PodSpecArgs(
                containers=[apps.v1.ContainerArgs(
                    name="my-app",
                    image="nginx:latest"
                )]
            )
        )
    )
)
''', language="python")
    
    with tab3:
        st.subheader("AWS CloudFormation")
        st.code('''
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ECSTaskDefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "Family": "my-app",
        "Cpu": "256",
        "Memory": "512",
        "ContainerDefinitions": [
          {
            "Name": "my-app",
            "Image": "nginx:latest",
            "Essential": true
          }
        ]
      }
    }
  }
}
''', language="json")

def show_cost_optimization():
    """Cost optimization dashboard"""
    st.markdown("""
    <h1>💰 Cost Optimization</h1>
    <p style="color: #ffffff; margin-bottom: 2rem;">Track and optimize cloud spending across providers</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="gold-card">', unsafe_allow_html=True)
        st.metric("Monthly Cloud Spend", "$12,450", "-$1,200")
        st.write("AWS: $4,200")
        st.write("Azure: $3,800")
        st.write("GCP: $4,450")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="gold-card">', unsafe_allow_html=True)
        st.metric("Cost Optimization Savings", "$2,300", "+18%")
        st.write("Reserved Instances: $1,200")
        st.write("Rightsizing: $800")
        st.write("Spot Instances: $300")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="gold-card">', unsafe_allow_html=True)
        st.metric("Cost Efficiency Score", "87/100", "+5")
        st.progress(0.87)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<h2>💰 Cost Trends</h2>', unsafe_allow_html=True)
    
    cost_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "AWS": [3800, 3900, 4000, 4100, 4150, 4200],
        "Azure": [3200, 3300, 3450, 3600, 3700, 3800],
        "GCP": [3900, 4000, 4100, 4250, 4300, 4450]
    })
    
    st.line_chart(cost_data.set_index("Month"))
    
    st.markdown("---")
    st.markdown('<h2>💡 Optimization Recommendations</h2>', unsafe_allow_html=True)
    
    recommendations = [
        "Consider moving dev workloads to spot instances - potential savings: $450/month",
        "Reserved instance purchase opportunity for GCP compute - 30% discount available",
        "Underutilized AWS instances detected - rightsizing could save $200/month"
    ]
    
    for rec in recommendations:
        st.info(f"💡 {rec}")

# ============================================
# MAIN APPLICATION
# ============================================

def main():
    """Main application entry point"""
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 3rem;">🌟</div>
            <h2 style="color: #d4af37; margin-top: 0.5rem;">Multi-Cloud</h2>
            <p style="color: #ffffff;">Deployment Manager</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        
        menu_options = ["Dashboard", "🚀 Deploy", "📦 Workloads", "📊 Monitoring", "⚙️ IaC", "💰 Cost Optimization"]
        
        if not st.session_state.authenticated:
            # Professional repositioning - Login and Register in the sidebar with better organization
            with st.container():
                st.markdown("### 🔐 Authentication")
                st.markdown("---")
                
                if not st.session_state.get("show_register", False):
                    # Show login form in sidebar
                    username = st.text_input("Username", placeholder="Enter username", key="sidebar_username")
                    password = st.text_input("Password", type="password", placeholder="Enter password", key="sidebar_password")
                    
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("🔐 Login", use_container_width=True, key="sidebar_login"):
                            if username and password:
                                success, user = authenticate_user(username, password)
                                if success:
                                    st.session_state.authenticated = True
                                    st.session_state.current_user = user
                                    st.rerun()
                                else:
                                    st.error("Invalid credentials")
                            else:
                                st.error("Please enter credentials")
                    
                    with col2:
                        if st.button("📝 Register", use_container_width=True, key="sidebar_register_btn"):
                            st.session_state.show_register = True
                            st.rerun()
                    
                    st.markdown("---")
                    st.markdown("#### Demo Accounts")
                    st.info("**Admin:** admin/admin\n**DevOps:** devops/devops")
                else:
                    # Show registration form in sidebar
                    st.markdown("### 📝 Create Account")
                    reg_username = st.text_input("Username*", placeholder="Choose username", key="reg_username")
                    reg_password = st.text_input("Password*", type="password", placeholder="Choose password", key="reg_password")
                    reg_confirm = st.text_input("Confirm Password*", type="password", placeholder="Confirm password", key="reg_confirm")
                    reg_fullname = st.text_input("Full Name*", placeholder="Your full name", key="reg_fullname")
                    reg_email = st.text_input("Email*", placeholder="your@email.com", key="reg_email")
                    reg_phone = st.text_input("Phone", placeholder="Phone number", key="reg_phone")
                    reg_role = st.selectbox("Role*", ["student", "teacher", "devops", "admin"], key="reg_role")
                    reg_class = st.text_input("Class Level", placeholder="e.g., Grade 10", key="reg_class")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("✅ Register", use_container_width=True, key="reg_submit"):
                            if not reg_username or not reg_password or not reg_fullname or not reg_email:
                                st.error("Please fill all required fields (*)")
                            elif reg_password != reg_confirm:
                                st.error("Passwords do not match")
                            elif len(reg_password) < 6:
                                st.error("Password must be at least 6 characters")
                            else:
                                success, msg = register_user(reg_username, reg_password, reg_fullname, reg_email, reg_phone, reg_role, reg_class)
                                if success:
                                    st.success(msg)
                                    st.balloons()
                                    time.sleep(1)
                                    st.session_state.show_register = False
                                    st.rerun()
                                else:
                                    st.error(msg)
                    
                    with col2:
                        if st.button("← Back", use_container_width=True, key="reg_back"):
                            st.session_state.show_register = False
                            st.rerun()
        else:
            # User is authenticated - show user info and menu
            st.markdown(f"""
            <div style="padding: 1rem; background: linear-gradient(135deg, #0f2a3a 0%, #0a1922 100%); border-radius: 12px; border: 1px solid #d4af37;">
                <p style="color: #d4af37; font-weight: 600; margin: 0;">👤 {st.session_state.current_user['full_name']}</p>
                <p style="color: #ffffff; font-size: 0.8rem; margin: 0;">@{st.session_state.current_user['username']}</p>
                <p style="color: #f5c542; font-size: 0.8rem; margin: 0;">Role: {st.session_state.current_user['user_role'].upper()}</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")
            
            for option in menu_options:
                if st.button(option, use_container_width=True, key=f"menu_{option}"):
                    st.session_state.page = option
                    st.rerun()
            
            st.markdown("---")
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.current_user = None
                st.session_state.show_register = False
                st.rerun()
    
    # Main content
    if not st.session_state.authenticated:
        # Professional welcome section with repositioned auth options
        st.markdown("""
        <div class="welcome-section">
            <div style="font-size: 5rem;">🌟</div>
            <h1>Multi-Cloud Container<br>Deployment System</h1>
            <p style="font-size: 1.2rem; color: #ffffff; margin: 1rem 0;">
                Deploy, manage, and optimize containerized applications across AWS, Azure, and GCP
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 2rem;">
                <div style="background: linear-gradient(135deg, #d4af37 0%, #b8960f 100%); padding: 1rem 2rem; border-radius: 12px; color: #0a1922; font-weight: 600;">
                    🚀 Multi-Cloud Deployment
                </div>
                <div style="background: linear-gradient(135deg, #d4af37 0%, #b8960f 100%); padding: 1rem 2rem; border-radius: 12px; color: #0a1922; font-weight: 600;">
                    📊 Unified Monitoring
                </div>
                <div style="background: linear-gradient(135deg, #d4af37 0%, #b8960f 100%); padding: 1rem 2rem; border-radius: 12px; color: #0a1922; font-weight: 600;">
                    💰 Cost Optimization
                </div>
            </div>
            <p style="margin-top: 2rem; color: #ffffff;">
                Please use the sidebar to login or create an account
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature highlights
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="gold-card" style="text-align: center;">
                <div style="font-size: 2rem;">☁️</div>
                <h3>Multi-Cloud Support</h3>
                <p>Deploy to AWS, Azure, and GCP seamlessly</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="gold-card" style="text-align: center;">
                <div style="font-size: 2rem;">📊</div>
                <h3>Unified Monitoring</h3>
                <p>Centralized observability across all clouds</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="gold-card" style="text-align: center;">
                <div style="font-size: 2rem;">💰</div>
                <h3>Cost Optimization</h3>
                <p>Intelligent cost management and recommendations</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        page = st.session_state.get("page", "Dashboard")
        
        if page == "Dashboard":
            show_dashboard()
        elif page == "🚀 Deploy":
            show_deployment()
        elif page == "📦 Workloads":
            show_workloads()
        elif page == "📊 Monitoring":
            show_monitoring()
        elif page == "⚙️ IaC":
            show_configuration()
        elif page == "💰 Cost Optimization":
            show_cost_optimization()
        else:
            show_dashboard()
    
    # Footer
    st.markdown("""
    <div class="footer">
        🌟 Multi-Cloud Container Deployment System | Powered by Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
