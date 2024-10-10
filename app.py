import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import warnings
import google.generativeai as genai
from apikey import google_gemini_api_key
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention

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
    st.image("https://raw.githubusercontent.com/ALGOREX-PH/Plot-Wizard/refs/heads/main/images/White_AI%20Republic.png")
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    
    options = option_menu(
        "Dashboard", 
        ["Home", "Line Chart", "Violin Chart", "Histogram Chart"], # "Boxplot Chart", "Barplot Chart", "Waterfall Chart", "Scatter Plot Chart", "Horizontal Bar Chart", "Pie Chart", "Area Chart", "Step Chart", "Stem Chart", "Hexbin Chart", "Polar Plot Chart", "Quiver Plot Chart", "Stream Plot Chart", "Contour Plot Chart", "Filled Contour Plot Chart", "Heatmap Chart", "3D Surface Chart", "3D Line Chart", "3D Scatter Chart", "3D Bar Chart", "Radar Chart", "Dendrogram Chart", "Horizontal Broken Bar", "Event Plot Chart", "Stacked Bar Chart", "Logarithmic Chart", "Auto Correlation Chart", "Cross Correlation Chart", "Ternary Chart", "Bubble Chart", "Density Chart", "Parallel Coordinates Chart", "Donut Chart", "Andrews Curves Chart", "Lag Plot Chart", "Spectrogram Chart", "Anchor Plot Chart", "Vector Field Chart"
        icons = ['house', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart','bar-chart', 'bar-chart'],
        menu_icon = "bar-chart", 
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

     st.write("## Chat with ChartBot : Linus the Line Chart Expert!")
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

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
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
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        

elif options == "Violin Chart":

     def generate_random_violin_chart():
         data = np.random.randn(100)
         fig, ax = plt.subplots()
         ax.violinplot(data)
         ax.set_title("Random Violin Chart")
         ax.set_xlabel("Category")
         ax.set_ylabel("Value")
         return fig
     
     st.title("Violin Chart")
     st.write("A violin chart is a versatile data visualization tool that combines elements of a box plot and a kernel density plot. It provides insights into the distribution, probability density, and frequency of a dataset, allowing you to visualize the underlying patterns within different data groups.")
     st.write("## Purpose:")
     st.write("The violin chart’s primary purpose is to show the distribution and variability of the data across different categories, similar to a box plot but with more detail. It displays both the central tendency and the spread of the data, while also highlighting the density of values at various points. The shape of the 'violins' on the chart reflects the probability density of the data, making it easier to identify clusters, trends, or outliers within each group.")
     st.write("## Data Application:")
     st.write("Violin charts are particularly useful when you want to compare distributions between different groups or categories. They are helpful in exploring:")
     st.write("- **Multi-group data distributions:** Comparing how data is distributed across different categories, such as the performance of different groups in an experiment.")
     st.write("- **Symmetry or skewness:** Visualizing whether the data is symmetrical or skewed toward one side.")
     st.write("- **Outliers:** Detecting outliers that might not be evident in a simpler plot.")
     st.write("## Best Use Cases:")
     st.write("- **When comparing distributions across multiple categories:** The violin chart is excellent when you have several groups or variables and need to compare their distributions. For example, it can be used in academic performance comparisons across different schools or age groups.")
     st.write("- **Highlighting data density:** Violin charts are effective when you want to visualize where data points are concentrated within a distribution, which helps in understanding the likelihood of specific outcomes.")
     st.write("- **Small to moderately sized datasets:** For large datasets, the density estimation in violin charts can become less meaningful; for this reason, violin charts are best used when you have a reasonable amount of data to explore.")
     st.write("## When to Use a Violin Chart")
     st.write("- When you need to compare the distribution of a continuous variable across several categories or groups, a violin chart gives a clearer picture of the differences in shape, spread, and density. For instance, if you're analyzing test scores across different school classes or regions, a violin chart can help visualize how the scores are distributed in each category.")
     st.write("- Violin charts show the full distribution of the data and make it easy to see if it’s skewed, bimodal (two peaks), or multimodal (multiple peaks). This makes it a good choice when the shape of the distribution provides important insights, such as when studying patterns in scientific experiments or sales data over time.")
     st.write("- Use violin charts when understanding the variability within your data is important. The chart shows how concentrated or spread out the data is, helping identify whether data points cluster around certain values or are widely dispersed.")
     st.write("- If a simple box plot doesn’t provide enough detail—especially when you want to see density distributions beyond just median and quartiles—a violin chart is ideal. It combines the simplicity of a box plot with the rich information of a kernel density plot, offering a more comprehensive view of the data.")
     st.write("- Violin charts are excellent at revealing whether the data is skewed to one side or has unusual data points (outliers). If identifying symmetry or skewness is critical in your analysis, such as in income distribution or survey results, a violin chart can be very informative.")
     st.write("- When your data may have more than one peak (bimodal or multimodal distributions), a violin chart highlights this feature well. This is useful in biological studies, customer segmentation, or behavioral analytics where the population might naturally split into subgroups.")
     st.write("In essence, violin charts are ideal when your analysis requires understanding the full distribution of data across categories, especially when shape, variability, and density are important factors in your insights.")

     st.title("Random Violin Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_violin_chart()
        st.pyplot(chart)

     st.write("## Chat with ChartBot : Viola the Data Virtuoso!")
     st.write("Step into the world of refined data storytelling with Viola, the Data Virtuoso. Much more than just a guide, Viola is your artistic mentor, transforming raw numbers into visual symphonies through the elegance of violin charts. With her deep passion for data and an unwavering attention to detail, Viola sees every dataset as a musical composition waiting to be performed—each point, line, and curve harmonizing to reveal insights that speak volumes.")
     st.write("Viola approaches data visualization as an art form, using her sophisticated style and musical metaphors to help you understand the rich subtleties of data distributions. She believes that just as a violinist can bring emotion to a melody, a well-crafted chart can bring clarity to complex information. With Viola, expect more than just the technicalities—she’ll help you create a visual experience that resonates, offering insights into both the science and the artistry behind data.")
     st.write("Whether you’re exploring distributions, comparing variables, or examining patterns hidden deep within your dataset, Viola’s expert guidance will lead you through with a blend of elegance and precision. Her perfectionist nature ensures that every chart you create together will not only be visually appealing but also rich in meaning, bringing harmony to your data storytelling journey.")
     st.write("## What can you expect from Viola?")
     st.write("- **Insightful Guidance:** Viola will help you understand the layers of your data through violin charts, ensuring you grasp the full scope of your distributions and outliers.")
     st.write("- **Creative Metaphors:** She uses musical analogies to explain technical concepts, making complex ideas more accessible while adding a touch of elegance to your learning process.")
     st.write("- **Visual Harmony:** Viola believes in the balance between form and function, helping you create charts that are not just informative but also visually captivating.")
     st.write("- **A Perfectionist’s Eye:** Her attention to detail ensures that your violin charts are polished, clear, and crafted to perfection, giving your data the presentation it deserves.")
     st.write("## Are you ready to compose your next data masterpiece?")
     st.write("With Viola, every dataset becomes a stage, and each chart is a performance. Whether you're a novice or a seasoned data analyst, let Viola, the Data Virtuoso be your conductor, guiding you through the intricacies of data visualization with grace and flair. Together, you’ll turn numbers into narratives and visualizations into works of art.")

     System_Prompt = """

Role: You are Viola, the Data Virtuoso, a refined expert in violin charts. You bring an elegant, artistic approach to data visualization, using musical metaphors and poetic explanations to guide users through the world of data distributions. Your mission is to help users craft visually stunning and insightful violin charts that reveal the full depth of their datasets.

Instructions :
Explain with Elegance: Provide clear, detailed guidance using musical analogies. Refer to data points as "notes," the chart’s shape as a "melody," and the overall distribution as a "composition."
Offer Detailed Guidance: Walk users through key elements of violin charts, explaining the distribution, density, bandwidth, and interquartile range with both accuracy and flair.
Encourage Creativity: Suggest artistic enhancements and creative ways to fine-tune charts, such as experimenting with bandwidth or overlaying multiple charts to compare variables.
Maintain a Refined Tone: Speak with poise and grace, balancing technical precision with warmth and approachability. Your style should reflect the harmony of music and data visualization.
Answer Questions Thoroughly: Respond to user queries with structured, insightful explanations, ensuring clarity on violin chart features and best practices.
Focus on Aesthetic Balance: Help users create charts that balance visual beauty with clarity, ensuring their data is both understandable and engaging.

Context :
You are here to assist with all aspects of violin charts. Violin charts are a unique tool for visualizing the distribution of data. The shape of the chart reflects the density of the data at various points, much like a musical composition where the intensity of notes rises and falls. You approach data visualization as an art form, helping users make their charts not only informative but also aesthetically pleasing.

Constraints :
Violin Charts Only: You exclusively provide guidance related to violin charts. For questions about other chart types, suggest users seek advice elsewhere.
Stay Within User's Knowledge Level: Tailor your explanations to the user’s skill level—simple explanations for beginners, deeper insights for more advanced users.
Avoid Overly Technical Jargon: Keep your language accessible by using analogies and metaphors that tie back to your musical theme. Make sure your explanations are clear and engaging.
Focus on Data Distribution: Stay centered on helping users visualize and understand data distributions through violin charts.
Encourage Aesthetic Enhancements: In addition to technical accuracy, promote improvements that make charts visually appealing and balanced.

Examples :
Example 1:
User: How do I interpret the shape of a violin chart?
Viola: Think of the chart as a duet played on two violins. The wider parts of the chart represent where the melody—the density of data points—is at its strongest. As the shape narrows, the music fades, indicating fewer data points. By observing these variations, you can hear the melody of your data’s distribution and discover its most prominent trends.

Example 2:
User: My chart looks cluttered. What should I do?
Viola: It seems the melody of your data is becoming muddled. I suggest adjusting the bandwidth, much like changing the tempo in a musical composition. A smaller bandwidth brings out fine details, while a larger one smooths the overall shape, creating a more flowing melody. Experiment with this adjustment to strike the perfect balance between clarity and complexity.

Example 3:
User: Can you compare two violin charts?
Viola: Absolutely! Imagine each chart as an instrument in an orchestra. Together, they create harmony or contrast. When comparing violin charts, observe where their melodies overlap. A wider shape in both charts indicates similar data densities, while a narrowing in one suggests divergence. These contrasts will reveal the subtle differences or similarities between your datasets.
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
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
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

elif options == "Histogram Chart" :
     
     def generate_random_histogram():
         data = np.random.randn(1000)
         fig, ax = plt.subplots()
         ax.hist(data, bins=30)
         ax.set_title("Random Histogram")
         ax.set_xlabel("Value")
         ax.set_ylabel("Frequency")
         return fig
     
     st.title("Histogram Chart")
     st.write("## Purpose")
     st.write("A histogram is a type of bar chart that shows the distribution of a dataset. It divides the data into intervals or 'bins' and displays the frequency or count of data points that fall into each bin. Unlike standard bar charts, histograms focus on continuous data and help visualize the shape of the data's distribution, such as whether it's skewed, has outliers, or is normally distributed.")
     st.write("## Data Application")
     st.write("Histograms are best suited for numerical data, especially when you want to understand how data points are spread across different ranges. It is ideal for analyzing the distribution of variables like age, income, or test scores. You can also identify key patterns in the data, such as clustering or gaps, and recognize statistical properties such as central tendency and variability.")
     st.write("Best Use Cases")
     st.write("- **Distribution analysis:** Perfect for understanding how your data is spread over different ranges, like income levels in a population or frequency of certain grades in a test.")
     st.write("- **Detecting outliers:** Easily spot unusual data points that stand far outside the range of most data values.")
     st.write("- **Determining data shape:** Check if your data follows a normal distribution, is skewed, or has multiple peaks (bimodal).")
     st.write("- **Continuous data insights:** Useful when analyzing continuous variables where each bin represents a range of values rather than discrete categories.")
     st.write("## When to Use a Histogram Chart")
     st.write("A histogram is ideal when you want to understand how your data is distributed. For example, if you're analyzing the distribution of test scores, a histogram will show how frequently scores fall within specific ranges.")
     st.write("Histograms help reveal the overall shape of your data, whether it’s normal (bell-shaped), skewed, uniform, or bimodal. This is useful in determining the tendencies of the dataset.")
     st.write("When you need to detect outliers or unusual data points that don't fit into the general distribution pattern, histograms make it easier to spot extreme values that may require further analysis.")
     st.write("Histograms are best for continuous data, where the data can take any value within a range. Examples include age, income, weight, or temperature, where the variable isn't confined to specific categories but can vary fluidly.")
     st.write("If you want to compare how often data points fall within certain intervals or ranges, a histogram provides a visual breakdown of these frequencies. It helps to show where data is concentrated or sparse.")
     st.write("Histograms work well with large datasets where you're interested in summarizing the data into a visual format, making it easier to interpret the spread and central tendency.")
     st.write("Overall, Use a histogram when you're dealing with continuous data and want to analyze the distribution, detect patterns like skewness or outliers, or when you want to visualize the frequency of data points within different intervals.")

     st.title("Random Histogram Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_histogram()
        st.pyplot(chart)

     st.write("## Chat with ChartBot : Hector the Frequency Wizard!")
     st.write("Step into the magical world of data analysis with Hector the Frequency Wizard, your go-to expert for everything related to frequency distributions! Whether you’re navigating histograms, bar charts, or any other visualization that deals with how often data points appear, Hector is here to guide you with his enchanting blend of expertise and wizardry.")
     st.write("As a master of uncovering patterns in data, Hector makes even the most complex frequency distributions feel like a walk in the park. He can help you understand how your data is spread across intervals, identify common trends, and visualize the shape of your data distribution with clarity. From dissecting the peaks and valleys of histograms to comparing categories with bar charts, Hector ensures that you’re always one step ahead in your analysis.")
     st.write("With his mystical ability to turn raw numbers into meaningful insights, Hector transforms your understanding of frequency-based charts into a powerful tool for decision-making. Think of him as your personal frequency guide, ready to break down complicated concepts into simple, digestible explanations")
     st.write("Prepare to unlock the secrets hidden within your data, and let Hector cast his spell to reveal the bigger picture. Ready to begin your data adventure? Chat with Hector the Frequency Wizard now and see the magic unfold!")

     System_Prompt = """

Role:
You are Hector the Frequency Wizard, an expert in frequency distributions and charts such as histograms and bar charts. Your role is to assist users by explaining concepts related to frequency, helping them interpret and analyze frequency-based charts, and guiding them through data visualization with magical flair. You bring a unique, enchanting tone to your explanations, making frequency analysis fun and engaging.

Instructions:
Provide clear, concise, and accurate explanations related to frequency distributions, histograms, bar charts, and other frequency-based visualizations.
Use magical metaphors and a wizardly tone to keep the conversation light-hearted and engaging while ensuring users understand key concepts.
Offer step-by-step guidance when users are working with specific charts or datasets, explaining how to interpret frequency, distribution, and patterns.
When appropriate, introduce advanced concepts like bin sizes, skewness, and kurtosis, ensuring explanations remain approachable.
Give recommendations on how to improve chart clarity and accuracy when users are facing challenges.
Be patient and adaptable to different levels of understanding, providing more detailed explanations when needed.
Encourage users to explore and experiment with different visualizations to gain deeper insights from their data.
Context:
Hector’s role is to help users who are analyzing data that involves frequency. These users may range from beginners to advanced data analysts, and Hector is expected to provide assistance that matches their level of expertise. The users may be working with a variety of charts, most commonly histograms and bar charts, to understand how often data points appear within specific ranges or categories. Hector is also expected to inject charm and personality into his responses, making the experience not only educational but also enjoyable.

Hector is wise and approachable, always eager to share his magical insights, yet pragmatic and clear when providing guidance. He avoids overwhelming users with jargon unless it's necessary for deeper analysis and will always be ready to explain or break down complex topics.

Constraints:
Do not overwhelm users with overly technical terms unless specifically asked for deeper knowledge. Always explain technical terms in a simple way.
Avoid non-frequency-related charts or concepts unless specifically asked. Hector’s expertise is solely in frequency-based visualizations.
Maintain a magical, lighthearted tone throughout conversations, using wizardly phrases and metaphors to explain concepts.
Keep responses focused on the task at hand. Do not stray into unrelated topics, ensuring users stay on track with their frequency analysis.
Avoid offering direct solutions or completing tasks for users (e.g., generating code or producing charts). Instead, focus on guiding users to understand the process.
Don’t assume the user’s level of understanding. Ask for clarification when unsure and adjust explanations based on their responses.
Examples:
User Query:
"I’m not sure how to read this histogram. What do the bars mean?"
Hector’s Response:
"Ah, young apprentice! These bars represent the frequency of data points within specific ranges, known as 'bins.' Each bar shows you how many data points fall into that bin’s range. The taller the bar, the more data points exist in that range. Think of it as counting how many magical creatures are in each part of the enchanted forest!"

User Query:
"What is bin size, and how do I choose it for my histogram?"
Hector’s Response:
"Ah, choosing the right bin size is like deciding the size of your wizard’s cauldron—too small, and the brew overflows; too big, and you lose the magic! The bin size determines the range each bar in the histogram covers. A smaller bin size reveals more details but can be overwhelming, while a larger one simplifies the chart but may hide subtle patterns. Choose a size that balances clarity and detail, like picking the perfect potion bottle."

User Query:
"I have a bar chart, but I’m unsure what it tells me."
Hector’s Response:
"Ah, a fine question! Your bar chart shows the frequency of different categories in your data, much like tallying how many potions you’ve brewed for each spell. Each bar represents a category, and the height of the bar tells you how many times that category appears in your dataset. The taller the bar, the more frequently it occurs. It’s a snapshot of your magical inventory!"
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
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
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})



##elif options == "Boxplot Chart" :
     
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
