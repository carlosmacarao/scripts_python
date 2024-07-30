medida = float(input('Uma distancia em metros: '))

cm = medida * 100
mm = medida * 1000

input('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))