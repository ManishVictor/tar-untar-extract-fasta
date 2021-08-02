import os
import gzip
################################################
entries = os.listdir('/home/skd/manish/lab_work/all_data/chryseobacteria_untarred_files')#the directory where all the NCBI untarred folders are kept 
################################################
#print(entries[0])
for i in range (len(entries)):
    try:#sometimes the directory may not have folders instead text files will be there
        inside=os.listdir('/home/skd/manish/lab_work/all_data/chryseobacteria_untarred_files/'+entries[i])#one by one each folder is traversed
        for each in inside:
            if('_cds_' in each):#if cds is found in folder then the loop executes
                for member in inside:#now it checks for a txt file in the proceeding line
                    if('_assembly_report.txt' in member):#here that text file is seen
                        with open('/home/skd/manish/lab_work/all_data/chryseobacteria_untarred_files/'+entries[i]+'/'+member,'r') as file1:
                            read_f=file1.readlines()#the text file is opened and read for the name of the organism and the strain
                            for every in read_f:##############  same  ###############
                                if("Organism name" in every):
                                    nameoforganism='_'.join((((''.join(every.split(':')[1])).split('\n')[0]).strip(' ')).split(' ')[0:2])#name is extracted here
                                    #print(nameoforganism)
                                if('strain' in every):
                                    strainoforganism=((''.join(every.strip(' ').split(':')[1])).split('\n')[0]).strip(' ')#here the strain is extracted
                                    sst='_'.join(strainoforganism.split(' '))
                            fullnameoforganism=str(nameoforganism+'_'+sst)
                            print(each)
                            print(fullnameoforganism)
                with gzip.open('/home/skd/manish/lab_work/all_data/chryseobacteria_untarred_files/'+entries[i]+'/'+each,'rt') as f:#Now the strain
                    file_content =(f.read())#for which we know from above that it has cds file we do the extraction here
                with open('/home/skd/manish/lab_work/all_data/Chryseobacteria_All_CDS'+'/'+fullnameoforganism+'.fasta','a') as file2:#make a new file where you want the fasta files
                    file2.write(file_content)#just write the content here
            else:#if we donot have the cds files then it skips the loop
                continue
    except NotADirectoryError:#if we have something other than the sequence folder eg .txt file or something else it will skip and run the program
        continue
#########################################################
            
