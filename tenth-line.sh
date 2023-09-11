# Read from the file file.txt and output the tenth line to stdout.
# Using sed
sed -n '10p' file.txt

# Using awk
awk 'NR == 10' file.txt