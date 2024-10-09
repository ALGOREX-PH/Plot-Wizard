import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import warnings
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention


warnings.filterwarnings("ignore")
st.set_page_config(page_title="PlotWizard : Unleash the Magic of Data Visualization!", page_icon="📊", layout="wide")

# Created by Danielle Bagaforo Meer (Algorex)
# LinkedIn : https://www.linkedin.com/in/algorexph/

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
    
if options == "Home" :
    st.title("PlotWizard : Unleash the Magic of Data Visualization! 🧙‍♂️📈")
    st.write("## Welcome to PlotWizard!")
    st.write("Your ultimate companion for exploring the world of data visualization. Whether you’re a beginner trying to understand basic chart types or a professional looking to sharpen your visualization skills, PlotWizard makes learning about data visualization fun, interactive, and easy to grasp.")
    st.write("With PlotWizard, you can generate random charts with just a click, receive detailed explanations about them, and even get personalized help from our built-in chatbot, ChartBot. Ready to get started? Let us guide you!")
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

elif options == "Line Chart" : 

     def generate_random_line_chart():
         x = np.linspace(0, 10, 100)
         y = np.random.randn(100).cumsum()
         fig, ax = plt.subplots()
         ax.plot(x, y)
         ax.set_title("Random Line Chart")
         ax.set_xlabel("X-axis")
         ax.set_ylabel("Y-axis")
         return fig
     
     st.title("Random Line Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_line_chart()
        st.pyplot(chart)

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
