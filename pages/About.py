import streamlit as st


st.image("logo.png", width=200)  # Add your logo here
# Using the custom CSS classes
st.markdown('<div class="title">Welcome to Irshasoft ToDo App 1.0</div>', unsafe_allow_html=True)

st.write(""  )
st.write(""  )
st.markdown('<h2 style ="color:red;">Irshasoft International</h2>',unsafe_allow_html=True)
st.markdown("Customer Care: http://wa.me/919562777796")
st.write("Email: irshasoft@gmail.com")
st.write("Instagram: https://www.instagram.com/irshasoftx/")
st.write("" )
st.write( "" )
st.write( "" )
st.write( "" )
st.write( "" )
st.write( "" )
st.title("Useful Links")
st.write("You Wanna Watch Top Movies: https://www.imdb.com/list/ls055483029/")

st.write("" )
st.write( "" )
st.write( "" )
st.write( "" )
st.write( "" )
st.write( "" )

# Sample images - replace with your own images or URLs
image_urls = [
    "20927404112712-Capture.png",
    "48847571765852-oru-pa.jpg",
    "bk_9852.jpg",
    "Vismayam.jpg",
    "41BUiQsNbqL._SY466_.jpg",
    "714711.jpg",
]

# Number of columns in the gallery
num_cols = 3

# Create a grid layout
cols = st.columns(num_cols)

# Display images in the grid
# for index, img in enumerate(image_urls):
#     cols[index % num_cols].image(img, use_column_width=True)

for index, img in enumerate(image_urls):
    with cols[index % num_cols]:
        st.image(img, caption=f"Book {index+1}", use_column_width=True)




st.write("if you want those Books Please Contact:  +91 9562 77 77 96 ")

import streamlit as st

# Injecting CSS using st.markdown
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




# Sidebar styling (using CSS class defined above)
st.sidebar.write("This is the sidebar with custom background color.")
