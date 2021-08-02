import tarfile
import os
import gzip
import shutil
################################################################
#c=1
################################################################
entries = os.listdir('/home/skd/Desktop/MAN_LIPI/all_zipped_assembly')
################################################################
for members in entries:
    t = tarfile.open('/home/skd/Desktop/MAN_LIPI/all_zipped_assembly/'+members, "r")
    for members in t.getmembers():
        t.extract(members,'/home/skd/Desktop/MAN_LIPI/untarred_files')
################################################################
entries1 = os.listdir('/home/skd/Desktop/MAN_LIPI/untarred_files')
for every in entries1:
    try:
        entries2=os.listdir('/home/skd/Desktop/MAN_LIPI/untarred_files/'+every)
        for each in entries2:
            if(('scaf' not in each) and ('from' not in each) and ('_genomic.fna.gz' in each)):
                with gzip.open('/home/skd/Desktop/MAN_LIPI/untarred_files/'+every+'/'+each,'rt') as f:
                    file_content =(f.read())
                    with open('/home/skd/Desktop/MAN_LIPI/genomic_fna_files/'+each.split('.gz')[0],'wt') as wr:
                        wr.write(file_content)
    except NotADirectoryError:
        continue
#################################################################