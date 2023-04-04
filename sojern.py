def compare_versions(version1, version2):
    v1= version1.split('.')
    v2=version2.split('.')


    if len(v1) > len(v2):
        for i in range(len(v2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        return 1 #v1 and v2 same but v1 has extra number at end so must be higher version


    else:
        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        
        return -1




            
