﻿param([string]$m = "")

# If the commit message is null, exit script
if($m -eq ""){
    Write-Host "Must enter a commit message";
    exit;
}

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

# Push to git
git add .
git commit -m "'$m'"