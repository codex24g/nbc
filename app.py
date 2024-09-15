import logging
import os
from flask import Flask, request, render_template, jsonify
from PIL import Image, ImageOps
import torch
import json
import io
from pyngrok import ngrok
import uuid
import numpy as np
from torchvision import transforms
import streamlit as st

# Streamlit app that writes "Hello World"
st.title("Hello World with Streamlit")

st.write("This is a simple app using the following libraries:")
st.write("- Flask")
st.write("- Pillow (PIL)")
st.write("- PyTorch")
st.write("- pyngrok")
st.write("- NumPy")
st.write("- TorchVision")

st.write("Hello, World!")
