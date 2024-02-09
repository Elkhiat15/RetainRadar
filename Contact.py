import streamlit as st
import webbrowser 
def app(sst):
    # ___________________________ Picture ans summary  __________________
    c1,c2 = st.columns([1,2])
    c1.image(".\Photos\profile-pic.png")
    with c2:
        st.header('About Me')
        st.markdown("I am a Computer Engineering student at Cairo University Faculty of Engineering with a focused interest in the field of machine learning and data science. Eager to elevate my skills through hands-on, cutting-edge projects.  I am ready to apply my knowledge to real-world challenges, contributing to the forefront of technology and innovation.")
        st.caption('Feb 2024')
# TODO: Myresume.pdf 
        with open('.\Resume\MyResume.pdf', "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name='Mohamed_Elkhiat_Resume',
            mime="application/octet-stream",
        )
            
    st.write('#')
    # ___________________________ Links __________________
    _,sup = st.columns([1,2])
    with sup:
        sub = st.columns(3)
        sub[0].image(".\Photos\linkedin.png", width= 50)
        LinkedIn = sub[0].button('LinkedIn')
        sub[1].image(".\Photos\github.png", width= 50)
        GitHub = sub[1].button('GitHub')
        sub[2].image(".\Photos\gmail.png", width= 50)
        Gmail = sub[2].button('Gmail')

    if LinkedIn:
        webbrowser.open('https://www.linkedin.com/in/mohammed-elkhiat-66b36521a', new=2)
    if GitHub:
        webbrowser.open('https://github.com/Elkhiat15', new=2)
    if Gmail:
        webbrowser.open('mailto: mohammed.khayyat02@eng-st.cu.edu.eg', new=2)
        
        
    