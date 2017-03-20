graph = {'Husein Airport': ['Jl. Padjajaran', 'Jl. Industri','Jl. Ciroyom'],
             'Jl. Padjajaran': ['Jl. Diponegoro',' Jl. Banda'],
             'Jl. Industri': ['Jl. Merdeka','Jl. Banda'],
             'Jl. Ciroyom': ['Jl. Garuda','Jl. Banda'],
             
           
         }
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Menuju Husein Airport")
print ("Jl. Banda ,Jl. Padjajaran,Jl. Diponegoro ,Jl. Industri,Jl. Merdeka,Jl. Ciroyom, Jl. Garuda")
print ("\n")
awal = raw_input("Masukan Awal : ")
tujuan = raw_input("Masukan Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
