from bombacombustivel import Bombacombustivel

bb1 = Bombacombustivel("Gasolina",50.0, 6.72)
bb1.alterarcombustivel()
bb1.status()
print("=======================================================")
bb2 = Bombacombustivel("Gasolina", 100, 6.72)
bb2.abastercerporlitro()
bb2.status()
print("====================================================")
bb3 = Bombacombustivel("Diesel", 100, 3.50)
bb3.abastecerporvalor()
bb3.status()