#!/usr/local/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)
folder <- args[1]

# load csv file
print(paste("loading csv in folder:", folder))

list_file <- list.files(path = folder, pattern="*\\.csv$")

for (i in 1:length(list_file))
{
    csv_name <- list_file[i]
    full_path <- file.path(folder, csv_name)
    print(paste("analysing this csv:", full_path))
    data <- read.csv(full_path, header=FALSE)
    # set column names
    names(data) <- c("x", "y", "z", "ex", "int", "kg", "rep")

    pdf(paste(full_path, ".pdf", sep = ""))

    # plot x,y,z and ex
    plot.ts(data[c("x", "y", "z", "ex")], main="Sensors data")

}