$cur_path = Convert-Path Get-Location;

# Remove current pdf
if(Test-Path Resume.pdf){
    Remove-Item Resume.pdf;
}
# Change to job search directory
Set-Location "C:\Users\bgree\Documents\Job-Search"

# Pull the current version of the resume
git pull

# Copy it over
Copy-Item Ben_Greenawald_resume.pdf $cur_path.ToString() + "\Resume.pdf"

# Change back
Set-Location $cur_path

# Run the blog build script
python generate.py

