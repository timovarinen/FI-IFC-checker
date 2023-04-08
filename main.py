import ifcopenshell
# Simple solution to read file if path is given or as for path  if not given
# Argument PATH is path to the IFC-file
# Returns read IFC-file

def read_ifc_file(PATH = ""):
    
    if PATH == "":
        PATH = input("Enter path to IFC-file to be read: ")
        
    try:
        ifc_file = ifcopenshell.open(PATH)
        return ifc_file
    except FileNotFoundError:
        print("File not found.")
    except:
        print('An error occurred while reading the file.') 
    return 0

###
# test to read a file and print some information about it
ifc = read_ifc_file("D:\ifc.ifc")

num_entities = len(ifc.by_type("IfcFlowSegment"))
print("Number of pipes and ducts in the IFC file:", num_entities)