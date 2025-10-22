# Script to create the session content files for Hugo from a csv file.

def main():
    import csv, sys, os
    from slugify import slugify
    
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = "teams.csv"

    dirname = "teams"
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
            members = row['integrantes'].split(",")
            content = row['justificacion']
            reto1 = row['reto1']
            reto2 = row['reto2']
            
            slug = slugify(title)
            filename =  f"teams/{slug}.md"

            with open(filename, "w") as f:
                f.write("---\n")
                f.write(f"title: \"{title}\"\n")
                f.write("members:\n")
                for s in members:
                    f.write(f" - {s}\n")
                f.write(f"reto: {reto1}\n")
                f.write(f"reto2: {reto2}\n")
                f.write("---\n\n")
                f.write(content)


if __name__ == "__main__": 
	main() 

