import subprocess
import shlex 


with open('projects2.tex', 'w') as texfile:
 texfile.write('\\documentclass[a4paper,twoside]{report}\n')
 texfile.write('\\usepackage[T1]{fontenc}\n')
 texfile.write('\\usepackage[utf8]{inputenc}\n')
 texfile.write('\\usepackage{lmodern}\n')
 texfile.write('\\usepackage[left=1cm,right=1cm]{geometry}\n')
 texfile.write('\\usepackage{graphicx}\n')
 texfile.write('\\usepackage{subcaption}\n')
 texfile.write('\\usepackage{caption}\n')
 texfile.write('\\usepackage{pdfpages}\n')
 texfile.write('\\usepackage{adjustbox}\n')
 texfile.write('\\begin{document}\n')
 texfile.write('\\begin{figure}[htbp]\n')
 texfile.write('\\begin{subfigure}[htbp]{0.55\\textwidth}\n')
 texfile.write('\\includegraphics[width=0.8\\textwidth, height=5cm]{C:/Preyasee/ipython-3.0.0/VCPython/RapierData/outrights1.pdf}\n')
 texfile.write('\\null\hfill\n')
 texfile.write('\\caption{Digraph.}\n')
 texfile.write('\\label{fig:digraph}\n')
 texfile.write('\\end{subfigure}\n')
 texfile.write('\\begin{subfigure}[htbp]{0.55\\textwidth}\n')
 texfile.write('\\includegraphics[width=0.8\\textwidth, height=5cm]{C:/Preyasee/ipython-3.0.0/VCPython/RapierData/outrights2.pdf}\n')
 texfile.write('\\null\hfill\n')
 texfile.write('\\caption{Digraph.}\n')
 texfile.write('\\label{fig:bubbleplot}\n')
 texfile.write('\\end{subfigure}\n')
 texfile.write('\\end{figure}\n')
 
 texfile.write('\\begin{figure}[htbp]\n')
 texfile.write('\\begin{subfigure}[htbp]{0.55\\textwidth}\n')
 texfile.write('\\includegraphics[width=8cm, height=6cm]{C:/Preyasee/ipython-3.0.0/VCPython/RapierData/bubbleplot.pdf}\n')
 texfile.write('\\null\hfill\n')
 texfile.write('\\caption{Digraph.}\n')
 texfile.write('\\label{fig:digraph}\n')
 texfile.write('\\end{subfigure}\n')
 texfile.write('\\begin{subfigure}[htbp]{0.55\\columnwidth}\n')
 texfile.write('\\includepdf[width=8cm,height=10cm]{C:/Preyasee/ipython-3.0.0/VCPython/RapierData/table1.pdf}\n')
 texfile.write('\\null\hfill\n')
 texfile.write('\\caption{Digraph.}\n')
 texfile.write('\\label{fig:bubbleplot}\n')
 texfile.write('\\end{subfigure}\n')
 texfile.write('\\end{figure}\n')
 texfile.write('\\end{document}\n')
 
 texfile.close()
 proc=subprocess.Popen(shlex.split('pdflatex --shell-escape projects2.tex'))
 proc.communicate()