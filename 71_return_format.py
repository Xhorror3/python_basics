def name_format(fname,lname):
  first_name=fname.title()
  last_name=lname.title()
  return f"{first_name} {last_name}"
name1=input("Enter your first name:")
name2=input("Enter your last name:")
output=name_format(name1,name2)
print(output)
