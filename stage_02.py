with open("artifact.txt","r") as f:
    text = f.read()
print(text)

print(" testing to see changes in dvc.lock file")
# again run dvc repro command to see changes in dvc.lock file

print("this is second example")