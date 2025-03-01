import streamlit as st
from streamlit_option_menu import option_menu
import os
from openai import OpenAI
import time

kimi_client = OpenAI(
    api_key="sk-WcwPj9W8NKk9h9OIbhucOlhxP2Ol4o475XeS5wvOAw40fkaK", # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url="https://api.moonshot.cn/v1",
)

# Set page configuration
st.set_page_config(
    page_title="AI Interactive Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Create directory structure for pages if it doesn't exist
if not os.path.exists("pages"):
    os.makedirs("pages")

# Custom CSS
def add_custom_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5em;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 1em;
    }
    .card {
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: white;
    }
    .nav-link {
        color: white !important;
        font-weight: 500;
    }
    .nav-link:hover {
        color: #F1C40F !important;
    }
    .agent-box {
        background-color: #f0f6ff;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

add_custom_css()

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "Market", "Legal Affairs", "Analytics", "About"],
    icons=["house", "graph-up", "file-earmark-text", "bar-chart", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#2E86C1"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"color": "white", "font-size": "16px", "text-align": "center"},
        "nav-link-selected": {"background-color": "#1A5276"},
    }
)

# Main content
if selected == "Home":
    st.markdown('<h1 class="main-header">AI Interactive Platform</h1>', unsafe_allow_html=True)
    
    # Welcome section
    st.markdown("""
    ### Welcome to the AI Interactive Platform
    
    This platform provides AI-powered solutions for various business needs, including:
    
    - **Market analysis** - Get insights on market trends and competition
    - **Legal document processing** - AI-assisted legal document analysis
    - **Data analytics** - Advanced data visualization and analytics
    
    Choose a section from the navigation bar above to explore more features.
    """)
    
    # Feature showcases in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Market Analysis")
        st.write("Analyze market trends and get competitive insights using AI-powered tools.")
        st.button("Explore Market Tools", key="market_btn")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Legal Document Processing")
        st.write("Process and analyze legal documents with our advanced AI algorithms.")
        st.button("Try Legal Tools", key="legal_btn")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Data Analytics")
        st.write("Visualize and analyze your data with interactive dashboards.")
        st.button("View Analytics", key="analytics_btn")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional information
    st.markdown("""
    ### How to Use This Platform
    
    1. Navigate to different sections using the top navigation bar
    2. Each section offers specialized AI tools for specific business needs
    3. Upload data or input parameters as required by each tool
    4. Get AI-generated insights and analysis results
    
    For more information, check out the About section.
    """)

elif selected == "Market":
    st.markdown('<h1 class="main-header">Market Analysis</h1>', unsafe_allow_html=True)
    
    st.write("Welcome to the Market Analysis section. Here you can analyze market trends and get competitive insights.")
    
    # AI Interaction Interface
    st.markdown('<h1 class="main-header">AI Interaction Interface</h1>', unsafe_allow_html=True)
    
    st.write("Welcome to the AI Interaction Interface. Here you can chat with AI agents with different roles.")
    
    # Adjust column widths
    col1, col2 = st.columns((1, 3))
    
    # Agent options
    agent_options = ["Competitive Analysis", "Market Trend Analysis", "Consumer Behavior Analysis"]
    selected_agent = st.session_state.get("selected_agent", agent_options[0])
    
    # Add a column for the AI agents
    with col1:
        st.markdown('<h3 class="sub-header">AI Agents</h3>', unsafe_allow_html=True)
        
        # Display all AI agents in a vertical list
        for option in agent_options:
            # Create a unique key for each agent button
            button_key = f"agent_{option.lower().replace(' ', '_')}"
            
            # Create a container for each agent with proper styling
            agent_container = st.container()
            with agent_container:
                col_img, col_text = st.columns([1, 3])
                
                # Load and display the image using Streamlit's image display
                img_path = os.path.join("assets", f"{option.lower().replace(' ', '_')}.png")
                if os.path.exists(img_path):
                    with col_img:
                        st.image(img_path, width=60)
                
                # Display the agent name
                with col_text:
                    st.write(option)
            
            # Add some space between agents
            st.markdown("<hr style='margin: 5px 0px'>", unsafe_allow_html=True)
    
    # Add a column for the user chat interface
    with col2:
        st.markdown('<h3 class="sub-header">Chat Interface</h3>', unsafe_allow_html=True)
        
        # Initialize chat history in session state if it doesn't exist
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history in a scrollable container with a fixed height
        chat_container = st.container()
        with chat_container:
            chat_area = st.markdown("", unsafe_allow_html=True)
            chat_area.markdown(f"""
            <div style="height: 250px; overflow-y: scroll; border: 1px solid #d3d3d3; border-radius: 5px; padding: 5px">
            {'<br>'.join([f"<b>You:</b> {message['content']}" if message["role"] == "user" else f"<b>AI:</b> {message['content']}" for message in st.session_state.chat_history])}
            </div>
            """, unsafe_allow_html=True)
        
        # Add a small area for user input
        chat_input = st.text_input("Type your message here")
        
        if st.button("Send"):
            if chat_input:
                # Add user message to chat history
                st.session_state.chat_history.append({"role": "user", "content": chat_input})
                
                if "@leader" in chat_input:
                    completion = kimi_client.chat.completions.create(
                        model = "moonshot-v1-32k",
                        messages = [
                            {"role": "system", "content": "你是一个市场营销团队的leader,你会根据user给出的需求以对话的口吻给Market Trend Analysis团队分配任务，输出格式为：@Market Trend Analysis:任务内容"},
                            {"role": "user", "content": chat_input}
                        ],
                        temperature = 0.3,
                    )
                    response = f"{completion.choices[0].message.content}"
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    chat_container.empty()
                    with chat_container:
                        chat_area.markdown(f"""
                        <div style="height: 250px; overflow-y: scroll; border: 1px solid #d3d3d3; border-radius: 5px; padding: 5px">
                        {'<br>'.join([f"<b>You:</b> {message['content']}" if message["role"] == "user" else f"<b>AI:</b> {message['content']}" for message in st.session_state.chat_history])}
                        </div>
                        """, unsafe_allow_html=True)

                    time.sleep(2)
                    
                    completion = kimi_client.chat.completions.create(
                        model = "moonshot-v1-32k",
                        messages = [
                            {"role": "system", "content": "你是Market Trend Analysis的专家,你会根据需求给出专业的方案"},
                            {"role": "user", "content": response}
                        ],
                        temperature = 0.3,
                    )
                    response = f"{completion.choices[0].message.content}"
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    chat_container.empty()
                    with chat_container:
                        chat_area.markdown(f"""
                        <div style="height: 250px; overflow-y: scroll; border: 1px solid #d3d3d3; border-radius: 5px; padding: 5px">
                        {'<br>'.join([f"<b>You:</b> {message['content']}" if message["role"] == "user" else f"<b>AI:</b> {message['content']}" for message in st.session_state.chat_history])}
                        </div>
                        """, unsafe_allow_html=True)

                    time.sleep(2)
                    
                    completion = kimi_client.chat.completions.create(
                        model = "moonshot-v1-32k",
                        messages = [
                            {"role": "system", "content": "你是一个市场营销团队的leader,你会根据user给出的需求以对话的口吻给Consumer Behavior Analysis团队分配任务，输出格式为：@Consumer Behavior Analysis:任务内容"},
                            {"role": "user", "content": chat_input}
                        ],
                        temperature = 0.3,
                    )
                    response = f"{completion.choices[0].message.content}"
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    chat_container.empty()
                    with chat_container:
                        chat_area.markdown(f"""
                        <div style="height: 250px; overflow-y: scroll; border: 1px solid #d3d3d3; border-radius: 5px; padding: 5px">
                        {'<br>'.join([f"<b>You:</b> {message['content']}" if message["role"] == "user" else f"<b>AI:</b> {message['content']}" for message in st.session_state.chat_history])}
                        </div>
                        """, unsafe_allow_html=True)     

                    time.sleep(2)             

                    completion = kimi_client.chat.completions.create(
                        model = "moonshot-v1-32k",
                        messages = [
                            {"role": "system", "content": "你是Consumer Behavior Analysis的专家,你会根据需求给出专业的方案"},
                            {"role": "user", "content": response}
                        ],
                        temperature = 0.3,
                    )
                    response = f"{completion.choices[0].message.content}"
                    st.session_state.chat_history.append({"role": "assistant", "content": response})       
                    chat_container.empty()
                    with chat_container:
                        chat_area.markdown(f"""
                        <div style="height: 250px; overflow-y: scroll; border: 1px solid #d3d3d3; border-radius: 5px; padding: 5px">
                        {'<br>'.join([f"<b>You:</b> {message['content']}" if message["role"] == "user" else f"<b>AI:</b> {message['content']}" for message in st.session_state.chat_history])}
                        </div>
                        """, unsafe_allow_html=True)          
                else:
                    response = "How can I assist you today?"
                
                # Add AI response to chat history
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                
                # Rerun the app to update the chat display
                st.experimental_rerun()

elif selected == "Legal Affairs":
    st.markdown('<h1 class="main-header">Legal Affairs</h1>', unsafe_allow_html=True)
    
    st.write("Welcome to the Legal Affairs section. Here you can process and analyze legal documents.")
