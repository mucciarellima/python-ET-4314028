import os

art = '''
mmm
                                                                                
                                                                                
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


'''
steps to encode:
0. go through the ascii art and put each character into a set to establish the unique characters used in the artwork - to do
    example {' ', '%', '\n'}
1. split the ascii art into a list of strings, one for each line - done
2. count the number of lines - done
3. for each line, count the occurrences of each character AND store the counts in a LIST of TUPLES for each line - to do
    example [('m', 2),(' ', 10), ('%', 5),(' ', 15), ('\n', 1)]
4. put all the lines into a master List of Lists of Tuples - to do
5. return the master List of Lists of Tuples - to do
'''



def encodeString(stringVal):
    # Your code goes here.
    #charlist = set(stringVal)#this creates a set of unique characters in the string that was passed in
    #print("set of characters", charlist)
    prevChar=None
    counter=1
    linenumber=0
    decodelist=[]
    decodetuple=()    
    lineByLine = stringVal.split('\n')
    #linebyline23=stringVal.splitlines() this does the same thing as split('\n')
    #print("linebyline is:", lineByLine)
    #print("linebyline23 is:", linebyline23)
    prevChar=None
    
    for line in lineByLine[0:3]:
        #print("line is:", line)
        linenumber= linenumber + 1
        
        for char in line:
            if char != prevChar:#test if current char does not match previous character (leading edge detection)
                #if current character is different than previous character then
                #remember in the first iteration prevChar is None so this will always be true
                print(f'{linenumber}\"{char}\" repeats {counter} times')
                counter = 1#we reset the counter becase we have a new character
            else:# if char == prevChar then we have a repeat of the same character
                counter= counter + 1 #increment the counter
            prevChar = char#advance the previous character to current character
            #so that we can perform the perform the next iteration
                
        
        '''
        for char in line:
            if char != prevChar:#test if current char does not match previous character (leading edge detection)
                #if current character is different than previous character then
                #remember in the first iteration prevChar is None so this will always be true
                counter = 1#we reset the counter becase we have a new character
            else:# if char == prevChar then we have a repeat of the same character
                counter= counter + 1 #increment the counter
                print(f'{linenumber}\"{char}\" repeats {counter} times')
            prevChar = char#advance the previous character to current character
            #so that we can perform the compare on the next iteration
        '''
    
    #print("num of lines is", len(lineByLine))
    return #lineByLine




def decodeString(encodedList):
    # Your code goes here.
    pass



# Test cases
clear_terminal() # Clear the terminal before printing

encoded = encodeString(art)

#print(encoded)

#print(f'Encoded "{original}" to {encoded}') 
