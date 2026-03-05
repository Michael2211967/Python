#include <stdio.h>
#include <stdlib.h>

#define WIDTH 20
#define HEIGHT 10

char grid[HEIGHT][WIDTH];

// Funktion zum Initialisieren des Rasters
void clearGrid() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = '.';
        }
    }
}

// Funktion zum Anzeigen des Rasters
void printGrid() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            printf("%c ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Funktion zum Zeichnen eines Punktes
void drawPoint(int x, int y, char symbol) {
    if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
        grid[y][x] = symbol;
    } else {
        printf("Ungueltige Koordinaten!\n");
    }
}

int main() {
    clearGrid();
    int x, y;
    char command;
    char symbol = '*';

    printf("Einfaches Malprogramm (Konsole)\n");
    printf("--------------------------------\n");
    printf("Befehle:\n");
    printf("d <x> <y> <symbol> - Zeichne ein Symbol an Position (x, y)\n");
    printf("c                 - Loesche den Bildschirm\n");
    printf("q                 - Beenden\n\n");

    printGrid();

    while (1) {
        printf("Gib einen Befehl ein: ");
        if (scanf(" %c", &command) != 1) {
            // Fehlerbehandlung fuer fehlerhafte Eingabe
            while (getchar() != '\n'); // Eingabepuffer leeren
            printf("Ungueltige Eingabe.\n");
            continue;
        }

        switch (command) {
            case 'd':
                if (scanf("%d %d %c", &x, &y, &symbol) == 3) {
                    drawPoint(x, y, symbol);
                    printGrid();
                } else {
                    printf("Ungueltige Eingabe fuer den Befehl 'd'. Erwarte: d <x> <y> <symbol>\n");
                    while (getchar() != '\n'); // Eingabepuffer leeren
                }
                break;
            case 'c':
                clearGrid();
                printGrid();
                break;
            case 'q':
                printf("Programm beendet.\n");
                return 0;
            default:
                printf("Ungueltiger Befehl.\n");
        }
    }

    return 0;
}