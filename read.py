#! /usr/bin/env python
#coding=utf-8


Tor = []
non_Tor = []
Tor_tag = 'Tor'
Notor_tag = 'non-Tor'
Tor_list = []
Notor_list = []
isTor = False
isNotor = False
with open(r'D:\test\read_test\test_3.txt','r') as f:
    for line in f.readlines():
        if line.strip('\n')== Tor_tag:
            Tor_list.append([])
            isTor = True
            isNotor = False
            continue
        if line.strip('\n') == Notor_tag:
            Notor_list.append([])
            isNotor = True
            isTor = False
            continue
        if isTor:
           Tor_list[-1].append(line.strip('\n'))
        if isNotor:
           Notor_list[-1].append(line.strip('\n'))

print(Notor_list)
        
            
#with open(r'D:\test\read_test\test_3.txt','r') as f:
#    while not f.readline().strip('\n') == '':
#        l = []
#        line = f.readline().strip('\n')
#        if line == 'Tor':
#            while True:
#                Tor_line = f.readline().strip('\n')
#                if Tor_line == 
            
        
        
            
 
#    for line in f.readlines():
#        line.strip('\n')
#        if line == 'Tor':
#            l = []
#        while True:
#            line = f.readline().strip('\n')
#            l = []
#            p = []
#            if line == 'Tor':
#                
#                while True:
#                    Tor_line = f.readline().strip('\n')
#                    if Tor_line == 'non-Tor' and not f.readline().strip('\n') == '':
#                    elif Tor_line == '':
#                        break
#                    else:
#                        l.append(Tor_line)
#                Tor.append(l)
#            elif line == 'non-Tor':
#                
#                while True:
#                    non_Tor_line = f.readline().strip('\n')
#                    if non_Tor_line == 'non-Tor' or non_Tor_line == 'Tor':
#                        break
#                    elif non_Tor_line == '':
#                        break
#                    else:
#                        l.append(non_Tor_line)
#                non_Tor.append(l)
#            elif line == '':
#                break
            
            
            
#print(Tor)


#print(non_Tor)
                
                
                
                    
                    
                    
        
        
        
        
        
        
##    while True:
##        line = f.readline()
##        if line == '':
##            break
##        else:
##            print(line)
#    while True:
#        l = []
#        if f.readline() == 'non-Tor':
#            while True:
#                line = f.readline()
#                if line == 'non-Tor' or line == 'Tor':
#                    break
#                elif line == '':
#                    print('输入完成')
#                    break
#                else:
#                    l.append(line)
#            non_Tor.append(l)
#        elif f.readline() == 'Tor':
#            while True:
#                line = f.readline()
#                if line == 'non-Tor' or line == 'Tor':
#                    break
#                elif line == 0:
#                    print('输入完成')
#                    
#                    break
#                else:
#                    l.append(line)
#            Tor.append(l)
#        elif f.readline() == '':
#            break
#            
#print(Tor)
#print(non_Tor)

                
                    
                
            
        

        
    