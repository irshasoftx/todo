import streamlit as st

# Add your logo at the top
st.image("logo.png", width=200)

# Title with custom CSS class
st.markdown('<div class="title">Welcome to Irshasoft ToDo App 1.0</div>', unsafe_allow_html=True)

# Adding space between elements
st.write("\n\n")

# Subtitle styled in red
st.markdown('<h2 style="color:red;">Irshasoft International</h2>', unsafe_allow_html=True)

# Contact information
st.markdown("[Customer Care: http://wa.me/919562777796](http://wa.me/919562777796)")
st.write("Email: irshasoft@gmail.com")
st.write("[Instagram: https://www.instagram.com/irshasoftx/](https://www.instagram.com/irshasoftx/)")

# Adding space
st.write("\n\n")

# Useful Links Section
st.title("Useful Links")
st.write("[You Wanna Watch Top Movies? Click Here](https://www.imdb.com/list/ls055483029/)")

# Adding space
st.write("\n\n")

# Book gallery
st.title("Book Gallery")

# Sample images - replace with your own images or URLs
image_urls = [
    "./pages/20927404112712-Capture.png",
    "./pages/48847571765852-oru-pa.jpg",
    "./pages/bk_9852.jpg",
    "./pages/Vismayam.jpg",
    "./pages/41BUiQsNbqL._SY466_.jpg",
    "./pages/714711.jpg",
]

# Number of columns in the gallery
num_cols = 3

# Create a grid layout for the images
cols = st.columns(num_cols)

# Display images in a grid with captions
for index, img in enumerate(image_urls):
    with cols[index % num_cols]:
        st.image(img, caption=f"Book {index+1}", use_column_width=True)

# Contact information for the books
st.write("If you want these Books, Please Contact: +91 9562 77 77 96")

# Injecting CSS for additional styling
st.markdown(
    """
    <style>
    .title {
        color: blue;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar styling
st.sidebar.write("www.google.com")
st.sidebar.write("www.amazon.in")
st.sidebar.write("www.flipkart.com")
st.sidebar.write("www.youtube.com")
st.sidebar.write("https://chatgpt.com/")

st.camera_input("Take a Photo")