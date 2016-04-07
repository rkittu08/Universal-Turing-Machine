import ast
import xml.etree.ElementTree as ET

tree = ET.parse('I:\study\Winter - 2014 - AAA\input_turing_XOR.xml')
root = tree.getroot()
print(root)
for x in root:
    print(x.text)
    if x.tag=='ProgramTape':
        print(x)
        print(x.tag)
        l=x.attrib
        print(l)
        
        #for k in split(x.text):
         #   print("HI",k)
        k=x.text
        #k=repr(dedent(x.text))
        #print (k.translate(k.maketrans("\n\t\r", "   ")))
        k=k.replace('\n\t','')
        #k=k.replace('\t','')
        #k=ast.literal_eval(k)
        k=ast.literal_eval(k)
        print (k)
        print (k[('1','1')])
        print(type(k))
        
        #print(k[(1,1)])
        #k=k.replace('\n','')
        
        
        #k=ast.literal_eval(k)
        #print(k[('1','1')])
        #print(k)
