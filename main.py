import json

#load the json file
with open("knowledge_base.json", "r") as file:
    kb = json.load(file)

def main():
    print("MEDICAL EXPERT SYSTEM")
    print("Rule-Based Diagnosis with Forward Chaining")
    
if __name__ == "__main__":
    main()
    