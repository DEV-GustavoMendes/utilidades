def calcular_racao(saco_kg, qntd_gato):
        saco_g = saco_kg * 1000
        qntd_cinco_dias = qntd_gato * 5
        saco_total = saco_g - qntd_cinco_dias

        print(f"O saco de ração é {saco_kg} KG ou {saco_g} g.")
        print(f"Os gatos comem por dia {qntd_gato} g")
        print(f"Em cinco dias os gatos comeram {qntd_cinco_dias} g")
        print(f"Depois de cinco dias resta de ração {saco_total} g")
    
calcular_racao(8, 200)

    


