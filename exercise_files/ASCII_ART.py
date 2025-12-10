import os
string1 ='AAAAABBBBCCC'

art = '''


                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''
def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')



def encodeString(stringVal):
    # Your code goes here.
    #charlist = set(stringVal)#this creates a set of unique characters in the string that was passed in
    #print("set of characters", charlist)
    outputList = []
    lineTuple = ()
    prevChar=None
    counter=0
    linenumber=0
    startChrFlag=True
    lineByLine = stringVal.splitlines() #splits the string into a list of lines
            #linebyline23=stringVal.splitlines() this does the same thing as split('\n')
            #print("linebyline is:", lineByLine)
            #print("linebyline23 is:", linebyline23)
    prevChar=None
    
    for line in lineByLine:
        #print(f'processing line: {linenumber} .... ({line})')
        '''if line == "" or line == None: #skips empty lines ... for now
            #print(f"skipping empty line at L{linenumber}")
            outputList.append(('',1))
            outputList.append(('\n',1)) #add newline character at end of line
            counter=0
            linenumber= linenumber + 1 
            continue
        '''
        if line == None:
            counter=0
            continue
    
        for char in line:
            charTuple= ()
            if char != prevChar and startChrFlag != True :#test if current char does not match previous character (leading edge detection)
                #if current character is different than previous character then log the previous character and its count
                #remember in the first iteration prevChar is None so this will always be true
                #startChrFlag is used to skip this block for the first character processed becuase there is no previous character yet

                charTuple= prevChar,counter
                #print(f'Appending to outputList: {charTuple}')
                outputList.append(charTuple)
                #print(f'outputList is now: {outputList}') 
                counter = 1 #we reset the counter becuase we have a new character
                #print(f'L{linenumber},Ctr{counter},Ch\'{char}\' P\'{prevChar}\'<>')
                
            else:# if char == prevChar then we have a repeat of the same character
                counter += 1 #increment the counter
                #print(f'L{linenumber},Ctr{counter},Ch\'{char}\' P\'{prevChar}\'==')
                #print(f'test \"{prevChar}\" repeats {counter} times')
                startChrFlag= False #make sure startChrFlag is off after first character processed
                    
            
            prevChar = char#advance the previous character to current character
            #so that we can perform the perform the next iteration
        
        linenumber= linenumber + 1
        startChrFlag= False #after first line processed we turn off the startChrFlag
        #end of line processing - we need to log the last character and its count
        charTuple= prevChar,counter
        #print(f'Appending to outputList: {charTuple}')
        #print(f'End of line L{linenumber-1} reached. Appending new line character.')
        outputList.append(charTuple)
        if linenumber-1  >= 0 and linenumber < len(lineByLine):
            outputList.append(('\n',1)) #add newline character at end of line
        #print(f'outputList is now: {outputList}')
        counter=0 #reset counter for next line
        
    return outputList




def decodeString(encodedList):
    inputList = encodedList
    outputString = ''
    for charTuple in inputList:
        char = charTuple[0]
        count = charTuple[1]
        outputString += char * count #repeat the character 'count' times and append to output string 
    return outputString
 



# Test cases
clear_terminal() # Clear the terminal before printing

encoded = encodeString(art)
print(f'here is the encoded string of characters {encoded}')

##decoded = decodeString(encoded)
#print(f'here is the decoded string of characters:\n{decoded}')

#print(encoded)

#print(f'Encoded "{original}" to {encoded}') 
