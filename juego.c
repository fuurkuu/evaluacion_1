#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  srand(time(NULL));
    int numeroSecreto = rand() % (100 + 1);
    int intento, intentosRealizados = 0;
    int intentosMaximos = 10;
    printf("Adivina un número entre 1 y 100.\n");
    do {
        printf("Dime cual crees que es: ");
        scanf("%d", &intento);
        intentosRealizados++;
        if (intento > numeroSecreto) {
            printf("Muy alto. Intenta otra vez.\n");
        } 
        if (intento < numeroSecreto) {
            printf("Muy bajo. Intenta nuevamente.\n");
        } 
        if (intento==numeroSecreto) {
            printf("¡Felicidades! Adivinaste el número en %d intentos.\n", intentosRealizados);
            break;
        }
        if (intentosRealizados == intentosMaximos) {
            printf("Agotaste tus intentos. El número correcto era: %d\n", numeroSecreto);
            break;
        }
    } while (1);
  }
