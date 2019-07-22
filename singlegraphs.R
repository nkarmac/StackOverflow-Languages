library(cowplot)
library(ggplot2)
library(zoo)
setwd("/home/nick/Desktop/Github/StackOverflow-Languages/languagesv2")

languages = c('java','c','c++','python','.net', 'c#', 'javascript', 'sql','php','assembly',
              'objective-c', 'delphi', 'perl','matlab','ruby','vba','groovy','swift','go','r',
              'sas','abap','fortran', 'dart','scala', 'prolog', 'lisp', 'lua', 'rust', 'ada',
              'f#', 'apex', 'kotlin', 'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell',
              'clojure', 'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 'jquery', 'reactjs')

for(language in languages)
{
  filename <- paste(language, ".csv", sep = "", collapse = NULL)
  lang = read.csv(filename)
  yrmo <- as.yearmon(lang$date, "%Y-%m")
  
  lang$Date <- as.Date(yrmo)
  
  
  g1 <- ggplot(lang, aes(Date, count)) +
    geom_point(
      aes(Date, count),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,count), colour = "blue") +
    ggtitle(paste(language, " count", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_count.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = g1)
  
  g2 <- ggplot(lang, aes(Date, viewcount)) +
    geom_point(
      aes(Date, viewcount),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,viewcount), colour = "blue") +
    ggtitle(paste(language, " viewcount", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_viewcount.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = g2)
  
  g3 <- ggplot(lang, aes(Date, positive)) +
    geom_point(
      aes(Date, positive),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,positive), colour = "blue") +
    ggtitle(paste(language, " positive posts", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_positive.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = g3)
  
  g4 <- ggplot(lang, aes(Date, negative)) +
    geom_point(
      aes(Date, negative),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,negative), colour = "blue") +
    ggtitle(paste(language, " negative posts", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_negative.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = g4)
  
  p1 <- ggplot(lang, aes(Date, count)) +
    geom_point(
      aes(Date, count),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,count), colour = "blue", span = 0.1) +
    ggtitle(paste("localized ", language, " count", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_count_local.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = p1)
  
  p2 <- ggplot(lang, aes(Date, viewcount)) +
    geom_point(
      aes(Date, viewcount),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,viewcount), colour = "blue", span = 0.1) +
    ggtitle(paste("localized ", language, " viewcount", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_viewcount_local.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = p2)
  
  p3 <- ggplot(lang, aes(Date, positive)) +
    geom_point(
      aes(Date, positive),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,positive), colour = "blue", span = 0.1) +
    ggtitle(paste("localized ", language, " positive posts", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_positive_local.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = p3)
  
  p4 <- ggplot(lang, aes(Date, negative)) +
    geom_point(
      aes(Date, negative),
      size = 1, colour = "green") +
    geom_smooth(aes(Date,negative), colour = "blue", span = 0.1) +
    ggtitle(paste("localized ", language, " negative posts", sep = "", collapse = NULL)) +
    scale_x_date(date_breaks = "3 months", date_labels = "%Y-%m") +
    theme(text = element_text(size=12), axis.text.x = element_text(angle=55, hjust = 1))
  
  outfile = paste(language, "_negative_local.png", sep = "", collapse = NULL)
  ggsave(outfile, plot = p4)
  
  
}