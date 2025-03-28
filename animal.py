class Animal:
    def fazer_som(self):
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Exemplo de uso
def main():
    cachorro = Cachorro()
    gato = Gato()

    print("Cachorro faz:", cachorro.fazer_som())
    print("Gato faz:", gato.fazer_som())

if __name__ == "__main__":
    main()