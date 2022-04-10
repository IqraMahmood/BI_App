# **Bioinformatics WEb App**

Bioinformatics WEb App is a simple app to do 
- Transcription
- Translation
- GC content
- Reverse Complement

Students can use this app to perform these simple task

# Running the BI web app
 To recreate this web app on your own computer, do the following.

### Create conda environment (Optional)
Firstly, we will create a conda environment called streamlit

> conda create -n streamlit python=3.8

Secondly, we will login to the streamlit environment

> conda activate streamlit

### Download GitHub repo
git clone https://github.com/IqraMahmood/BI_App
### Pip install libraries
> pip install -r requirements.txt
### Launch the app
> streamlit run seq.py
