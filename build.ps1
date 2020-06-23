$cur_path = Convert-Path Get-Location;

# Remove current pdf
if(Test-Path data\\Resume.pdf){
    Remove-Item data\\Resume.pdf;
}
# Change to job search directory
Set-Location "C:\Users\bgree\Documents\Job-Search"

# Pull the current version of the resume
git pull

# Copy it over
Copy-Item Ben_Greenawald_resume.pdf $cur_path.ToString() + "\data\Resume.pdf"

# Change back
Set-Location $cur_path

# Run the blog build script
python script/generate_site_data.py

