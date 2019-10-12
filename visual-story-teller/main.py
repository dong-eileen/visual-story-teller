#!/usr/bin/env python3
"""
visual-story-teller
"""
import markdown
import importlib
import os
from markdownExtension import VisualStoryTellerExtension

__author__ = "dong-eileen"
__version__ = "0.1.0"
__license__ = "MIT"

currPath = os.path.dirname(__file__)

def convertFile(converter, inputFilePath):
    newPath = os.path.join(currPath, os.pardir, "output")
    if not os.path.exists(newPath):
        os.makedirs(os.path.join(currPath, os.pardir, "output"))
    newFileName = os.path.splitext(os.path.basename(inputFilePath))[0] + ".html"

    converter.convertFile(inputFilePath, output = os.path.join(newPath, newFileName))

def main():
    converter = markdown.Markdown(extensions = [VisualStoryTellerExtension()], output_format = "html5")

    inputPath = os.path.join(currPath, os.pardir, "input", "chapters")
    for filename in os.listdir(inputPath):
        inputFilePath = os.path.join(inputPath, filename)
        if os.path.isfile(inputFilePath):
            convertFile(converter, inputFilePath)

if __name__ == "__main__":
    main()