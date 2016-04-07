import xml.etree.ElementTree as ET

####### Function block for head movement and output writing ###############

def head_mov(input_tape,movement,head,blank,write):

    cur_pos= input_tape.index(head)
    l=len(input_tape)
    
        
    if movement==1 and (l-2)==cur_pos:
        
        input_tape=input_tape[:cur_pos]+write+head+blank
        
    elif movement==0 and cur_pos==0:
        
        input_tape=head+blank+write+input_tape[cur_pos+2:]
        
    else:
        if movement==1:
            
            input_tape=input_tape[:cur_pos]+write+head+input_tape[cur_pos+2:]
        else:
            
            input_tape=input_tape[:cur_pos-1]+head+input_tape[cur_pos-1]+write+input_tape[cur_pos+2:]
    result=[]
    result.append(input_tape)
    return result

####### Function "head_mov" completed ######

run='yes' ##initilization of loop variables
c=0
while (True):
    if c>0: ##this is to skip the first loop 
        run=input("\nPlease enter yes or no to run the Universal Turing Machine for a XML file: ")

    if (run.lower() =='no'):
        print("\nUniversal Turing Machine exited")
        break
    elif (run.lower() !='yes'):
        print("\nEXCEPTION: INVALID USER INPUT : Please enter a valid input")
        continue
    

    ####### Taking the XML input#######
    input_xml=input("\nEnter the XML file name along with the path: ")
    ############### Parsing the input XML file #########################
    xml_parser=ET.parse(input_xml)
    xml_root=xml_parser.getroot()
    print((xml_root.attrib)['name'])
    for x in xml_root:
        if x.tag.lower()=='iotape': ##### Loop for reading IOTape Block #####
            ####### Taking tape symbol variables and Input from IOTape ###############
            t          =(((x.text).replace('\t','')).replace('\n','')).strip() ###### Taking input into Pragram Tape ########
            io_tape_var=x.attrib
            head       =io_tape_var['head']
            io_format  =io_tape_var['format']
            in_blank   =io_tape_var['blank']

        if x.tag.lower()=='programtape':    ###### Loop for reading ProgramTape Block #######
            ####### Taking ProgramTape variables and assigning them to respective program variables ######
            pr_tape_var=x.attrib
            q          =pr_tape_var['start']
            halt       =pr_tape_var['halt']
            right      =pr_tape_var['right']
            left       =pr_tape_var['left']
            pr_blank   =pr_tape_var['blank']
            ####### Taking Program from Program Tape and assiging it to 'p' of universal Turing Machine #######
            p          =(((x.text).replace('\n','')).replace('\t','')).replace(' ','')

            #p          =ast.literal_eval((((x.text).replace('\n','')).replace('\t','')).replace(' ',''))
            ############### Parsing input XML is done ############################
    try:
        p=eval(p)

    except:
        x=0
        while (x < (len(p)-1)):
            if p[x:x+2]=="{(" or p[x:x+2]==",(" or p[x:x+2]==":(":
                p=p[:x+2]+"'"+p[x+2:]
                x=x+3
            elif p[x:x+2]==")}" or p[x:x+2]==")," or p[x:x+2]=="):" :
                p=p[:x]+"'"+p[x:]
                x=x+2
            elif p[x]==",":
                p=p[:x]+"','"+p[x+1:]
                x=x+3
            else:
                x=x+1
        p=eval(p)

    print("Input XML Parsed Successfully")

    if t.index(head)+1==len(t):
        t=t+blank
    
    print("Output Format --> "+io_format)

    print(t)

    while(q!=halt):

        
        cur_input=t[t.index(head)+1] ##reading the current input
    
        if cur_input==in_blank:
            cur_input=pr_blank

        pr_read=p[(q,cur_input)]  ##reading the program tape for next state
        print()
        print("('"+q+"', '"+cur_input+"') : ",pr_read)
        q=pr_read[0]  ## assigning the next state to tape q
        pr_output=pr_read[1]  ##reading the output to write on the input tape at head position
        movement=pr_read[2]  ## reading the next movement on the input tape

        if pr_output==pr_blank:
            pr_output=in_blank
    
        if movement == left:
            movement=0
        elif movement == right:
            movement=1

        cur_pos_main= t.index(head)

        print(t[:cur_pos_main+1]+pr_output+t[cur_pos_main+2:])    

        t=head_mov(t,movement,head,in_blank,pr_output)[0] ## redirecting the output after each state change to input tape

        print(t)
    
        if q==halt:
            print('\n'+(xml_root.attrib)['name']+" implemented on given input.")
    c=c+1
