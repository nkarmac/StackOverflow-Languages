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
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,count), colour = "green")
  
  g2 <- ggplot(lang, aes(Date, viewcount)) +
    geom_point(
      aes(Date, viewcount),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,viewcount), colour = "green")
  
  g3 <- ggplot(lang, aes(Date, positive)) +
    geom_point(
      aes(Date, positive),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,positive), colour = "green")
  
  g4 <- ggplot(lang, aes(Date, negative)) +
    geom_point(
      aes(Date, negative),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,negative), colour = "green")
  
  p1 <- ggplot(lang, aes(Date, count)) +
    geom_point(
      aes(Date, count),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,count), colour = "green", span = 0.1)
  
  p2 <- ggplot(lang, aes(Date, viewcount)) +
    geom_point(
      aes(Date, viewcount),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,viewcount), colour = "green", span = 0.1)
  
  p3 <- ggplot(lang, aes(Date, positive)) +
    geom_point(
      aes(Date, positive),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,positive), colour = "green", span = 0.1)
  
  p4 <- ggplot(lang, aes(Date, negative)) +
    geom_point(
      aes(Date, negative),
      size = 1, colour = "blue") +
    geom_smooth(aes(Date,negative), colour = "green", span = 0.1)
  
  myplot <- plot_grid(g1, g2, g3, g4, p1, p2, p3, p4, ncol = 4, labels = 'auto')
  title <- ggdraw() + draw_label(language, fontface='bold')
  
  theplot <- plot_grid(title, myplot, ncol=1, rel_heights=c(0.1, 1))
  
  outfile = paste(language, ".png", sep = "", collapse = NULL)
  
  save_plot(outfile, theplot, dpi = 300, base_aspect_ratio = 4)
}