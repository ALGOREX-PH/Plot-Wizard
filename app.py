import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import warnings
import google.generativeai as genai
from apikey import google_gemini_api_key
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
import chartbots.Linus_Line_Chart as Linus_Line_Chart
import streamlit_book as stb

warnings.filterwarnings("ignore")
st.set_page_config(page_title="PlotWizard : Unleash the Magic of Data Visualization!", page_icon="📊", layout="wide")

# Created by Danielle Bagaforo Meer (Algorex)
# LinkedIn : https://www.linkedin.com/in/algorexph/

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'chat_session' not in st.session_state:
    st.session_state.chat_session = None

genai.configure(api_key=google_gemini_api_key)
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 32768,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

with st.sidebar :
    st.write("AI Republics Logo Here")
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    
    options = option_menu(
        "Dashboard", 
        ["Home", "Line Chart", "Violin Chart", "Histogram Chart", "Boxplot Chart", "Barplot Chart", "Waterfall Chart", "Scatter Plot Chart", "Horizontal Bar Chart", "Pie Chart", "Area Chart", "Step Chart", "Stem Chart", "Hexbin Chart", "Polar Plot Chart", "Quiver Plot Chart", "Stream Plot Chart", "Contour Plot Chart", "Filled Contour Plot Chart", "Heatmap Chart", "3D Surface Chart", "3D Line Chart", "3D Scatter Chart", "3D Bar Chart", "Radar Chart", "Dendrogram Chart", "Horizontal Broken Bar", "Event Plot Chart", "Stacked Bar Chart", "Logarithmic Chart", "Auto Correlation Chart", "Cross Correlation Chart", "Ternary Chart", "Bubble Chart", "Density Chart", "Parallel Coordinates Chart", "Donut Chart", "Andrews Curves Chart", "Lag Plot Chart", "Spectrogram Chart", "Anchor Plot Chart", "Vector Field Chart"],
        icons = ['house', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart','bar-chart', 'bar-chart'],
        menu_icon = "book", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        })
    
if options == "Home":
    st.title("PlotWizard : Unleash the Magic of Data Visualization! 🧙‍♂️📈")
    st.write("## Welcome to PlotWizard!")
    st.write("Your ultimate companion for exploring the world of data visualization. Whether you’re a beginner trying to understand basic chart types or a professional looking to sharpen your visualization skills, PlotWizard makes learning about data visualization fun, interactive, and easy to grasp.")
    st.write("With PlotWizard, you can generate random charts with just a click, receive detailed explanations about them, and even get personalized help from our built-in chatbot ChartBots. Ready to get started? Let us guide you!")
    st.write("### 1. Generate a Random Chart")
    st.write("- At the heart of PlotWizard is the 'Generate Chart' button. Each time you click it, a unique chart will be generated from a variety of chart types such as:")
    st.write("- **Bar charts**")
    st.write("- **Line graphs**")
    st.write("- **Pie charts**")
    st.write("- **Scatter plots**")
    st.write("- **Histograms and more!**")
    st.write("- Along with each chart, you’ll see a detailed description explaining:")
    st.write("- What the chart represents.")
    st.write("- The type of data it is best suited for.")
    st.write("- When and how to use it effectively in your data analysis.")
    st.write("Each chart is designed to help you get familiar with different ways to visualize data. It’s perfect for those who want to explore new chart types or need inspiration for presenting their data.")
    st.write("### 2. Learn More with ChartBot")
    st.write("- Meet the ChartBot, your virtual chart assistant! ChartBot is here to answer all your questions about data visualization.")
    st.write("Have questions like:")
    st.write("- “When should I use a scatter plot instead of a line graph?”")
    st.write("- “How do I interpret a histogram?”")
    st.write("- “Which chart type is best for comparing categories over time?”")
    st.write("Simply ask the ChartBot, and it will provide a clear and comprehensive answer to guide you in selecting and interpreting charts.")
    st.write("**What ChartBot can help you with:**")
    st.write("Explanation of each chart type and its purpose.")
    st.write("Best practices for visualizing different kinds of data.")
    st.write("Recommendations for choosing the right chart based on your dataset.")
    st.write("Examples of how specific chart types are used in real-world scenarios.")
    st.write("### 3. Get Practical Examples")
    st.write("- Every time you generate a chart, PlotWizard will also provide a real-world example of how that chart can be used to solve practical problems or represent data.")
    st.write("- Learn by seeing how professionals in fields like marketing, finance, healthcare, and science use different types of charts to represent their data.")
    st.write("- Use these examples as inspiration for applying similar charts to your own data projects.")
    st.write("### 4. Hands-on Practice")
    st.write("After reviewing the chart and the example provided, we encourage you to try building your own charts! Whether you have data you want to visualize or are experimenting with new datasets, PlotWizard equips you with the knowledge to create impactful visuals.")
    st.write("You can start with small datasets, practice applying the right chart, and build your confidence in reading and creating visualizations.")
    st.write("")
    st.write("## Why Choose PlotWizard?")
    st.write("### **Interactive Learning:**")
    st.write("Explore various chart types hands-on, and gain a deep understanding of when and how to use them effectively. Each generated chart is designed to give you a fresh look at data visualization.")
    st.write("### **Detailed Explanations:**")
    st.write("No more guessing! Each chart is accompanied by a detailed description that breaks down its purpose, data application, and best use cases. This way, you can ensure you're using the right visualization method for your data.")
    st.write("### **Personalized Guidance with the ChartBot:**")
    st.write("Our unique ChartBot is here to assist with any chart-related questions you may have. Whether you're confused about the best way to represent your data or just want to learn more about visualization techniques, ChartBot is here to help.")
    st.write("### **Real-World Applications:**")
    st.write("Each chart includes examples of how it's used in professional settings, helping you connect the theory with practical applications. Understand how different industries leverage data visualization to make better decisions.")
    st.write("### **Improve Your Skills:**")
    st.write("Whether you're preparing for a presentation, working on a data science project, or just expanding your skill set, PlotWizard offers a simple and engaging way to improve your understanding of charts and graphs. You'll walk away confident in your ability to visualize data effectively.")
    st.write("## Get Started!")
    st.write("Ready to generate your first chart? Simply click the “Generate Chart” button and see what type of chart appears! Start learning by exploring the description, interacting with ChartBot, and reviewing the provided examples.")
    st.write("Have a specific question? Don’t hesitate to ask ChartBot for guidance.")

elif options == "Line Chart":

     def generate_random_line_chart():
         x = np.linspace(0, 10, 100)
         y = np.random.randn(100).cumsum()
         fig, ax = plt.subplots()
         ax.plot(x, y)
         ax.set_title("Random Line Chart")
         ax.set_xlabel("X-axis")
         ax.set_ylabel("Y-axis")
         return fig

     st.title("Line Chart")
     st.write("Line charts are powerful visualizations designed to help you easily understand data trends over time. By connecting individual data points with a continuous line, this chart makes it effortless to observe and analyze changes and patterns, especially in datasets that have a chronological sequence. Each line in the chart corresponds to a particular data set or variable, making it particularly effective when you want to compare multiple variables over the same period.")
     st.write("## Purpose:")
     st.write("The primary purpose of a line chart is to visualize changes, trends, and patterns in data over time or another continuous variable, like distance or progression in a process. It's ideal for detecting trends—whether upward, downward, cyclical, or constant—and helps in making predictions based on historical data.")
     st.write("## Data Application:")
     st.write("Line charts are especially effective when working with time-series data, such as:")
     st.write("- Sales Figures: Observe monthly or quarterly revenue, and track performance.")
     st.write("- Stock Market Prices: Display fluctuations in stock prices over weeks, months, or years.")
     st.write("- Website Traffic: Analyze user visits or engagement levels across a given period.")
     st.write("- Weather Data: Track changes in temperature, rainfall, or other meteorological data over time.")
     st.write("The chart excels at making long-term trends clear and easily understandable. For example, a business might track its revenue over time to spot periods of growth or decline, while a scientist could use a line chart to show temperature variations over the course of several seasons.")
     st.write("## Best Use Cases:")
     st.write("- **Tracking Progress Over Time:** Line charts are perfect for tracking the growth or decline of a variable over a specific time frame, such as monthly sales figures, project milestones, or website user growth.")
     st.write("- **Comparing Multiple Variables:** When you need to compare how several variables perform or change over the same period (e.g., revenue from different regions), a line chart with multiple lines makes it easy to see how they move in relation to each other.")
     st.write("- **Spotting Trends and Patterns:** Whether you’re looking for seasonal trends, long-term growth, or sudden dips, a line chart helps you quickly spot these patterns in the data.")
     st.write("- **Forecasting:** Since line charts make trends visible, they are often used to forecast future data points based on historical trends. For example, if sales are increasing steadily each month, the line chart can help predict future sales.")
     st.write("## When to Use a Line Chart:")
     st.write("- You have continuous data (usually time-based) and want to show the relationship or trend.")
     st.write("- You need to compare multiple datasets over the same continuous variable.")
     st.write("- You're interested in identifying turning points or key changes in your data (like sudden drops or spikes).")
     st.write("However, avoid using line charts when your data points are disconnected or when you're dealing with categorical data that doesn’t follow a sequential pattern. In such cases, bar or column charts may be more suitable.")
     st.write("In conclusion, line charts are an essential tool for spotting trends, analyzing performance, and comparing multiple variables over time. By providing a clear, visual representation of data, line charts allow you to make informed decisions based on historical and current data patterns.")


     st.title("Random Line Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_line_chart()
        st.pyplot(chart)

     st.write("## Chat with ChartBot : Linus")
     st.write("Meet Linus the Line Chart Expert, your AI-powered assistant designed to help you master the world of line charts! Linus is not just an ordinary chatbot—he’s a highly specialized AI programmed to guide you through everything you need to know about line charts. Whether you’re just getting started or are looking to refine your data visualization skills, Linus is here to make the process simple, efficient, and insightful.")
     st.write("As your virtual data coach, Linus can answer all your questions about line charts—from choosing the right datasets to analyzing trends and comparing multiple lines. He’s methodical, calm, and always ready to offer clear, concise explanations. Want to understand the best use cases for line charts? Curious about how to spot trends over time? Linus can help you with that and much more.")
     st.write("Thanks to his deep knowledge and thoughtful approach, Linus will not only help you build and optimize line charts but also empower you to make data-driven decisions with confidence. So go ahead, chat with Linus and explore the endless possibilities of what line charts can reveal about your data!")

     System_Prompt = """
Role:
You are Linus the Line Chart Expert, a highly knowledgeable and approachable guide specializing in all aspects of line charts. Your purpose is to help users understand, create, analyze, and troubleshoot line charts. You offer clear, methodical, and analytical advice, ensuring that users can confidently work with line charts at any skill level. Maintain a professional yet friendly tone, making even complex topics accessible to all.

Instructions:
Offer specific and actionable guidance on line charts, including their creation, interpretation, and troubleshooting.
Explain when and why line charts are the best option, emphasizing their strengths in tracking trends, comparisons over time, and data analysis.
Help users identify and fix problems with their line charts, such as incorrect scaling, axis labeling, dataset comparisons, and trend visualization.
Provide best practices for line chart design, such as appropriate intervals, formatting, and techniques for highlighting key trends or data points.
Engage users in a way that encourages learning and experimentation, keeping all advice focused on line charts.
Adapt your responses to suit the user’s level of experience, from beginners needing basic explanations to experts seeking advanced insights.
Context:
Users will seek your expertise with various questions related to line charts, ranging from fundamental concepts to more advanced analytical techniques. Some may need help with the basics, like understanding how to plot a line chart, while others may request detailed advice on improving the clarity or accuracy of their visualizations. Your responses should be tailored to the specific needs of the user, ensuring that all feedback is practical and relevant to their line chart queries.

Constraints:
Keep all guidance focused solely on line charts; do not provide information about other types of charts (e.g., bar charts, scatter plots).
Avoid giving general data visualization advice. Ensure that your responses are specific to line charts.
Do not divert into unrelated topics or concepts not tied to line charts.
Simplify explanations for less experienced users but offer detailed, advanced advice when required.
Stay focused on answering the user's questions thoroughly without providing unnecessary information.
Examples:
Example 1:
User: What’s the best way to compare trends from two datasets on a line chart?
Linus: To compare trends from two datasets, plot each dataset as a separate line on the same chart. Use distinct colors or line styles to differentiate them. Ensure that both lines share the same x-axis for time or categories, and label the y-axis clearly to represent the data being compared. Adding a legend will help clarify which line corresponds to which dataset.

Example 2:
User: How do I show a clear upward trend in a line chart?
Linus: To highlight an upward trend, make sure your data points are evenly spaced along the x-axis, representing the timeline or categories. Consider using a trendline to smooth out fluctuations, which will emphasize the overall direction of the data. You can also annotate key points, such as peak values or milestones, to make the trend more visible.

Example 3:
User: How should I label the axes on my line chart?
Linus: Axis labels are essential for clarity. The x-axis usually represents time or categories, while the y-axis shows the values being measured. Make sure the labels are descriptive but concise. For instance, if you’re charting sales performance over months, your x-axis label could be 'Months,' and the y-axis label 'Sales Revenue (in USD).' Ensure that your labels help users quickly understand the data being presented without overwhelming them with too much text.
"""
    # Function to initialize conversation, ensuring it's only done once
     def initialize_conversation(prompt):
         # Check if the session has been initialized
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             # Add initial prompt to messages only once
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             # Mark session as initialized
             st.session_state.chat_initialized = True

     # Initialize conversation with "Sell\nAstro Serpent" only if not already done
     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     # Display chat messages
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message("context : Spaceship_Model = Galactic Pathfinder, Lightyears_Traveled = 108K Lightyears, Type_of_Propulsion = Ion Thruster, Spacecraft_Maintenance_Contract = Cosmic Shield Coverage, Crew_Capacity = 4 Crew Members, Energy_Source = Quantum Reactor, Registration_Code = SPC-2724, Features_Description = Standard Spacecraft Features, Current_Damages = Hull Dents, Modifications = Weaponized Plasma Cannons, Enhancements = Advanced Navigation Systems, Overheating = No, Core_Reactor_Anomalies = Yes, Power_Cell_Replacement = Required, Viewports_Front_Left = Clear, Viewports_Front_Right = Clear, Viewports_Rear_Left = Clear, Viewports_Rear_Right = Clear, Transparent_Armor_Windshield = Minor Damage, Transparent_Armor_Backshield = Minor Damage, Side_Visual_Enhancer_Lens = Functional, Navigation_Lights_Front_Left = Operational, Navigation_Lights_Front_Right = Operational, Navigation_Lights_Rear_Left = Operational, Navigation_Lights_Rear_Right = Operational, Atmospheric_Scanner_Lamps = Operational, Deceleration_Indicators = Functional, Plasma_Thruster_Front_Left_Lifespan = 75%, Plasma_Thruster_Front_Right_Lifespan = 75%, Plasma_Thruster_Rear_Left_Lifespan = 75%, Plasma_Thruster_Rear_Right_Lifespan = 75%, Backup_Thruster_Lifespan = 75%, Backup_Thruster_Condition = Operational, Hatch_Controls_Front_Left = Operational, Hatch_Controls_Front_Right = Operational, Hatch_Controls_Rear_Left = Operational, Hatch_Controls_Rear_Right = Operational, Cargo_Bay_Hatch_Controls = Operational, Interior_Fabric_Condition = Worn, Control_Panel_Condition = Partially Functional, Control_Panel_Lights = Operational, Audio_System_Condition = Worn, Speaker_Condition = Worn, Energy_Port_Condition = Operational, Climate_Control_Efficiency = Suboptimal, Ventilation_System_Strength = Weak, Drive_and_Engine_Condition_Hard_Start = No, Propulsion_Shift_Delay = Severe, Unusual_Spacecraft_Sounds = Yes, Source_of_Unusual_Sounds = Unknown Source, Maneuverability = Standard Maneuverability, Shield_Response_Time = Standard Shield Response, Hull_Integrity = Minor Damage, Plasma_Leak = No Leak, Coolant_Level = Optimal, Brake_Fluid_Level = Maximum, Plasma_Color = Blue, Plasma_Flux_Viscosity = Thin \n Query : " + user_message + "\n Response : ")
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
           
def generate_random_violin_chart():
    data = np.random.randn(100)
    fig, ax = plt.subplots()
    ax.violinplot(data)
    ax.set_title("Random Violin Chart")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    return fig

def generate_random_histogram():
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.hist(data, bins=30)
    ax.set_title("Random Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    return fig

def generate_random_boxplot():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]
    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.set_title("Random Boxplot")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    return fig

def generate_random_barplot():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(1, 100, size=5)
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title("Random Barplot")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    return fig

def generate_random_waterfall_chart():
    data = np.random.randint(-50, 50, size=6)
    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data, bottom=np.maximum.accumulate(np.concatenate(([0], data[:-1]))))
    ax.set_title("Random Waterfall Chart")
    ax.set_xlabel("Step")
    ax.set_ylabel("Value")
    return fig

def generate_random_scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Random Scatter Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_horizontal_bar_chart():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(1, 100, size=5)
    fig, ax = plt.subplots()
    ax.barh(categories, values)
    ax.set_title("Random Horizontal Bar Chart")
    ax.set_xlabel("Value")
    ax.set_ylabel("Category")
    return fig

def generate_random_pie_chart():
    sizes = np.random.rand(5)
    labels = ['A', 'B', 'C', 'D', 'E']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Random Pie Chart")
    return fig

def generate_random_area_chart():
    x = np.linspace(0, 10, 100)
    y = np.random.rand(100)
    fig, ax = plt.subplots()
    ax.fill_between(x, y)
    ax.set_title("Random Area Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_step_chart():
    x = np.arange(10)
    y = np.random.randint(0, 10, 10)
    fig, ax = plt.subplots()
    ax.step(x, y)
    ax.set_title("Random Step Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_stem_plot():
    x = np.linspace(0, 2*np.pi, 20)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.stem(x, y)
    ax.set_title("Random Stem Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_hexbin_plot():
    x = np.random.standard_normal(1000)
    y = np.random.standard_normal(1000)
    fig, ax = plt.subplots()
    ax.hexbin(x, y, gridsize=20)
    ax.set_title("Random Hexbin Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_polar_plot():
    r = np.random.rand(100)
    theta = 2 * np.pi * np.random.rand(100)
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.scatter(theta, r)
    ax.set_title("Random Polar Plot")
    return fig

def generate_random_quiver_plot():
    x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
    u = np.cos(x)
    v = np.sin(y)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    ax.set_title("Random Quiver Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_stream_plot():
    x, y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
    u = -1 - x**2 + y
    v = 1 + x - y**2
    fig, ax = plt.subplots()
    ax.streamplot(x, y, u, v)
    ax.set_title("Random Stream Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_contour_plot():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    fig, ax = plt.subplots()
    ax.contour(X, Y, Z)
    ax.set_title("Random Contour Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_filled_contour_plot():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    fig, ax = plt.subplots()
    ax.contourf(X, Y, Z)
    ax.set_title("Random Filled Contour Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_heatmap():
    data = np.random.rand(10, 10)
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap='hot')
    fig.colorbar(im)
    ax.set_title("Random Heatmap")
    return fig

def generate_random_3d_surface():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_title("Random 3D Surface")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_3d_line():
    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_title("Random 3D Line")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_3d_scatter():
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = np.random.rand(100)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_title("Random 3D Scatter")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_3d_bar():
    x = np.arange(5)
    y = np.arange(5)
    z = np.random.randint(0, 10, size=(5, 5))
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X.ravel(), Y.ravel(), np.zeros_like(z).ravel(), 1, 1, z.ravel())
    ax.set_title("Random 3D Bar")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_radar_chart():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(1, 100, size=5)
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.plot(angles, values)
    ax.set_thetagrids(angles[:-1] * 180/np.pi, categories)
    ax.set_title("Random Radar Chart")
    return fig

def generate_random_dendrogram():
    X = np.random.rand(10, 10)
    Z = hierarchy.linkage(X, 'ward')
    fig, ax = plt.subplots()
    dn = hierarchy.dendrogram(Z, ax=ax)
    ax.set_title("Random Dendrogram")
    return fig

def generate_random_broken_barh():
    fig, ax = plt.subplots()
    ax.broken_barh([(10, 50), (100, 20), (130, 10)], (10, 9), facecolors=('tab:blue', 'tab:orange', 'tab:green'))
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('X-axis')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Task 1', 'Task 2'])
    ax.grid(True)
    ax.set_title("Random Broken Barh")
    return fig

def generate_random_event_plot():
    np.random.seed(42)
    num_points = 100
    num_series = 3
    data = [np.random.random(num_points) for _ in range(num_series)]
    fig, ax = plt.subplots()
    colors = plt.cm.rainbow(np.linspace(0, 1, num_series))
    for i, series in enumerate(data):
        ax.eventplot(series, colors=[colors[i]])
    ax.set_title("Random Event Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Series")
    return fig

def generate_random_stacked_bar():
    categories = ['A', 'B', 'C', 'D']
    values1 = np.random.randint(0, 100, size=4)
    values2 = np.random.randint(0, 100, size=4)
    values3 = np.random.randint(0, 100, size=4)
    fig, ax = plt.subplots()
    ax.bar(categories, values1, label='Series 1')
    ax.bar(categories, values2, bottom=values1, label='Series 2')
    ax.bar(categories, values3, bottom=values1+values2, label='Series 3')
    ax.set_title("Random Stacked Bar")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    ax.legend()
    return fig

def generate_random_logarithmic():
    x = np.logspace(0, 5, num=100)
    y = np.random.randn(100) * 100
    fig, ax = plt.subplots()
    ax.semilogx(x, y)
    ax.set_title("Random Logarithmic Plot")
    ax.set_xlabel("X-axis (log scale)")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_autocorrelation():
    np.random.seed(42)
    x = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.acorr(x, maxlags=50)
    ax.set_title("Random Autocorrelation Plot")
    ax.set_xlabel("Lag")
    ax.set_ylabel("Autocorrelation")
    return fig

def generate_random_cross_correlation():
    np.random.seed(42)
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.xcorr(x, y, maxlags=50)
    ax.set_title("Random Cross-Correlation Plot")
    ax.set_xlabel("Lag")
    ax.set_ylabel("Cross-correlation")
    return fig

def generate_random_bubble():
    np.random.seed(42)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=area, c=colors, alpha=0.5)
    ax.set_title("Random Bubble Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_density():
    np.random.seed(42)
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    sns.kdeplot(data=data, ax=ax)
    ax.set_title("Random Density Plot")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    return fig

def generate_random_parallel_coordinates():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
    fig, ax = plt.subplots()
    pd.plotting.parallel_coordinates(df, 'A', ax=ax)
    ax.set_title("Random Parallel Coordinates Plot")
    return fig

def generate_random_donut():
    sizes = [25, 20, 30, 15, 10]
    labels = ['A', 'B', 'C', 'D', 'E']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=0.85, wedgeprops=dict(width=0.5))
    ax.set_title("Random Donut Chart")
    return fig

def generate_random_andrews_curves():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
    fig, ax = plt.subplots()
    pd.plotting.andrews_curves(df, 'A', ax=ax)
    ax.set_title("Random Andrews Curves")
    return fig

def generate_random_lag_plot():
    np.random.seed(42)
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    pd.plotting.lag_plot(pd.Series(data), ax=ax)
    ax.set_title("Random Lag Plot")
    return fig


def generate_random_spectrogram():
    np.random.seed(42)
    Fs = 1000
    t = np.linspace(0, 10, 10000)
    x = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)
    fig, ax = plt.subplots()
    ax.specgram(x, Fs=Fs)
    ax.set_title("Random Spectrogram")
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    return fig

def generate_random_anchor():
    fig, ax = plt.subplots()
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = ax.plot(t, s, lw=2)
    ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.set_title("Random Anchor Plot")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    return fig

def generate_random_vector_field():
    np.random.seed(42)
    x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
    u = np.cos(x) * y
    v = np.sin(x) * y
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    ax.set_title("Random Vector Field")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig
