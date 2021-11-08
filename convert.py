from os import walk

filenames = next(walk('contacts'), (None, None, []))[2]  # [] if no file

print(filenames)

with open("out.vcf", 'w') as v:
    for index,file_name in enumerate(filenames):
        with open(f"contacts/{file_name}") as f:
            input_file = f.readlines()
            print(input_file)

            temp = input_file[2].strip()
            print(temp)
            temp = temp.lstrip()
            print(temp)
            print(temp.split(":")[1])
            full_name = temp.split(":")[1].split(";")
            print(full_name)
            if len(full_name) == 2:
                first_name, last_name = full_name
                new_2 = f"N;CHARSET=UTF-8;ENCODING=8BIT:{last_name};{first_name}"
            else:
                new_2 = full_name[0]

            print(new_2)

            v.write("BEGIN:VCARD")
            v.write("\n")

            v.write("VERSION:2.1")
            v.write("\n")

            v.write(new_2)
            v.write("\n")

            v.write(input_file[3].strip().lstrip())
            v.write("\n")

            v.write("END:VCARD")
            v.write("\n")
