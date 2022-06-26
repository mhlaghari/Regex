import glob
import re
def output1(path):
    outputFile = open("output_1","a")
    for line in open(path, "r"):
        for match in re.finditer(re.compile(r'\s+\w\w\w\w\w\s+X\s+'), line):
            outputFile.write(path + line)
        for match in re.finditer(re.compile(r'\s+\w\w\w\w\w\s+\w\w\w\w\s+'), line):
            outputFile.write(path + line)
    outputFile.close()
def output2(path):
    outputFile = open("output_2","a")
    for line in open(path, "r"):
        for match in re.finditer(re.compile("Short description"), line):
            outputFile.write(path + line)
        for match in re.finditer(re.compile("Field count"), line):
            outputFile.write(path + line)
    outputFile.close()
def output3(path):
    outputFile = open("output_3","a")
    for line in open(path, "r"):
        for match in re.finditer(re.compile("ABAP Dictionary"), line):
            outputFile.write(line)
        for match in re.finditer(re.compile("SAP AG"), line):
            outputFile.write(line)
    outputFile.close()
def main():
    paths = sorted(glob.glob('input/*.txt'))
    for path in paths:
        output1(path)
        output2(path)
        output3(path)
main()
