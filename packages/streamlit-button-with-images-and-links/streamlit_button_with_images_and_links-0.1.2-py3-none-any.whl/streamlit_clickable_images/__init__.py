from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components
import base64

# Tell streamlit that there is a component called streamlit_clickable_images,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_button_with_images_and_links", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_button_with_images_and_links(
    key: Optional[str] = None,
    image: Optional[bin] = None,
    label: Optional[str] = None,
    width: Optional[str] = 'auto',
    height: Optional[str] = 'auto',
    labelColor: Optional[str] = 'white',
    font_size: Optional[str] = '1.5vw',
    font_family: Optional[str] = 'Century Gothic',
    link: Optional[str] = None
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key,
        image=image,
        label=label,
        width=width,
        height=height,
        labelColor = labelColor,
        font_size= font_size,
        font_family=font_family,
        link=link
    )

    return component_value


def main():
    style_css = """
        <style>
        [data-testid="stMainBlockContainer"]{
        margin:0px;
        padding:0px;
        height:100vh;
        width:100vw;
        padding-bottom:1vh;
        background-color:#303143;
        }
        </style>
        """
    st.markdown(style_css,unsafe_allow_html=True)
    st.write("## Example")
    image_link = './test.jpg'
    value = st.text_input('asd')
    bin_bg = base64.b64encode(open(image_link, "rb").read()).decode()
    value = streamlit_button_with_images_and_links(image=bin_bg, label='test', height='20vh', labelColor='white', font_size='4.5vw', link='example.com')
    st.write(value)
    st.write(value)
    st.write(123)

if __name__ == "__main__":
    main()
