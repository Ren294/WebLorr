#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import copy
import argparse
import itertools
from collections import Counter
from collections import deque

# import cv2 as cv
# import numpy as np
# import mediapipe as mp

# from utils import CvFpsCalc
# from model import KeyPointClassifier
# from model import PointHistoryClassifier
import streamlit as st

import streamlit.components.v1 as components
st.set_page_config(page_title="Phân cụm", page_icon="🌐")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("# Phân cụm dựa trên dữ liệu kinh tế vĩ mô thế giới")
with open('html/world_macro_economic_overview_2015.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
html_content = f"""
<div style="height: 80vh; overflow-y: auto;">
    {html_content}
</div>
"""
# Embed the HTML content
components.html(html_content, height=700)

FRAME_WINDOW = st.image([])


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument('--use_static_image_mode', action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='min_detection_confidence',
                        type=float,
                        default=0.7)
    parser.add_argument("--min_tracking_confidence",
                        help='min_tracking_confidence',
                        type=int,
                        default=0.5)

    args = parser.parse_args()

    return args


def main():
    # Argument parsing #################################################################
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    use_static_image_mode = args.use_static_image_mode
    min_detection_confidence = args.min_detection_confidence
    min_tracking_confidence = args.min_tracking_confidence

    use_brect = True


if __name__ == '__main__':
    main()
