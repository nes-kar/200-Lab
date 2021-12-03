hc=1.23984198   ## in eV.microns

Lmin=0.200      ## in microns
Lmax=0.400      ## in microns
Emin=hc/Lmax    ## in eV
Emax=hc/Lmin    ## in eV
Nmin=1
Nmax=201
counter=0
i = 0
for n in range(Nmin, Nmax):    
    for m in range(n + 1, Nmax):
        dE = (-13.6 / m**2) - (- 13.6 / n**2)
        if Emin < dE < Emax:
            counter += 1
print(counter)

