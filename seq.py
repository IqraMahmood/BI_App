######################
# Import libraries
######################

import streamlit as st
import pandas as pd
import numpy as np # linear algebra
import Bio
from Bio.Seq import Seq
from Bio.SeqUtils import GC
from PIL import Image

######################
# Page Title
######################

image = Image.open('Bioinformatics web App.png')
st.image(image, use_column_width=True)
st.title("Bioinformatics Web App")
st.markdown('''
### The app is developed by iqra Mahmood called ***BI APP***
''')

######################
# Input Text Box
######################

st.header('Enter DNA sequence')
sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string
DNA = my_dna = Seq(sequence)


######################
# selectbox
######################


DNA = Seq(sequence)
# st.write(DNA)

st.header('DNA operations')
options = ['Transcription','Translation','GC content','Reverse Complement']
st.text("DNA can perform many function Some are given below:")
st.write(options)
input, display = st.columns(2)
function_name = input.selectbox("Select an Operation", options = ['Transcription','Translation','GC content','Reverse Complement'])

######################
# DNA operations
######################

if function_name == 'Transcription':
    st.header('***Transcription***')
    st.text("""
    Transcription is the process by which the genetic information stored in DNA 
    is used to produce a complementary RNA strand. In more detail, the DNA base sequence 
    is first copied into an RNA molecule, called premessenger RNA, by messenger RNA 
    (mRNA) polymerase.""")
    mRNA = DNA.transcribe()
    st.write("The RNA Sequence after transcription is", mRNA)
if function_name == 'Translation':
    st.header('***Translation***')
    st.text("""
    In molecular biology and genetics, translation is the process in which ribosomes
    in the cytoplasm or endoplasmic reticulum synthesize proteins after the process of transcription
    of DNA to RNA in the cell's nucleus.""")
    
    mRNA = DNA.transcribe()
    protein = mRNA.translate()
    st.write("The Protein Sequence after translation is")
    st.write(protein)
if function_name == 'GC content':
    st.header('***GC content***')
    st.text("""
    In molecular biology and genetics, GC-content (or guanine-cytosine content) is the percentage
    of nitrogenous bases in a DNA or RNA molecule that are either guanine (G) or cytosine (C).
    
    Aim for the GC content to be between 40 and 60% with the 3' of a primer ending in G or C to promote binding. 
    This is known as a GC Clamp.  The G and C bases have stronger hydrogen bonding and help with the stability of the primer.
    
    Higher GC content has higher thermal stability while lower GC content has low thermostability. 
    """)
    st.subheader("GC content of given sequence is:")
    st.write("GC% Percent:\t" + str(GC(DNA)) + " %")
if  function_name == 'Reverse Complement':
    st.header('***Complement / Reverse Complement***')
    st.text("""
    
    In biology, specifically in terms of genetics and DNA, complementary means that the polynucleotide 
    strand paired with the second polynucleotide strand has a nitrogenous base sequence that is the
    reverse complement, or the pair, of the other strand
    """)
    st.text("""
    The reverse complement of a DNA sequence is formed by reversing the letters, interchanging A and T 
    and interchanging C and G. Thus the reverse complement of ACCTGAG is CTCAGGT.
    """)
    st.subheader("Complement of given sequence is:")
    st.write(DNA.complement() + " - ")
    st.subheader("Reverse Complement of given sequence is:")
    st.write(DNA.reverse_complement() + " - ")    
