def abbreviateName(name): 
    split_name = name.split(' '); 
    abbrev_name = str(split_name[0][0] + '.' + split_name[1]); 
    return abbrev_name;