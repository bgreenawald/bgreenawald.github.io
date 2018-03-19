param(
[string]$message
)

# Remove current pdf
if(Test-Path Resume_2018.pdf){
    Remove-Item Resume_2018.pdf
}
# Change to job search directory
cd "C:\Users\bgree\Documents\Job-Search"

# Pull the current version of the resume
git pull

# Copy it over
Copy-Item Resume_2018.pdf C:\xampp\htdocs\bgreenawald.github.io\Resume_2018.pdf

# Change back
cd "C:\xampp\htdocs\bgreenawald.github.io\"

# Run the blog build script
python generate.py

# Add and push
git add . 
git commit -m $message
git push
