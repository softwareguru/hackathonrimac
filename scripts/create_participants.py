# Script to create the session content files for Hugo from a csv file.

def main():
    import csv, sys, os
    from slugify import slugify
    
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = "participants.csv"

    dirname = "participants"
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    except OSError:
        print ("Creation of the directory "+dirname+" failed" )


    with open(source_file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            title = row['title']
            content = row['content']
            location = row['location']
            profile = row['profile']
            especialidad = row['especialidad']
            area = row['area']
            link = row['link']
            modalidad = row['modalidad']
            
            slug = slugify(title)
            filename =  f"participants/{slug}.md"

            with open(filename, "w") as f:
                f.write("---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"location: \"{location}\"\n")
                f.write(f"profile: {profile}\n")
                f.write(f"area: {area}\n")
                f.write(f"link: {link}\n")
                f.write("---\n\n")
                f.write(content)


if __name__ == "__main__": 
	main() 

