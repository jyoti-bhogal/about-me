install.packages("LocaTT")
library(LocaTT)
# Create a temporary file path for the FASTQ file to write.
path_to_FASTQ_file<-"data_patient_1_sample_1.fastq"
file_name <- "data_patient_1_sample_1.fastq"
write.fastq(names = file_name, sequences = "", quality_scores = "", file = path_to_FASTQ_file)
file.exists("data_patient_1_sample_1.fastq")
