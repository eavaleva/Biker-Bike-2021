
# Gemaakt door Eleonora Avaleva student: 20220545

#De applicatie zal de CSV document lezen, hierna voegt die de gevonde informatie in de text widget van de student overview tabel.

from src.layout import BikerApp


def main():
    try:
        bikerApp = BikerApp()

        bikerApp.app.mainloop()

    except KeyboardInterrupt:
        print('Successfully closed application')


if __name__ == '__main__':
    main()
