import os

print()

print("""\t\t1) Creating physical volume
\t\t2) Creating Volume group
\t\t3) Creating Logical Volume 
\t\t4) Exit """)

print()


ch=input("Enter your choice from the menu : ") 

if int(ch)==1:
 os.system("fdisk -l")
 print()

 hd=input("Select hard disk from above and provide hard disk here : ")  

 print("Creating physical volume.....")

 os.system("pvcreate {}".format(hd))

 exit()

if int(ch)==2:
 os.system("pvdisplay")
 print()
 pv=input("Provide your physical volume for contributing to Volume group  from above PV list : ")

 vg=input("provide name for volume group : ")

 print("Creating volume group.....")

 os.system("vgcreate {} {}".format(vg,pv))

 exit()

if int(ch)==3:
 os.system("vgdisplay")
 print()
 
 vg=input("Eneter your volume group name : ")
 lv=input("Enter your logical volume name : ")
 sz=input("Enetr you logical volume size : ")

 print("creating Logical volume.....")

 os.system("lvcreate --size {} --name {} {}".format(sz,lv,vg))

 print("Formatting Logical volume.....")

 os.system("mkfs.ext4 /dev/{}/{}".format(vg,lv))

 mtdir=input("Enetr directory name for mounting. Make sure directory is not available : ")

 print("Mounting logical volume...") 

 os.system("mkdir {}".format(mtdir))

 os.system("mount /dev/{}/{} {}".format(vg,lv,mtdir))

 exit()

if int(ch)==4:
 exit()


  

