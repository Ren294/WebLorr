import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Phân tích dữ liệu kinh tế vĩ mô - Nhóm 2")

st.sidebar.success("Chọn ở trên")

st.markdown(
    """
    <div class="red-text">
        Hello! Thank you for visiting my website. Here are the projects I have learned through the Digital Image Processing courses taught by Mr. Tran Tien Duc.
        This website is created for the purpose of reporting the final projects.
        👉 You can choose one of the projects I have learned on the left side.
         <p><b style="font-size: 40px;">Thành viên nhóm:</b></p>
        <div>
        <ul>
	      <li>Nguyen Trung Nghia - 21110560 </li>
        <li>Nguyen Trung Nghia - 21110560 </li>
        <li>Nguyen Trung Nghia - 21110560 </li>
        <li>Nguyen Trung Nghia - 21110560 </li>
        </ul>
        - School name: HCMC University of Technology and Education
        </div>
	<p><b style="font-size: 40px;">Instructor Information:</b></p>
   	<div>
        <p>- Teacher: Tran Trong Binh</p>
    </div>
    """,
    unsafe_allow_html=True
)
