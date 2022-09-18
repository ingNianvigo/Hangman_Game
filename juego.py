from secrets import choice


def jugar():
    pass



def seleccionar_palabra(palabra):
    data = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0:
                data.append(line.strip())
    if len(data)> 0:
        palabra=choice(data)        
    


if __name__ == '__main__':
    jugar(seleccionar_palabra())