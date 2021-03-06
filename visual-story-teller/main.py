#!/usr/bin/env python3
"""
visual-story-teller
"""
import markdown
import importlib
import os
import shutil
from nameTagExtension import NameTagExtension

__author__ = "dong-eileen"
__version__ = "0.1.0"
__license__ = "MIT"

# Create a new file with the same filename as inputFilePath but different path and extension.
def getOutputFilePath(inputFilePath, outputPath, extension):
    baseFileName = getBaseFileName(inputFilePath)
    return os.path.join(outputPath, f"{baseFileName}.{extension}")

# Strip the path and extensions off of a file name. Supports files that start with a .
def getBaseFileName(filePath):
    baseFileName = os.path.splitext(os.path.basename(filePath))[0]
    while baseFileName.find('.') != -1 and baseFileName[0] != '.':
        baseFileName = os.path.splitext(os.path.basename(baseFileName))[0]
    return baseFileName

# Create a directory if it doesn't yet exist.
def initializeDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Convert markdown files to html and dump them in the directory specified by outputPath.
def createHtmlFromMarkdown(converter, inputFilePath, outputPath):
    initializeDirectory(outputPath)
    outputFilePath = getOutputFilePath(inputFilePath, outputPath, "html.tmp")
    converter.convertFile(inputFilePath, output = outputFilePath)
    return outputFilePath

# Reads and writes the entire contents of an input file to an outputFile. Client is responsible for closing outputFile.
def writeFile(inputFilePath, outputFile, spacing=0):
    inputFile = open(inputFilePath, 'r')
    indentation = ' ' * spacing
    for line in inputFile:
        outputFile.write(indentation + line)
    inputFile.close()

# Replaces title and body of the chapter template with the body given at inputFilePath, and outputs the result to outputPath/<input file name>.html
def fillChapterTemplate(inputFilePath, outputPath):
    templateFile = open(os.path.join("static", "chapterTemplate.html"), "r")
    print(getOutputFilePath(inputFilePath, outputPath, "html"))
    outputFile = open(getOutputFilePath(inputFilePath, outputPath, "html"), "w")
    title = "Chapter " + getBaseFileName(inputFilePath)
    for line in templateFile:
        if "CHAPTER_TITLE" in line:
            outputFile.write(line.replace("CHAPTER_TITLE", title))
        elif "INSERT_BODY" in line:
            writeFile(inputFilePath, outputFile, 8)
        else:
            outputFile.write(line)
    outputFile.close()
    templateFile.close()

# Returns a stringified JSON representing a character, given the name
def createCharacterObject(fileName):
    name = getBaseFileName(fileName)
    print(name)
    return f"""
        {name.lower()}: {{
            name: "{name}",
            imagePath: "./images/{name.lower()}.png"
        }},"""

# Generates character.js that stores the JSON representation of characters and image paths
def generateCharacterFile(inputPath, outputPath):
    outputFile = open(os.path.join(outputPath, "characters.js"), "w")
    outputFile.write("let characters = {\n")
    for filename in os.listdir(inputPath):
        inputFilePath = os.path.join(inputPath, filename)
        if os.path.isfile(inputFilePath):
            outputFile.write(createCharacterObject(filename))
    outputFile.write("\n};\n")
    outputFile.write("\nconst getDetailsFor = name => characters[name];\n")
    outputFile.close()

# Deletes files that end with specific extensions in a directory.
def cleanFiles(path, extensions):
    for filename in os.listdir(path):
        filePath = os.path.join(path, filename)
        if os.path.isfile(filePath) and os.path.splitext(filename)[1] in extensions:
            os.remove(filePath)

# Given an ../input/ folder in the base directory with Markdown files, convert those Markdown files to HTML, put them inside a template, and put them in an ../output/ folder.
def main():
    converter = markdown.Markdown(extensions = [NameTagExtension()], output_format = "html5")

    print("*** Generating Chapter Files ***")
    inputPath = os.path.join(os.pardir, "input")
    outputPath = os.path.join(os.pardir, "output")

    chaptersPath = os.path.join(inputPath, "chapters")
    for filename in os.listdir(chaptersPath):
        inputFilePath = os.path.join(chaptersPath, filename)
        if os.path.isfile(inputFilePath):
            outputFilePath = createHtmlFromMarkdown(converter, inputFilePath, outputPath)
            fillChapterTemplate(outputFilePath, outputPath)

    charactersPath = os.path.join(inputPath, "characters", "images")

    print("*** Copying css, js, and image files ***")
    shutil.copytree(os.path.join("static", "css"), os.path.join(outputPath, "css"));
    shutil.copytree(os.path.join("static", "js"), os.path.join(outputPath, "js"));
    shutil.copytree(charactersPath, os.path.join(outputPath, "images"));

    print("*** Generating character files ***")
    generateCharacterFile(charactersPath, os.path.join(outputPath, "js"))

    cleanFiles(outputPath, [".tmp"])

if __name__ == "__main__":
    main()